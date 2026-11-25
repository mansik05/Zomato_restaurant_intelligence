
# Zomato Restaurant Intelligence

## Overview

Zomato Restaurant Intelligence is a Data Science and Machine Learning project designed to analyze restaurant data and customer reviews to uncover insights into restaurant performance, pricing, cuisine diversity, and customer sentiment.

The project combines Exploratory Data Analysis (EDA), data preprocessing, feature engineering, sentiment analysis, unsupervised machine learning, clustering evaluation, and business insight generation.

The objective is to segment restaurants into meaningful groups based on restaurant attributes and customer feedback, helping identify restaurant characteristics, customer satisfaction patterns, and potential areas for improvement.

---

## Problem Statement

The restaurant industry is highly competitive, and understanding customer preferences, restaurant performance, pricing, and customer feedback is essential for data-driven decision-making.

This project aims to:

- Explore restaurant characteristics and customer review data.
- Analyze restaurant pricing, ratings, cuisine diversity, and customer sentiment.
- Extract insights from customer reviews using sentiment analysis.
- Group restaurants into segments using unsupervised machine learning.
- Evaluate clustering performance using multiple evaluation metrics.
- Identify business insights and potential opportunities for restaurant improvement.

---

## Project Objectives

- Perform Exploratory Data Analysis on restaurant and review datasets.
- Clean and preprocess restaurant and customer review data.
- Perform feature engineering to derive useful analytical features.
- Analyze customer reviews using sentiment analysis.
- Apply K-Means clustering to segment restaurants.
- Evaluate clustering models across multiple cluster configurations.
- Visualize restaurant segments and data patterns.
- Generate business insights and exploratory hypotheses.

---

## Dataset

The project uses two datasets.

### 1. Restaurant Metadata

The restaurant metadata dataset contains 105 records and 6 columns.

| Column | Description |
|---|---|
| Name | Restaurant name |
| Links | Restaurant webpage or reference link |
| Cost | Estimated restaurant cost |
| Collections | Restaurant collections |
| Cuisines | Restaurant cuisine categories |
| Timings | Restaurant operating hours |

### 2. Restaurant Reviews

The restaurant reviews dataset contains 10,000 records and 7 columns.

| Column | Description |
|---|---|
| Restaurant | Restaurant associated with the review |
| Reviewer | Reviewer information |
| Review | Customer review text |
| Rating | Customer rating |
| Metadata | Additional review metadata |
| Time | Review timestamp or information |
| Pictures | Review-associated pictures |

---

## Project Workflow

The project follows the following workflow:

1. Data loading
2. Data validation and inspection
3. Data preprocessing
4. Exploratory Data Analysis
5. Feature engineering
6. Sentiment analysis
7. Restaurant-review aggregation
8. Feature preparation
9. K-Means clustering
10. Clustering evaluation
11. Visualization
12. Business insight generation

---

## Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the restaurant dataset and customer review patterns.

The analysis includes:

- Restaurant cost distribution
- Restaurant rating distribution
- Cuisine diversity
- Restaurant collections
- Customer sentiment distribution
- Customer rating and sentiment comparison
- Restaurant cluster distribution
- Correlation analysis
- Restaurant segment comparison

### EDA Visualizations

The project generates the following visualizations:

- Average rating distribution
- Cost distribution
- Cost versus rating
- Cost by cuisine count
- Cuisine count and rating
- Top cuisines
- Top reviewed restaurants
- Rating distribution
- Rating variability
- Correlation heatmap
- Pairplot
- PCA cluster visualization
- Elbow curve
- Silhouette score comparison
- Cluster count visualization
- Sentiment distribution
- Sentiment and rating comparison

The visualizations are stored in the `outputs/` directory.

---

## Data Preprocessing

The data preprocessing pipeline includes:

- Cleaning restaurant metadata.
- Processing restaurant cost information.
- Processing cuisine information.
- Processing collection information.
- Cleaning customer review text.
- Handling missing values.
- Matching restaurant review records with restaurant metadata.
- Aggregating customer reviews at the restaurant level.
- Preparing numerical and categorical features for clustering.

### Restaurant Matching

The project contains 105 restaurants in the metadata dataset.

Customer reviews were successfully matched with 100 restaurants.

Five restaurants did not have matching review aggregates. These restaurants were retained in the final dataset, with missing numerical features handled through preprocessing and imputation.

Therefore, review-based conclusions should be interpreted carefully for restaurants without matched reviews.

---

## Feature Engineering

The project derives analytical features from restaurant metadata and customer reviews.

