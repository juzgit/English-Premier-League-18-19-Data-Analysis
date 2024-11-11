import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

output_dir = 'C:\\Users\\gadzi\\OneDrive\\Desktop\\Football-DA\\league-percentage'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

df = pd.read_csv("C:/Users/gadzi/OneDrive/Desktop/Football-DA/data/clean_england-premier-league-teams-2018-to-2019-stats.csv")

df.columns = df.columns.str.strip()

#get the sum of matches played, games won, games lost, games drawn
total_games = df['matches_played'].sum()
total_games_won = df['wins'].sum()

total_games_lost = df['losses'].sum()

total_games_drawn = df['draws'].sum()

#calculate the win percentage of the whole league
lge_win_perc = round((total_games_won/total_games) * 100, 2)
print("Win Percentage:")
print(lge_win_perc)

#Display the win percentage of the whole league
fig, ax = plt.subplots(figsize=(3, 1.5))
ax.text(0.5, 0.5, f'Win Percentage%\n{lge_win_perc}', horizontalalignment="center", #horizontalalignment='center' #horinzontalalignment="center"
        verticalalignment="center", fontsize=20, fontweight="bold")
ax.axis("off")
plt.show()

#Calculate the draw percentage of the league
lge_draw_perc = round((total_games_drawn/total_games) * 100, 2)
print("Draw percentage")
print(lge_draw_perc)

#Display the Draws percentage of the whole league card 
fig, ax = plt.subplots(figsize=(3, 1.5))
ax.text(0.5, 0.5, f'Draw Percentage%\n{lge_draw_perc}', horizontalalignment='center',
        verticalalignment="center", fontsize=20, fontweight="bold")
ax.axis("off")
plt.show()




