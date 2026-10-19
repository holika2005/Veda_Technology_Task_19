"""Task 19: Top 10 Products by Sales. Run: python python/top_10_products.py"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_DIR / "data" / "superstore_sample.csv"
OUTPUT_DIR = PROJECT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df = df.dropna(subset=["Product Name", "Sales"])
top10 = (df.groupby("Product Name", as_index=False)
         .agg(Total_Sales=("Sales", "sum"),
              Total_Quantity=("Quantity", "sum"),
              Orders=("Order ID", "nunique"))
         .sort_values(["Total_Sales", "Product Name"], ascending=[False, True])
         .head(10).reset_index(drop=True))
top10.insert(0, "Rank", range(1, len(top10) + 1))
top10["Total_Sales"] = top10["Total_Sales"].round(2)
top10.to_csv(OUTPUT_DIR / "top_10_products.csv", index=False)

plot_data = top10.sort_values("Total_Sales", ascending=True)
plt.figure(figsize=(12, 7))
plt.barh(plot_data["Product Name"], plot_data["Total_Sales"])
plt.title("Top 10 Products by Total Sales")
plt.xlabel("Total Sales"); plt.ylabel("Product")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_10_products_chart.png", dpi=160)
plt.show()
print(top10.to_string(index=False))
