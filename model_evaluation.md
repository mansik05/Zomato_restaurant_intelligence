# K-Means Model Evaluation – Zomato Restaurant Intelligence

## Objective
Evaluate the restaurant clustering model using multiple unsupervised learning metrics and compare clustering configurations from K=2 to K=6.

## Evaluation Metrics

### 1. Inertia
Measures the sum of squared distances between samples and their assigned cluster centroids. Lower inertia indicates tighter clusters, although inertia generally decreases as the number of clusters increases.

### 2. Silhouette Score
Measures how well-separated and cohesive the clusters are. Scores closer to 1 indicate better separation, while values near 0 indicate overlapping clusters.

### 3. Davies–Bouldin Index
Evaluates similarity between clusters. Lower values generally indicate better-defined clusters.

### 4. Calinski–Harabasz Index
Measures the ratio of between-cluster dispersion to within-cluster dispersion. Higher values generally indicate better-defined clusters.

## Evaluation Results

| K | Inertia | Silhouette | Davies-Bouldin | Calinski-Harabasz |
|---|---:|---:|---:|---:|
| 2 | 887.2105 | 0.2260 | 1.4869 | 39.3404 |
| 3 | 770.8269 | 0.2409 | 1.1985 | 30.1205 |
| 4 | 659.8542 | 0.1892 | 1.4492 | 28.8894 |
| 5 | 596.4319 | 0.1790 | 1.4977 | 26.3921 |
| 6 | 539.2360 | 0.1751 | 1.4963 | 25.2198 |

## Metric-Based Observations

- K=3 achieved the highest silhouette score among the evaluated configurations.
- K=3 achieved the lowest Davies-Bouldin index.
- K=2 achieved the highest Calinski-Harabasz index.
- Inertia decreased as the number of clusters increased.

## Final Exploratory Configuration

K=4 was retained for exploratory restaurant segmentation and business interpretation.

K=4 was not the best-performing configuration across the evaluation metrics. K=3 demonstrated stronger results according to the silhouette score and Davies-Bouldin index, while K=2 had the highest Calinski-Harabasz index.

The decision to retain K=4 was based on exploring a more granular segmentation for descriptive business analysis rather than claiming it was the mathematically optimal clustering configuration.

## Limitations

- The clustering metrics indicate modest cluster separation.
- No single metric definitively establishes the optimal number of clusters.
- The clustering results are exploratory.
- The four-cluster model should not be interpreted as a definitive segmentation of the restaurant market.
- Further experimentation with features and cluster configurations could improve segmentation quality.

## Conclusion

Multiple evaluation metrics were used to assess the K-Means clustering model. The results demonstrate that K=3 performs comparatively well according to silhouette and Davies-Bouldin metrics, while K=2 leads according to the Calinski-Harabasz index.

The four-cluster solution was retained for exploratory analysis to support more granular business interpretation. The results and limitations are documented transparently.
