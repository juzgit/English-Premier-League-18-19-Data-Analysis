import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/gadzi/OneDrive/Desktop/Football-DA/data/clean_england-premier-league-teams-2018-to-2019-stats.csv")

# removing the whitespaces aroudn the columns
df.columns = df.columns.str.strip()

#adding the Points column
df['Points'] = (df['wins'] * 3) + df['draws']

#a dictionary to abbreviate the selected columns
column_abbreviations = {
    'team_name': 'TEAM',
    'league_position': 'POS',
    'matches_played': 'MP',
    'wins': 'W',
    'draws': 'D',
    'losses': 'L',
    'goals_scored': 'GS',
    'goals_conceded': 'GC',
    'goal_difference': 'GD',
    'Points' : 'PTS'
}


#abbreviated the columns
df_select = df[list(column_abbreviations.keys())].rename(columns=column_abbreviations)

#sorting the table by Points, Goal Difference and Goals Scored
df_select = df_select.sort_values(by=['PTS','GD', 'GS'], ascending=False)
df_select.reset_index(drop=True, inplace=True)

fig, ax = plt.subplots(figsize=(14,10))
ax.axis('off')

fig.suptitle('English Premier League 2018/19', fontsize=16, fontweight = 'bold', ha='center', y=0.95)

#Using the table to display the league table
table = ax.table(cellText=df_select.values, colLabels=df_select.columns, cellLoc='center', loc='center')

table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.4, 1.6)

#the text doesn't overlap
for col_num in range (len(df_select.columns)):
    max_len = max(df_select.iloc[:, col_num].apply(lambda x: len(str(x))))
    for row_num in range(len(df_select)):
        cell = table[(row_num + 1, col_num)]
        cell.set_width(max_len * 0.05)

for row_num in range(1, len(df_select) + 1):
    cell = table[(row_num, 0)]
    cell.set_text_props(wrap=True)
    cell.set_fontsize(10)
#display the league table
plt.show()