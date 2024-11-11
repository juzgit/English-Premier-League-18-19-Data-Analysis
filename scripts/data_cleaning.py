import pandas as pd


df = pd.read_csv("C:/Users/gadzi/OneDrive/Desktop/Football-DA/data/england-premier-league-teams-2018-to-2019-stats.csv")

df.columns = df.columns.str.strip()

cleaned_file_path = "C:/Users/gadzi/OneDrive/Desktop/Football-DA/data/clean_england-premier-league-teams-2018-to-2019-stats.csv"
df.to_csv(cleaned_file_path, index=False)