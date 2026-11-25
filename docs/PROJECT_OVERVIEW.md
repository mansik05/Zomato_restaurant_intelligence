# Project overview and business framing

## Problem statement
Restaurant discovery platforms collect restaurant attributes and customer reviews, but raw records alone do not give a compact view of restaurant positioning, cuisine patterns, value and customer experience. This project analyzes restaurant data and review text to create descriptive insights and exploratory restaurant segments.

## Stakeholders
- Customers: discover restaurants and compare cuisine, price and rating patterns.
- Platform/business teams: understand segment profiles and potential improvement areas.

## Proposed workstreams
1. Exploratory data analysis and hypothesis testing.
2. Data quality checks and feature engineering.
3. Baseline review sentiment scoring.
4. Unsupervised restaurant clustering.
5. Cluster profiling, visualization and recommendations.

## Suggested hypotheses (test, don't assume)
- Costs and ratings may be related.
- Cuisine patterns may vary by city.
- Sentiment may agree with numerical ratings but need not always do so.
- Restaurant data may form interpretable groups based on price, rating, cuisine and review signals.

## Limitations
The demo dataset is synthetic and small; demo metrics and clusters are not business findings. The sentiment method is a simple word-list baseline. Use real data, validate fields and evaluate results before presenting findings.
