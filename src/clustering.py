import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

NUMERIC = ["cost", "rating", "review_length"]
CATEGORICAL = ["city", "cuisines", "collection"]

def prepare_features(df):
    df = df.copy()
    df["review_length"] = df["reviews"].str.len().astype(float)
    numeric = [c for c in NUMERIC if c in df.columns]
    categorical = [c for c in CATEGORICAL if c in df.columns]
    transformers = []
    if numeric:
        transformers.append(("num", Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), numeric))
    if categorical:
        transformers.append(("cat", Pipeline([("impute", SimpleImputer(strategy="most_frequent")), ("encode", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), categorical))
    prep = ColumnTransformer(transformers, remainder="drop")
    X = prep.fit_transform(df)
    return X, prep

def fit_kmeans(X, k=4):
    if len(X) < 2:
        raise ValueError("At least two rows are required for clustering.")
    k = max(2, min(int(k), len(X)-1))
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X)
    score = silhouette_score(X, labels) if len(set(labels)) > 1 and len(X) > k else float("nan")
    return model, labels, score
