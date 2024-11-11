import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/gadzi/OneDrive/Desktop/Football-DA/data/clean_england-premier-league-teams-2018-to-2019-stats.csv")

#removing the white spaces in each column
df.columns = df.columns.str.strip()

#rank teams by average possession in descending order
df_rank = df[['team_name', 'average_possession']].sort_values(by='average_possession', ascending=False).reset_index(drop=True)

print(df_rank)

#choose the figure size
plt.figure(figure=(10, 3))
#customised the palette
custom_palette = sns.light_palette("green", n_colors=len(df_rank), reverse=True)
#show the data using a bar graph
sns.barplot(x='average_possession', y='team_name', data=df_rank, palette=custom_palette)

#show the points each team got 
for index, value in enumerate(df_rank['average_possession']):
    plt.text(value - 1.5, index, f"{value:.1f}", va='center', ha='right', fontsize=10, color='blacky', weight='bold')

#adding labels around the bar graph
plt.suptitle('English Premier League 18/19 Average Possesion Ranking', fontsize=15, fontweight='bold')
plt.ylabel('Teams')
plt.xlabel('Avg. Possession %')

#show the graph
plt.show()