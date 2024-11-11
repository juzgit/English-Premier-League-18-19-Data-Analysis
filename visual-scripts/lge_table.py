import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import table

df = pd.read_csv("C:/Users/gadzi/OneDrive/Desktop/Football-DA/data/clean_england-premier-league-teams-2018-to-2019-stats.csv")

#removing the whitespaces
df.columns = df.columns.str.strip()

#Adding the points column
df['Points'] = (df['wins'] * 3) + df['draws']

#sorting the table by Points, Goal Difference and goals scored
df = df.sort_values(by=['Points', 'goal_difference', 'goals_scored'], ascending=False)
df.reset_index(drop=True, inplace=True)

sns.set_style(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.barplot(x='Points', y='team_name', data=df, palette='viridis')

#show each teams points in the bar graph
for index, value in enumerate(df['Points']):
    plt.text(value + 0.2, index, str(value), va='center', ha='left', fontsize=10)

#add labels for the table
plt.suptitle('English Premier League 2018/19', fontsize=16, fontweight = 'bold', ha='center', y=0.95)
plt.ylabel('Points', fontsize=12)
plt.ylabel('Team', fontsize=12)

#show the table
plt.show()

