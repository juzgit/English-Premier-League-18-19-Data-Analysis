# I am looking at goals scored at different intervals 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/gadzi/OneDrive/Desktop/Football-DA/data/clean_england-premier-league-teams-2018-to-2019-stats.csv")

# remove the white spaces in columns
df.columns = df.columns.str.strip()

# getting the total goals for each interval for the whole league
intervals_total = df[['goals_scored_min_0_to_10', 'goals_scored_min_11_to_20', 'goals_scored_min_21_to_30', 'goals_scored_min_31_to_40', 
          'goals_scored_min_41_to_50', 'goals_scored_min_51_to_60', 'goals_scored_min_61_to_70', 
          'goals_scored_min_71_to_80', 'goals_scored_min_81_to_90']].sum()

intervals_total = intervals_total.reset_index()
intervals_total.columns = ['time_interval','total_goals']

plt.figure(figsize=(12, 6))
sns.barplot(x='time_interval', y='total_goals', data=intervals_total, palette='viridis')

#label the graph
plt.title('Total Goals Scored by Time Interval', fontsize=16, fontweight='bold')
plt.xlabel('Time Interval')
plt.ylabel('Total Goals')
plt.xticks(rotation=90)
plt.show()

#Comparing goals scored in the first vs second half for each team
#group the first half intervals together
df['First-half goals'] = df[['goals_scored_min_0_to_10', 'goals_scored_min_11_to_20', 'goals_scored_min_21_to_30', 'goals_scored_min_31_to_40']].sum(axis=1)

#group the second half intervals together
df['Second-half goals'] = df[['goals_scored_min_41_to_50', 'goals_scored_min_51_to_60', 'goals_scored_min_61_to_70', 
                            'goals_scored_min_71_to_80', 'goals_scored_min_81_to_90']].sum(axis=1)

#sort the visuals by team name
df_sorted = df.sort_values('team_name')

#plot the data
plt.figure(figsize=(14, 8))
sns.barplot(x='team_name', y='First-half goals', data=df_sorted, color='steelblue', label='First-Half Goals')

sns.barplot(x='team_name', y='Second-half goals', data=df_sorted, bottom=df_sorted['First-half goals'], color='darkorange', label='Second-Half Goals')

#label the graph
plt.title('First Half vs Second Half Goals by Team', fontsize=16, fontweight='bold')
plt.xlabel('Team')
plt.ylabel('Total Goals')
plt.xticks(rotation=90)
plt.legend(title='Goal Distribution', loc='upper right')

plt.tight_layout()
plt.show()

#tracking the trend of averaged goals scored over time intervals

#get the mean of the time intervals
intervals_means = df[['goals_scored_min_0_to_10', 'goals_scored_min_11_to_20', 'goals_scored_min_21_to_30', 'goals_scored_min_31_to_40', 
          'goals_scored_min_41_to_50', 'goals_scored_min_51_to_60', 'goals_scored_min_61_to_70', 
          'goals_scored_min_71_to_80', 'goals_scored_min_81_to_90']].mean()

intervals_means = intervals_means.reset_index()
#added two columns
intervals_means.columns = ['time_interval', 'avg_goals']

#plot the data
plt.figure(figsize=(10, 6))
sns.lineplot(data=intervals_means, x='time_interval', y='avg_goals', marker='o', color='orange')
plt.title('Average Goals Scored by Time Interval', fontsize=16, fontweight='bold')
plt.xlabel('Time Interval')
plt.ylabel('Average Goals')
plt.xticks(rotation=90)
plt.show()

#Highlighting the correlations between different time intervals

#select all the intervals
goal_intervals = df[['goals_scored_min_0_to_10', 'goals_scored_min_11_to_20', 'goals_scored_min_21_to_30', 'goals_scored_min_31_to_40', 
          'goals_scored_min_41_to_50', 'goals_scored_min_51_to_60', 'goals_scored_min_61_to_70', 
          'goals_scored_min_71_to_80', 'goals_scored_min_81_to_90']]


correlation_matrix = goal_intervals.corr()

#plot the correlation visual
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

plt.title('Correlation Between Goals Scored in Different Time Intervals', fontsize=16)
plt.show()


#top first 10 minutes top scorers

#get the team name column and the first 10 minutes goals scored
top_first_10_min_scorers = df[['team_name', 'goals_scored_min_0_to_10']].sort_values('goals_scored_min_0_to_10', ascending=False)

#plot the data using the bar graph
plt.figure(figsize=(12, 8))
sns.barplot(
    x='goals_scored_min_0_to_10',
    y='team_name',
    data=top_first_10_min_scorers,
    palette='Blues_r'
)

#show the data values
for index, value in enumerate(top_first_10_min_scorers['goals_scored_min_0_to_10']):
    plt.text(value + 0.1, index, str(value), va='center', fontsize=10)

#label the graph
plt.title('Top Scoring Teams in the First 10 Minutes (0-10 minutes)', fontsize=16, fontweight='bold')
plt.xlabel('Goals Scored')
plt.ylabel('Team Name')
plt.xticks(rotation=0)
plt.show()

#mid game top scorers of teams

#group the mid game intervals together
mid_game_interval = ['goals_scored_min_31_to_40', 'goals_scored_min_41_to_50', 'goals_scored_min_51_to_60']
#get the sum of goals of the mid game intervals
df['mid_game_goals_scored'] = df[mid_game_interval].sum(axis=1)

#selected the team name and the new column created 'mid_game_goals_scored'
top_mid_game_scorers = df[['team_name', 'mid_game_goals_scored']].sort_values('mid_game_goals_scored', ascending=False)

#plot the data
plt.figure(figsize=(12, 8))
sns.barplot(
    x='mid_game_goals_scored',
    y='team_name',
    data=top_mid_game_scorers,
    palette='Blues_r'
)

#display the data values for each team
for index, value in enumerate(top_mid_game_scorers['mid_game_goals_scored']):
    plt.text(value + 0.1, index, str(value), va='center', fontsize=10)

#label the graph
plt.title('Goals Scored by Teams (31-60 Minutes)', fontsize=16, fontweight='bold')
plt.xlabel('Goals Scored')
plt.ylabel('Team Name')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#final 10 minutes top scorers

#get the team name column and the final 10 minutes goals scored
top_final_10_min_scorers = df[['team_name', 'goals_scored_min_81_to_90']].sort_values('goals_scored_min_81_to_90', ascending=False)

#plot the data using the bar graph
plt.figure(figsize=(12, 8))
sns.barplot(
    x='goals_scored_min_81_to_90',
    y='team_name',
    data=top_final_10_min_scorers,
    palette='Blues_r'
)

#display the data values
for index, value in enumerate(top_final_10_min_scorers['goals_scored_min_81_to_90']):
    plt.text(value + 0.1, index, str(value), va='center', fontsize=10)

#label the bar graph
plt.title('Top Scoring Teams in Final 10 Minutes (81-90 minutes)', fontsize=16, fontweight='bold')
plt.xlabel('Goals Scored')
plt.ylabel('Team Name')

plt.xticks(rotation=0)
plt.show()

