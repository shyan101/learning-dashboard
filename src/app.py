import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv(
    "data/cleaned_superstore.xlsx"
)

df["Order Date"] = pd.to_datetime(df["Order Date"])

# -----------------------------
# SIDEBAR FILTER
# -----------------------------

st.sidebar.header("FILTER DATA")

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[df["Category"].isin(category)]

# -----------------------------
# KPI METRICS
# -----------------------------

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", total_orders)

st.divider()

# -----------------------------
# SALES BY CATEGORY
# -----------------------------

sales_by_category = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    sales_by_category,
    x="Category",
    y="Sales",
    title="Sales by Category"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# MONTHLY SALES TREND
# -----------------------------

monthly_sales = (
    filtered_df.groupby(
        filtered_df["Order Date"].dt.month
    )["Sales"]
    .sum()
    .reset_index()
)

monthly_sales.columns = ["Month", "Sales"]

fig2 = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# TOP STATES BY SALES
# -----------------------------

top_states = (
    filtered_df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig3 = px.bar(
    top_states,
    x="State",
    y="Sales",
    title="Top 10 States by Sales"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# DATA PREVIEW
# -----------------------------

st.subheader("Dataset Preview")

st.dataframe(filtered_df.head(20))