### Numerical Features

The following features were used for clustering:

- `cost_numeric`
- `avg_review_rating`
- `review_count`
- `positive_pct`
- `negative_pct`
- `neutral_pct`
- `avg_review_length`
- `avg_pictures`
- `cuisine_count`
- `collection_count`

### Categorical Features

The following categorical features were included:

- `cuisines`
- `collection`

### Derived Features

The project includes features such as:

- Average restaurant review rating
- Positive sentiment percentage
- Negative sentiment percentage
- Neutral sentiment percentage
- Average review length
- Average number of pictures
- Cuisine count
- Collection count
- Numeric restaurant cost

---

## Sentiment Analysis

Customer reviews were analyzed using a rule-based sentiment analysis approach.

The sentiment classification method uses predefined positive and negative word lists.

A sentiment score is calculated based on the presence of positive and negative words.

The sentiment labels are:

- Positive
- Neutral
- Negative

### Sentiment Distribution

The analysis of 10,000 customer reviews resulted in:

| Sentiment | Number of Reviews |
|---|---:|
| Positive | 7,017 |
| Neutral | 1,887 |
| Negative | 1,096 |
| Total | 10,000 |

### Sentiment Analysis Observations

- Positive reviews represent the largest sentiment category.
- Neutral reviews represent a smaller portion of the dataset.
- Negative reviews represent the smallest sentiment category.
- Sentiment labels were used to derive restaurant-level sentiment percentages.

### Sentiment and Rating Analysis

The average customer ratings were observed to differ across sentiment categories.

Positive reviews generally had higher ratings, while negative reviews had lower ratings.

Sentiment analysis in this project is lexicon-based and exploratory. It is not based on a trained deep learning sentiment classification model.

---

## Machine Learning Model

### K-Means Clustering

K-Means clustering was used to group restaurants based on their restaurant characteristics and aggregated customer feedback.

The clustering model uses numerical and categorical restaurant features.

### Preprocessing for Clustering

The preprocessing pipeline includes:

- Median imputation for numerical features.
- Most-frequent imputation for categorical features.
- StandardScaler for numerical features.
- OneHotEncoder for categorical features.

### Model Configuration

The clustering model uses:

- Algorithm: K-Means
- Random State: 42
- Number of initializations: 10
- Final exploratory cluster configuration: K = 4

The model was used to explore restaurant segments and identify patterns among restaurants with different pricing, customer feedback, and restaurant characteristics.

---

## Model Evaluation

The K-Means clustering model was evaluated using multiple unsupervised learning metrics.

The models were evaluated across cluster configurations ranging from K = 2 to K = 6.

### Evaluation Metrics

#### 1. Inertia

Inertia measures the sum of squared distances between data points and their assigned cluster centroids.

Lower inertia generally indicates more compact clusters, although inertia decreases as the number of clusters increases.

#### 2. Silhouette Score

The Silhouette Score measures how well data points fit within their assigned clusters compared with other clusters.

Higher values generally indicate better-defined clusters.

#### 3. Davies-Bouldin Index

The Davies-Bouldin Index measures the similarity between clusters based on cluster dispersion and separation.

Lower values generally indicate better clustering.

#### 4. Calinski-Harabasz Index

The Calinski-Harabasz Index evaluates the ratio of between-cluster dispersion to within-cluster dispersion.

Higher values generally indicate better-defined clusters.

### Evaluation Results

| K | Inertia | Silhouette Score | Davies-Bouldin Index | Calinski-Harabasz Index |
|---|---:|---:|---:|---:|
| 2 | 887.2105 | 0.2260 | 1.4869 | 39.3404 |
| 3 | 770.8269 | 0.2409 | 1.1985 | 30.1205 |
| 4 | 659.8542 | 0.1892 | 1.4492 | 28.8894 |
| 5 | 596.4319 | 0.1790 | 1.4977 | 26.3921 |
| 6 | 539.2360 | 0.1751 | 1.4963 | 25.2198 |

### Evaluation Interpretation

- K = 3 achieved the highest Silhouette Score among the tested configurations.
- K = 3 also achieved the lowest Davies-Bouldin Index.
- K = 2 achieved the highest Calinski-Harabasz Index.
- Inertia decreased as the number of clusters increased.

K = 4 was retained for exploratory business segmentation and more granular cluster interpretation rather than being presented as the mathematically optimal configuration.

The final K = 4 configuration achieved a Silhouette Score of approximately 0.1892 in the evaluation script.

