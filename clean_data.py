import pandas as pd
import numpy as np

df = pd.read_csv('data/2020.csv')
df['date'] = pd.to_datetime(df['date'])
df['home'] = np.array(pd.isnull(df['home']), 'int64')
df['game_id'] = np.arange(len(df))
df['winner'] = df['winner'].str.replace('(\d+)\xa0', '')
df['loser'] = df['loser'].str.replace('(\d+)\xa0', '')

df['home_team'] = np.where(df['home'], df['winner'], df['loser'])
df['away_team'] = np.where(df['home'], df['loser'], df['winner'])
df['home_pts'] = np.where(df['home'], df['winner_pts'], df['loser_pts'])
df['away_pts'] = np.where(df['home'], df['loser_pts'], df['winner_pts'])

df_teams = df.melt(id_vars='game_id',value_vars=['home_team', 'away_team'], var_name='home', value_name='team')
df_teams['home'] = np.array(df_teams['home'] == 'home_team', 'int64')
df_pts = df.melt(id_vars='game_id',value_vars=['home_pts', 'away_pts'], var_name='home', value_name='pts')
df_pts['home'] = np.array(df_pts['home'] == 'home_pts', 'int64')

df_long = pd.merge(df_teams, df_pts, on=['game_id', 'home'])
df_long = df_long.sort_values(['game_id', 'home'])
df_long = df_long.reset_index(drop=True)
print(df_long)
