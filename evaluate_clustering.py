from pathlib import Path
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)

# Load the completed restaurant-level dataset
df = pd.read_csv("outputs/restaurant_clusters.csv")

# Features used in the original clustering pipeline
num = [
    "cost_numeric",
    "avg_review_rating",
    "review_count",
    "positive_pct",
    "negative_pct",
    "neutral_pct",
    "avg_review_length",
    "avg_pictures",
    "cuisine_count",
    "collection_count"
]

cat = ["cuisines", "collection"]

# Recreate the original preprocessing
prep = ColumnTransformer([
    (
        "num",
        Pipeline([
            ("impute", SimpleImputer(strategy="median")),
            ("scale", StandardScaler())
        ]),
        num
    ),
    (
        "cat",
        Pipeline([
            ("impute", SimpleImputer(strategy="most_frequent")),
            ("encode", OneHotEncoder(handle_unknown="ignore"))
        ]),
        cat
    )
])

X = prep.fit_transform(df)
if hasattr(X, "toarray"):
    X = X.toarray()

# Evaluate multiple values of K
results = []

for k in range(2, 7):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X)

    results.append({
        "k": k,
        "inertia": model.inertia_,
        "silhouette_score": silhouette_score(X, labels),
        "davies_bouldin_index": davies_bouldin_score(X, labels),
        "calinski_harabasz_index": calinski_harabasz_score(X, labels)
    })

results_df = pd.DataFrame(results)

# Save evaluation results
Path("outputs").mkdir(exist_ok=True)
results_df.to_csv("outputs/clustering_evaluation_metrics.csv", index=False)

print("\n--- Clustering Evaluation Metrics ---")
print(results_df.round(4).to_string(index=False))

print("\n--- K=4 Evaluation ---")
print(results_df[results_df["k"] == 4].round(4).to_string(index=False))

print("\nEvaluation complete.")
print("Saved to outputs/clustering_evaluation_metrics.csv")
