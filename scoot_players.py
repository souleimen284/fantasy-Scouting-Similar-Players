import pandas as pd

# Load your clustered data CSV
df = pd.read_csv('clustered_data_2025.csv')  # make sure this CSV has 'web_name', 'position_name', and 'cluster' columns
def find_similar_players(player_name):
    # Find the player row
    player = df[df['web_name'] == player_name]
    if player.empty:
        print(f"No player found with name '{player_name}'")
        return
    
    pos = player['position_name'].values[0]
    cluster = player['cluster'].values[0]
    
    # Find players with same position and cluster
    similar_players = df[(df['position_name'] == pos) & (df['cluster'] == cluster)]
    
    print(f"Players in the same position '{pos}' and cluster {cluster}:")
    print(similar_players['web_name'].tolist())

find_similar_players("Palmer")
