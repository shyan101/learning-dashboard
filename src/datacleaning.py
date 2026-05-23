import pandas as pd
import numpy as ny

df = pd.read_excel("data/superstoredata.xlsx")

print(df.head)

print("\nORIGINAL SHAPE:")
print(df.shape)

# Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

print("\nNEW SHAPE AFTER REMOVING DUPLICATES:")
print(df.shape)

# Create new column
df["Sales Per Quantity"] = df["Sales"] / df["Quantity"]

print("\nNEW COLUMN:")
print(df[["Sales", "Quantity", "Sales Per Quantity"]].head())

# Save cleaned dataset
df.to_csv("data/cleaned_superstore.xlsx", index=False)

print("\nCLEANED DATASET SAVED")