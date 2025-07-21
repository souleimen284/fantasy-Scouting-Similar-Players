import requests
import pandas as pd

# Get data from FPL API
url = "https://fantasy.premierleague.com/api/bootstrap-static/"
response = requests.get(url)
data = response.json()

# Get player data
players = data['elements']
df_players = pd.DataFrame(players)

# Get team and position names
teams = pd.DataFrame(data['teams'])[['id', 'name']].rename(columns={'id': 'team_id', 'name': 'team_name'})
positions = pd.DataFrame(data['element_types'])[['id', 'singular_name']].rename(columns={'id': 'position_id', 'singular_name': 'position_name'})

# Merge team and position info
df_players = df_players.merge(teams, left_on='team', right_on='team_id', how='left')
df_players = df_players.merge(positions, left_on='element_type', right_on='position_id', how='left')

# Optional: drop extra ID columns
df_players.drop(columns=['position_id','special','squad_number','region','has_temporary_code','opta_code', 'corners_and_indirect_freekicks_text' , 'direct_freekicks_text', 'penalties_text'], inplace=True)

# Save to CSV
df_players.to_csv("full_data.csv", index=False)

print("✅ All Premier League players saved to full_data.csv")
