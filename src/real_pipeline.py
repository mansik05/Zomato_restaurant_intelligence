from pathlib import Path
import re
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

POSITIVE = set('good great excellent amazing delicious tasty love loved friendly fresh wonderful awesome perfect recommend best pleasant nice fantastic yummy prompt courteous'.split())
NEGATIVE = set('bad poor terrible awful disappointing disappointed hate hated cold slow rude worst overpriced dirty unhygienic bland tasteless pathetic'.split())
def sentiment(text):
    words=re.findall(r'[a-z]+',str(text).lower()); p=sum(w in POSITIVE for w in words); n=sum(w in NEGATIVE for w in words)
    score=p-n; return score, ('positive' if score>0 else 'negative' if score<0 else 'neutral')
def norm(s): return re.sub(r'\s+',' ',str(s).strip().lower())
def parse_cost(s):
    s=str(s).replace(',','').strip(); m=re.search(r'\d+(?:\.\d+)?',s); return float(m.group()) if m else None

def run(meta_path, reviews_path, output_dir, k=4):
    out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
    meta=pd.read_csv(meta_path); reviews=pd.read_csv(reviews_path)
    meta.columns=[c.strip() for c in meta.columns]; reviews.columns=[c.strip() for c in reviews.columns]
    meta['name_key']=meta['Name'].map(norm); reviews['name_key']=reviews['Restaurant'].map(norm)
    reviews['rating_numeric']=pd.to_numeric(reviews['Rating'],errors='coerce')
    reviews['review_clean']=reviews['Review'].fillna('').astype(str)
    sentiments=reviews['review_clean'].map(sentiment)
    reviews['sentiment_score']=sentiments.map(lambda x:x[0]); reviews['sentiment']=sentiments.map(lambda x:x[1])
    reviews['review_length']=reviews['review_clean'].str.len()
    reviews.to_csv(out/'reviews_with_sentiment.csv',index=False)
    agg=reviews.groupby('name_key').agg(review_count=('Review','count'),avg_review_rating=('rating_numeric','mean'),avg_review_length=('review_length','mean'),positive_pct=('sentiment',lambda x:(x=='positive').mean()*100),negative_pct=('sentiment',lambda x:(x=='negative').mean()*100),neutral_pct=('sentiment',lambda x:(x=='neutral').mean()*100),avg_pictures=('Pictures','mean')).reset_index()
    df=meta.merge(agg,on='name_key',how='left')
    df['cost_numeric']=df['Cost'].map(parse_cost)
    df['cuisine_count']=df['Cuisines'].fillna('').map(lambda x: len([a for a in str(x).split(',') if a.strip()]))
    df['collection_count']=df['Collections'].fillna('').map(lambda x: len([a for a in str(x).split(',') if a.strip()]))
    df['rating']=df['avg_review_rating']
    df['reviews_text']=''
    df['cuisines']=df['Cuisines'].fillna('').astype(str); df['collection']=df['Collections'].fillna('').astype(str)
    df['review_length']=df['avg_review_length'].fillna(0)
    num=['cost_numeric','avg_review_rating','review_count','positive_pct','negative_pct','neutral_pct','avg_review_length','avg_pictures','cuisine_count','collection_count']
    cat=['cuisines','collection']
    prep=ColumnTransformer([('num',Pipeline([('impute',SimpleImputer(strategy='median')),('scale',StandardScaler())]),num),('cat',Pipeline([('impute',SimpleImputer(strategy='most_frequent')),('encode',OneHotEncoder(handle_unknown='ignore'))]),cat)])
    X=prep.fit_transform(df)
    k=max(2,min(int(k),len(df)-1)); model=KMeans(n_clusters=k,random_state=42,n_init=10); labels=model.fit_predict(X); df['cluster']=labels
    score=silhouette_score(X,labels) if len(set(labels))>1 else float('nan')
    df.to_csv(out/'restaurant_clusters.csv',index=False)
    profile=df.groupby('cluster').agg(restaurants=('Name','count'),avg_cost=('cost_numeric','mean'),avg_rating=('avg_review_rating','mean'),avg_review_count=('review_count','mean'),positive_pct=('positive_pct','mean'),negative_pct=('negative_pct','mean')).reset_index()
    profile.to_csv(out/'cluster_profile.csv',index=False)
    pd.DataFrame([{'k':k,'silhouette_score':score,'restaurants':len(df),'reviews':len(reviews),'matched_restaurants':int(df['review_count'].notna().sum())}]).to_csv(out/'model_metrics.csv',index=False)
    # EDA charts
    charts=[('cost_distribution.png',df['cost_numeric'],'Estimated cost (dataset units)','Restaurant cost distribution'),('rating_distribution.png',df['avg_review_rating'],'Average review rating','Average restaurant rating distribution'),('cost_vs_rating.png',None,None,'Cost vs rating')]
    for fname,series,xlab,title in charts:
        plt.figure(figsize=(8,5))
        if series is not None: series.dropna().plot(kind='hist',bins=20); plt.xlabel(xlab)
        else: plt.scatter(df['cost_numeric'],df['avg_review_rating']); plt.xlabel('Estimated cost'); plt.ylabel('Average rating')
        plt.title(title); plt.tight_layout(); plt.savefig(out/fname,dpi=150); plt.close()
    plt.figure(figsize=(8,5)); profile.set_index('cluster')['restaurants'].plot(kind='bar'); plt.ylabel('Restaurants'); plt.title('Restaurant count by cluster'); plt.tight_layout(); plt.savefig(out/'cluster_counts.png',dpi=150); plt.close()
    print(f'Pipeline complete: {len(df)} restaurants, {len(reviews)} reviews, {df.review_count.notna().sum()} restaurants matched; k={k}, silhouette={score:.4f}')
    return df,profile,score
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(); p.add_argument('--metadata',default='data/restaurant_metadata.csv'); p.add_argument('--reviews',default='data/restaurant_reviews.csv'); p.add_argument('--output',default='outputs'); p.add_argument('--k',type=int,default=4); a=p.parse_args(); run(a.metadata,a.reviews,a.output,a.k)
