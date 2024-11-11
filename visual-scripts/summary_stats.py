#importing the libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

output_dir = 'C:\\Users\\gadzi\\OneDrive\\Desktop\\Football-DA\\figures'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#loading the data 
df = pd.read_csv("C:/Users/gadzi/OneDrive/Desktop/Football-DA/data/clean_england-premier-league-teams-2018-to-2019-stats.csv")

#removing the whitespaces in the columns
df.columns = df.columns.str.strip()

#totla games played in the league
total_games = df['matches_played'].sum()
print("Total Games:")
print(total_games)

#total goals scored in the league
goals_scored =df['goals_scored'].sum()
print("Goals Scored:")
print(goals_scored)

#total home wins in the league
home_matches_played = df['matches_played_home'].sum()
print("Total Home Games:")
print(home_matches_played)

#total away matches in the league
away_matches_played = df['matches_played_away'].sum()
print("Total Away Games:")
print(away_matches_played)

#total wins in the league
total_wins = df['wins'].sum()
print("Total wins")
print(total_wins)

#total home wins in the league
total_home_wins = df['wins_home'].sum()
print("Total Home Wins")
print(total_home_wins)

#total away wins in the league
total_away_wins = df['wins_away'].sum()
print("Total Away Wins")
print(total_away_wins)

#total draws in the league
total_draws = df['draws'].sum()
print('Total Draws')
print(total_draws)

#total home draws in the league
total_home_draws = df['draws_home'].sum()
print("Total Home Draws")
print(total_home_draws)

#total away draws in the league
total_away_draws = df['draws_away'].sum()
print("Total Home Draws")
print(total_away_draws)

#total loses in the league
total_losses = df['losses'].sum()
print("Total Losses")
print(total_losses)

#total home losses in the league
total_home_losses = df['losses_home'].sum()
print("Total Home Losses")
print(total_home_losses)

#total away losses in the league 
total_away_losses = df['losses_away'].sum()
print("Total Home Losses")
print(total_away_losses)

#total goals scored card visual
fig, ax = plt.subplots(figsize=(3, 1.5))
ax.text(0.5, 0.5, f'Total Goals Scored\n{goals_scored}', horizontalalignment='center',
        verticalalignment='center', fontsize=20, fontweight='bold')
ax.axis('off')
plt.savefig(os.path.join(output_dir, "goals_scored.png"))
plt.show()

#total wins card visual
fig, ax = plt.subplots(figsize=(3, 1.5))
ax.text(0.5, 0.5, f'Total Wins\n{total_wins}', horizontalalignment='center',
        verticalalignment='center', fontsize=20, fontweight='bold')
ax.axis('off')
plt.savefig(os.path.join(output_dir, "total_wins.png"))
plt.show()

#total home wins card visual
fig, ax = plt.subplots(figsize=(3, 1.5))
ax.text(0.5, 0.5, f'Total Home Wins\n{total_home_wins}', horizontalalignment='center',
        verticalalignment='center', fontsize=20, fontweight='bold')
ax.axis('off')
plt.savefig(os.path.join(output_dir, "total_home_wins.png"))
plt.show()

#total away wins card viusal
fig, ax = plt.subplots(figsize=(3, 1.5))
ax.text(0.5, 0.5, f'Total Away Wins\n{total_away_wins}', horizontalalignment='center',
        verticalalignment='center', fontsize=20, fontweight='bold')
ax.axis('off')
plt.savefig(os.path.join(output_dir, "total_away_wins.png"))
plt.show()

#total draws in the season card visual
fig, ax = plt.subplots(figsize=(3, 1.5))
ax.text(0.5, 0.5, f'Total Draws\n{total_draws}', horizontalalignment='center',
        verticalalignment='center', fontsize=20, fontweight='bold')
ax.axis('off')
plt.savefig(os.path.join(output_dir, 'total_draws.png'))
plt.show()

#total home draws in the season card visual
fig, ax = plt.subplots(figsize=(3, 1.5))
ax.text(0.5, 0.5, f'Total Home Draws\n{total_home_draws}', horizontalalignment='center',
        verticalalignment='center', fontsize=20, fontweight='bold')
ax.axis('off')
plt.savefig(os.path.join(output_dir, 'total_home_draws.png'))
plt.show()

#total away draws in the season card visual
fig, ax = plt.subplots(figsize=(3, 1.5))
ax.text(0.5, 0.5, f'Total Away Draws\n{total_away_draws}', horizontalalignment='center',
        verticalalignment='center', fontsize=20, fontweight='bold')
ax.axis('off')
plt.savefig(os.path.join(output_dir,'total_away_draws.png'))
plt.show()

#total losses in the season card visual
fig, ax = plt.subplots(figsize=(3, 1.5))
ax.text(0.5, 0.5, f'Total Losses\n{total_losses}', horizontalalignment='center',
        verticalalignment='center', fontsize=20, fontweight='bold')
ax.axis('off')
plt.savefig(os.path.join(output_dir,'total_losses.png'))
plt.show()

#total home losses in the season card visual
fig, ax = plt.subplots(figsize=(3, 1.5))
ax.text(0.5, 0.5, f'Total Home Losses\n{total_home_losses}', horizontalalignment='center',
        verticalalignment='center', fontsize=20, fontweight='bold')
ax.axis('off')
plt.savefig(os.path.join(output_dir, 'total_home_losses.png'))
plt.show()

#total away losses in the season card visual
fig, ax = plt.subplots(figsize=(3, 1.5))
ax.text(0.5, 0.5, f'Total Away Losses\n{total_away_losses}', horizontalalignment='center',
        verticalalignment='center', fontsize=20, fontweight='bold')
ax.axis('off')
plt.savefig(os.path.join(output_dir, 'total_away_losses.png'))
plt.show()

