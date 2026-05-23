import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    "data/cleaned_superstore.xlsx"
)

# Convert dates again
df["Order Date"] = pd.to_datetime(df["Order Date"])

print("\nTOTAL SALES BY CATEGORY")
category_sales = df.groupby("Category")["Sales"].sum()

print(category_sales)

print("\nTOTAL PROFIT BY CATEGORY")
category_profit = df.groupby("Category")["Profit"].sum()

print(category_profit)

print("\nTOP 10 STATES BY SALES")

top_states = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_states)

print("\nAVERAGE SALES BY REGION")

region_avg = (
    df.groupby("Region")["Sales"]
    .mean()
)

print(region_avg)

print("\nMONTHLY SALES TREND")

monthly_sales = (
    df.groupby(df["Order Date"].dt.month)["Sales"]
    .sum()
)

print(monthly_sales)

print("\nTOP 5 PRODUCTS BY PROFIT")

top_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print(top_products)