The relatively modest silhouette scores indicate that the clusters are exploratory and do not represent strongly separated groups.

Evaluation results are saved in:

- `outputs/clustering_evaluation_metrics.csv`
- `model_evaluation.md`

---

## Restaurant Segmentation

The final exploratory model generated four restaurant clusters.

### Cluster Summary

| Cluster | Restaurants | Average Cost | Average Rating | Positive Sentiment % | Negative Sentiment % |
|---|---:|---:|---:|---:|---:|
| Cluster 0 | 46 | ₹804 | 3.54 | 74.32% | 10.59% |
| Cluster 1 | 34 | ₹479 | 3.27 | 53.71% | 15.18% |
| Cluster 2 | 23 | ₹1,520 | 4.17 | 87.26% | 5.83% |
| Cluster 3 | 2 | ₹1,100 | 4.05 | 68.50% | 6.00% |

---

### Cluster 0: Mid-Range Restaurant Segment

- 46 restaurants
- Average cost: approximately ₹804
- Average rating: approximately 3.54
- Positive sentiment: approximately 74.32%
- Negative sentiment: approximately 10.59%

This cluster represents a broad restaurant segment with moderate pricing and generally positive customer feedback.

The segment contains a diverse range of restaurants and restaurant types.

---

### Cluster 1: Value-Oriented Segment with Customer Experience Improvement Opportunities

- 34 restaurants
- Average cost: approximately ₹479
- Average rating: approximately 3.27
- Positive sentiment: approximately 53.71%
- Negative sentiment: approximately 15.18%

This cluster has the lowest average rating and positive sentiment percentage among the four clusters.

It also has the highest negative sentiment percentage.

The results suggest potential opportunities for restaurants in this segment to investigate customer experience issues and improve service, food quality, consistency, or other factors identified through individual reviews.

These observations are exploratory and do not establish the causes of customer dissatisfaction.

---

### Cluster 2: Higher-Priced and Higher-Performing Segment

- 23 restaurants
- Average cost: approximately ₹1,520
- Average rating: approximately 4.17
- Positive sentiment: approximately 87.26%
- Negative sentiment: approximately 5.83%

This cluster has the highest average rating and positive sentiment percentage among the four clusters.

It also has the lowest negative sentiment percentage.

The segment represents restaurants with higher estimated costs and comparatively favorable customer feedback.

The observed relationship does not establish that higher pricing causes better customer satisfaction.

---

### Cluster 3: Small Restaurant Segment

- 2 restaurants
- Average cost: approximately ₹1,100
- Average rating: approximately 4.05
- Positive sentiment: approximately 68.50%
- Negative sentiment: approximately 6.00%

This cluster contains only two restaurants.

Although the cluster has favorable average ratings and a relatively low negative sentiment percentage, its very small size limits the reliability and generalizability of conclusions.

This segment should be interpreted cautiously.

---

## Business Insights

The analysis provides several exploratory business insights.

### 1. Customer Feedback Varies Across Restaurant Segments

Different restaurant clusters exhibit differences in average ratings and sentiment distribution.

This suggests that customer feedback patterns may vary across restaurant segments.

### 2. Higher-Priced Restaurants Show More Favorable Feedback in This Dataset

Cluster 2 has the highest average estimated cost and the most favorable average customer feedback.

This represents an observed pattern within this dataset and should not be interpreted as evidence that higher prices directly improve customer satisfaction.

### 3. The Value-Oriented Segment Presents Potential Improvement Opportunities

Cluster 1 has the lowest average rating and the highest negative sentiment percentage.

Restaurants in this segment may benefit from investigating recurring complaints and identifying operational improvements.

### 4. Customer Reviews Provide Additional Analytical Information

Review sentiment percentages provide an additional perspective beyond restaurant ratings.

The combination of ratings and sentiment can help explore customer feedback patterns.

### 5. Restaurant Segmentation Can Support Exploratory Decision-Making

Restaurant clusters can help organize restaurants into broad groups for comparison.

The segmentation may be useful for exploratory analysis, benchmarking, and identifying potential areas for further investigation.

---

## Exploratory Hypotheses

The following hypotheses were developed for exploratory analysis.

### Hypothesis 1

Restaurants with higher estimated costs may have higher average ratings and more positive customer sentiment.

### Hypothesis 2

Restaurants with a higher percentage of positive customer reviews may have higher numeric ratings.

### Hypothesis 3

Restaurants offering a greater variety of cuisines may differ in cost and customer feedback patterns.

### Hypothesis 4

