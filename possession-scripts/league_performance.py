import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/gadzi/OneDrive/Desktop/Football-DA/data/clean_england-premier-league-teams-2018-to-2019-stats.csv")

df.columns = df.columns.str.strip()

df['Points'] = (df['wins']* 3) + df['draws']

correlation = df[['average_possession', 'Points', 'goals_scored', 'goals_conceded']].corr()
print(correlation)

#correlation between avg. possession, pointsm goals scored and goals conceded.
plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Average Possession vs Goals Conceded')
plt.show()

#regression line (not viable)
#plt.figure(figsize=(10, 6))
#sns.regplot(x='average_possession', y='goals_conceded', data=correlation, scatter_kws={'alpha':0.5})

#annotating each point with its values (not working due to overlapping)
#for i in range(len(correlation)):
#    plt.annotate(f"({df['average_possession'].iloc[i]:.1f}, {df['goals_conceded'].iloc[i]})",
#                 (df['average_possession'].iloc[i], df['goals_conceded'].iloc[i]),
#                 textcoords='offset points', xytext=(5,5), ha='left', fontsize=9)


#plt.title('Regression: Average Possession vs Goals Conceded')
#plt.xlabel('Average Possession (%)')
#plt.ylabel("Goals Conceded")

#plt.show()

#Box plot for Goals Scored
plt.figure(figsize=(8, 6))
sns.boxplot(y='goals_scored', data=df, palette='coolwarm')
plt.title('Distribution of Goals Scored')
plt.show()

# Histogram for Points
plt.figure(figsize=(8, 6))
sns.histplot(df['Points'], kde=True, bins=5, color='blue')
plt.title('Points Distribution')
plt.show()