import pandas as pd

df = pd.read_excel("data/superstoredata.xlsx")

#to print 5 rows
print(df.head())

#to get statistics
print(df.describe())

#to get datatypes
print(df.info())

#toget columns
print("\n columns are")
print(df.columns)