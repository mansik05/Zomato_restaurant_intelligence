
import streamlit as st
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Zomato Restaurant Intelligence",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ Zomato Restaurant Intelligence")
st.caption(
    "Restaurant analytics, review sentiment analysis "
    "and K-Means clustering insights."
)

# --------------------------------------------------
# LOAD EXISTING PIPELINE OUTPUTS
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "outputs"

restaurants_path = OUTPUT_DIR / "restaurant_clusters.csv"
profile_path = OUTPUT_DIR / "cluster_profile.csv"
reviews_path = OUTPUT_DIR / "reviews_with_sentiment.csv"

if not all([restaurants_path.exists(), profile_path.exists(), reviews_path.exists()]):
    st.error("Required project output files are missing from the outputs folder.")
    st.stop()

restaurants = pd.read_csv(restaurants_path)
profile = pd.read_csv(profile_path)
reviews = pd.read_csv(reviews_path)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.header("Dashboard Filters")

clusters = sorted(restaurants["cluster"].dropna().unique().tolist())

selected_clusters = st.sidebar.multiselect(
    "Select restaurant clusters",
    options=clusters,
    default=clusters
)

filtered_restaurants = restaurants[
    restaurants["cluster"].isin(selected_clusters)
].copy()

# --------------------------------------------------
# OVERVIEW METRICS
# --------------------------------------------------
st.subheader("Project Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Restaurants", len(restaurants))
c2.metric("Customer Reviews", len(reviews))
c3.metric("Clusters", restaurants["cluster"].nunique())

avg_rating = restaurants["avg_review_rating"].mean()

c4.metric(
    "Average Review Rating",
    f"{avg_rating:.2f}" if pd.notna(avg_rating) else "N/A"
)

st.divider()

# --------------------------------------------------
# CLUSTER DISTRIBUTION
# --------------------------------------------------
st.subheader("Restaurant Cluster Distribution")

cluster_counts = (
    filtered_restaurants["cluster"]
    .value_counts()
    .sort_index()
)

st.bar_chart(cluster_counts)

# --------------------------------------------------
# CLUSTER PROFILE
# --------------------------------------------------
st.subheader("Cluster Profile")

filtered_profile = profile[
    profile["cluster"].isin(selected_clusters)
].copy()

st.dataframe(
    filtered_profile,
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# RATING ANALYSIS
# --------------------------------------------------
st.subheader("Restaurant Rating Analysis")

rating_data = filtered_restaurants[
    ["Name", "cluster", "avg_review_rating"]
].dropna()

if not rating_data.empty:
    st.bar_chart(
        rating_data.groupby("cluster")["avg_review_rating"].mean()
    )

# --------------------------------------------------
# COST ANALYSIS
# --------------------------------------------------
st.subheader("Average Cost Analysis")

cost_data = filtered_restaurants[
    ["cluster", "cost_numeric"]
].dropna()

if not cost_data.empty:
    st.bar_chart(
        cost_data.groupby("cluster")["cost_numeric"].mean()
    )

# --------------------------------------------------
# SENTIMENT ANALYSIS
# --------------------------------------------------
st.subheader("Customer Review Sentiment")

sentiment_counts = reviews["sentiment"].value_counts()

st.bar_chart(sentiment_counts)

sentiment_percentage = (
    reviews["sentiment"].value_counts(normalize=True) * 100
)

st.subheader("Sentiment Distribution (%)")

st.dataframe(
    sentiment_percentage.rename("Percentage").reset_index(),
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# RESTAURANT EXPLORER
# --------------------------------------------------
st.subheader("Restaurant Explorer")

search = st.text_input("Search restaurant by name")

explorer_data = filtered_restaurants.copy()

if search:
    explorer_data = explorer_data[
        explorer_data["Name"].astype(str).str.contains(
            search, case=False, na=False
        )
    ]

display_columns = [
    col for col in [
        "Name",
        "Cuisines",
        "Cost",
        "rating",
        "avg_review_rating",
        "review_count",
        "positive_pct",
        "negative_pct",
        "cluster"
    ]
    if col in explorer_data.columns
]

st.dataframe(
    explorer_data[display_columns],
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# CLUSTERED DATA DOWNLOAD
# --------------------------------------------------
st.subheader("Download Analysis")

csv_data = filtered_restaurants.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Clustered Restaurant Data",
    data=csv_data,
    file_name="zomato_restaurant_clusters.csv",
    mime="text/csv"
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()

st.caption(
    "Zomato Restaurant Intelligence | "
    "Exploratory Data Analysis | Lexicon-Based Sentiment | "
    "K-Means Clustering"
)
