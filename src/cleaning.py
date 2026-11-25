import pandas as pd

EXPECTED = ["name", "city", "cost", "rating", "cuisines", "collection", "reviews"]

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
    aliases = {"restaurant_name": "name", "average_cost_for_two": "cost", "price": "cost",
               "aggregate_rating": "rating", "review": "reviews", "review_text": "reviews",
               "cuisine": "cuisines", "city_name": "city"}
    for old, new in aliases.items():
        if old in df.columns and new not in df.columns:
            df.rename(columns={old: new}, inplace=True)
    for col in EXPECTED:
        if col not in df.columns:
            df[col] = pd.NA
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_columns(df)
    df = df.dropna(subset=["name"]).copy()
    df["name"] = df["name"].astype(str).str.strip()
    df = df[df["name"].ne("")]
    for col in ["cost", "rating"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    for col in ["city", "cuisines", "collection", "reviews"]:
        df[col] = df[col].fillna("").astype(str)
    # Remove exact duplicate rows only; distinct outlets with the same name are retained.
    df = df.drop_duplicates()
    return df.reset_index(drop=True)
