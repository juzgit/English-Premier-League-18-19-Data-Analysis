import pandas as pd


df = pd.read_csv("C:/Users/gadzi/OneDrive/Desktop/Football-DA/data/england-premier-league-teams-2018-to-2019-stats.csv")

null_counts = df.isnull().sum()

column_count = len(df.columns)


print("Data Info:")
print(df.info())
print("First 10 DF")
print(df.head(10))
print("Describe the data")
print(df.describe())
print("DF columns")
print(df.columns)

print("Column Count:")
print(column_count)

print("Any Duplicates:")
print(df.duplicated())

print("Null Values:")
print(null_counts)