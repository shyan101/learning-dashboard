import pandas as pd
import numpy as np

df = pd.read_excel("data/superstoredata.xlsx")
#SUM
print(df["Sales"].sum())

#Average
print(round(df["Sales"].mean(),2))

#Unique Items
print(df["Category"].unique)