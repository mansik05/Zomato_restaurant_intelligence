import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv("outputs/restaurant_clusters.csv")

features = [
    "cost_numeric",
    "avg_review_rating",
    "avg_review_length",
    "positive_pct",
    "negative_pct",
    "neutral_pct",
    "avg_pictures",
    "cuisine_count",
    "collection_count",
]

X = df[features].fillna(df[features].median())
X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)

plot_df = pd.DataFrame(components, columns=["PC1", "PC2"])
plot_df["cluster"] = df["cluster"].astype(str)

plt.figure(figsize=(10, 7))

for cluster in sorted(plot_df["cluster"].unique()):
    subset = plot_df[plot_df["cluster"] == cluster]
    plt.scatter(subset["PC1"], subset["PC2"], label=f"Cluster {cluster}", alpha=0.75, s=50)

plt.title("Restaurant Clusters - PCA Visualization")
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)")
plt.legend()
plt.grid(alpha=0.2)
plt.tight_layout()
plt.savefig("outputs/pca_clusters.png", dpi=300)
plt.show()

print("PCA chart regenerated.")
print("Clusters plotted:", sorted(plot_df["cluster"].unique()))
print("Explained variance:", pca.explained_variance_ratio_.sum())
