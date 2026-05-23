import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(
    "data/cleaned_superstore.xlsx"
)

# -----------------------------
# TOTAL SALES BY CATEGORY
# -----------------------------

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()

# -----------------------------
# MONTHLY SALES TREND
# -----------------------------

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.month)["Sales"]
    .sum()
)

plt.figure(figsize=(10, 5))

sns.lineplot(
    x=monthly_sales.index,
    y=monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

# -----------------------------
# PROFIT DISTRIBUTION
# -----------------------------

plt.figure(figsize=(10, 5))

sns.histplot(
    df["Profit"],
    bins=50
)

plt.title("Profit Distribution")

plt.show()

# -----------------------------
# SALES VS PROFIT
# -----------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    x=df["Sales"],
    y=df["Profit"]
)

plt.title("Sales vs Profit")

plt.show()