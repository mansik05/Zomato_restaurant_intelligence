from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_eda_charts(df, outdir):
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    charts = []
    if df["cost"].notna().any():
        fig, ax = plt.subplots(); ax.hist(df["cost"].dropna(), bins=10); ax.set_title("Restaurant Cost Distribution")
        p=outdir/"cost_distribution.png"; fig.savefig(p, bbox_inches="tight"); plt.close(fig); charts.append(p)
    if df["rating"].notna().any():
        fig, ax = plt.subplots(); ax.hist(df["rating"].dropna(), bins=10); ax.set_title("Rating Distribution")
        p=outdir/"rating_distribution.png"; fig.savefig(p, bbox_inches="tight"); plt.close(fig); charts.append(p)
        if df["cost"].notna().any():
            fig, ax = plt.subplots(); sns.scatterplot(data=df, x="cost", y="rating", ax=ax); ax.set_title("Cost vs Rating")
            p=outdir/"cost_vs_rating.png"; fig.savefig(p, bbox_inches="tight"); plt.close(fig); charts.append(p)
    return charts
