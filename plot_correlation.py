import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("outputs/restaurant_clusters.csv")

cols = [
    "cost_numeric",
    "review_count",
    "avg_review_rating",
    "positive_pct",
    "negative_pct",
    "avg_review_length",
    "cuisine_count",
    "collection_count",
    "avg_pictures",
]

corr = df[cols].corr()

plt.figure(figsize=(12, 9))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title("Restaurant-Level Feature Correlation")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png", dpi=300)
plt.show()

print("Correlation heatmap regenerated.")
