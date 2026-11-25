# Business Insights – Zomato Restaurant Intelligence

## Cluster 0 – Broad Middle Segment
- Restaurants: 46
- Average cost: approximately 804
- Average rating: 3.54
- Positive sentiment: 74.32%
- Negative sentiment: 10.59%

Business implication:
This is the largest restaurant segment in the dataset. It provides a useful benchmark for restaurants with moderately positive customer feedback and may offer opportunities for improving customer satisfaction.

## Cluster 1 – Customer Experience Improvement Opportunity
- Restaurants: 34
- Average cost: approximately 479
- Average rating: 3.27
- Positive sentiment: 53.71%
- Negative sentiment: 15.18%

Business implication:
This segment has the lowest average rating and positive sentiment share, along with the highest negative sentiment share. Further review analysis could help investigate potential customer experience issues.

## Cluster 2 – High-Performing Premium Segment
- Restaurants: 23
- Average cost: approximately 1520
- Average rating: 4.17
- Positive sentiment: 87.26%
- Negative sentiment: 5.83%

Business implication:
This segment combines higher average cost with the strongest customer feedback metrics. It may be useful to explore customer experience practices and premium positioning.

## Cluster 3 – Small Segment
- Restaurants: 2
- Average cost: approximately 1100
- Average rating: 4.05
- Positive sentiment: 68.50%
- Negative sentiment: 6.00%

Business implication:
The cluster contains only two restaurants. Findings should be treated as exploratory and not generalized.

## Overall Limitations
- K-Means clustering is exploratory.
- The K=4 silhouette score is approximately 0.19, indicating modest cluster separation.
- Five restaurants have no matched review aggregates and were retained through preprocessing imputation.
- Sentiment analysis uses a rule-based lexicon.
- Correlations and cluster averages indicate associations, not causation.
