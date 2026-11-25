import argparse
from pathlib import Path
import pandas as pd
from .cleaning import clean_data
from .sentiment import add_sentiment
from .clustering import prepare_features, fit_kmeans
from .analysis import create_eda_charts

def run(input_path, output_dir, k=4):
    output_dir = Path(output_dir); output_dir.mkdir(parents=True, exist_ok=True)
    raw = pd.read_csv(input_path)
    df = clean_data(raw)
    df = add_sentiment(df)
    charts = create_eda_charts(df, output_dir)
    X, preprocessor = prepare_features(df)
    model, labels, score = fit_kmeans(X, k)
    df["cluster"] = labels
    df.to_csv(output_dir/"restaurant_clusters.csv", index=False)
    profile = df.groupby("cluster").agg(restaurants=("name", "count"), avg_cost=("cost", "mean"), avg_rating=("rating", "mean"), sentiment_positive_pct=("sentiment", lambda s: (s == "positive").mean()*100)).reset_index()
    profile.to_csv(output_dir/"cluster_profile.csv", index=False)
    pd.DataFrame([{"k": model.n_clusters, "silhouette_score": score}]).to_csv(output_dir/"model_metrics.csv", index=False)
    print(f"Finished. Cluster count={model.n_clusters}; silhouette={score:.4f}; outputs={output_dir}")
    print("Charts:", [str(p) for p in charts])
    return df, profile, score

if __name__ == "__main__":
    parser=argparse.ArgumentParser(); parser.add_argument("--input", default="data/demo_restaurants.csv"); parser.add_argument("--output", default="outputs"); parser.add_argument("--k", type=int, default=4)
    args=parser.parse_args(); run(args.input,args.output,args.k)