Restaurants with a higher percentage of negative customer reviews may have lower average numeric ratings.

These hypotheses are exploratory and describe relationships that can be investigated using the available data.

They do not establish causality.

---

## Limitations

The project has several limitations.

- The dataset contains 105 restaurant metadata records.
- Only 100 restaurants were successfully matched with review aggregates.
- Five restaurants lack matched review-based analytical features.
- The review dataset contains 10,000 reviews.
- Review counts are relatively constrained for many restaurants.
- Sentiment analysis uses a rule-based lexicon rather than a trained NLP model.
- Rule-based sentiment classification may misclassify sarcasm, context, complex expressions, and mixed sentiments.
- K-Means clustering is sensitive to feature selection, scaling, and the chosen number of clusters.
- The Silhouette Scores indicate relatively modest cluster separation.
- Cluster 3 contains only two restaurants and should be interpreted cautiously.
- Correlations and cluster patterns do not establish causation.
- Review-based conclusions may not generalize beyond the dataset.
- Restaurant matching and imputation can affect the interpretation of cluster results.

---

## Project Structure

```text
Zomato_Restaurant_Intelligence_Completed/
│
├── data/
│   ├── restaurant_metadata.csv
│   └── restaurant_reviews.csv
│
├── src/
│   ├── real_pipeline.py
│   └── ...
│
├── outputs/
│   ├── average_rating_distribution.png
│   ├── cluster_counts.png
│   ├── cluster_profile.csv
│   ├── correlation_heatmap.png
│   ├── cost_by_cuisine_count.png
│   ├── cost_distribution.png
│   ├── cost_vs_rating.png
│   ├── cuisine_count_rating.png
│   ├── elbow_curve.png
│   ├── model_metrics.csv
│   ├── pairplot.png
│   ├── pca_clusters.png
│   ├── rating_distribution.png
│   ├── rating_variability.png
│   ├── restaurant_clusters.csv
│   ├── reviews_with_sentiment.csv
│   ├── review_volume_negative_share.png
│   ├── sentiment_distribution.png
│   ├── sentiment_rating_comparison.png
│   ├── silhouette_by_k.png
│   ├── top_cuisines.png
│   ├── top_reviewed_restaurants.png
│   └── clustering_evaluation_metrics.csv
│
├── business_insights.md
├── hypotheses.md
├── model_evaluation.md
├── evaluate_clustering.py
├── README.md
├── requirements.txt
└── ...
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Zomato_Restaurant_Intelligence_Completed
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Data Pipeline

```bash
python -m src.real_pipeline --metadata data/restaurant_metadata.csv --reviews data/restaurant_reviews.csv --output outputs --k 4
```

The pipeline processes the restaurant and review datasets, performs preprocessing and feature engineering, analyzes review sentiment, applies K-Means clustering, and generates the analytical outputs and visualizations.

---

## Output Files

The project generates analytical outputs in the `outputs/` directory.

### Dataset Outputs

- `restaurant_clusters.csv`
- `reviews_with_sentiment.csv`
- `cluster_profile.csv`

### Model Evaluation

- `model_metrics.csv`
- `clustering_evaluation_metrics.csv`

### Visualizations

- Rating distribution
- Cost distribution
- Cost versus rating
- Cuisine analysis
- Restaurant cluster analysis
- Sentiment analysis
- Correlation heatmap
- PCA visualization
- Elbow curve
- Silhouette score visualization

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- NLP / Rule-Based Sentiment Analysis
- K-Means Clustering
- Exploratory Data Analysis
- Feature Engineering
- Data Visualization

---

## Conclusion

The Zomato Restaurant Intelligence project demonstrates how restaurant metadata and customer review data can be combined to perform exploratory data analysis, sentiment analysis, feature engineering, and unsupervised machine learning.

The project explores restaurant segments based on pricing, restaurant characteristics, and customer feedback.

K-Means clustering was used to generate exploratory restaurant segments, while multiple unsupervised evaluation metrics were used to compare cluster configurations.

Customer reviews were analyzed using a rule-based sentiment approach to derive restaurant-level sentiment features.

The resulting analysis provides exploratory insights into restaurant performance, customer feedback, pricing patterns, and potential areas for further investigation.

The project demonstrates an end-to-end Data Science workflow involving data preprocessing, analysis, feature engineering, machine learning, evaluation, visualization, and business insight generation.

---

## Author

Developed as a Data Science and Machine Learning project focused on restaurant analytics, customer review analysis, sentiment analysis, and unsupervised machine learning.
