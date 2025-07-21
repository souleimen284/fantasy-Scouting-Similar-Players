import pandas as pd
import matplotlib.pyplot as plt
# Load the data
df = pd.read_csv("full_data_2025.csv")



# generate age and days_in_his_team
df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce')
df['team_join_date'] = pd.to_datetime(df['team_join_date'], errors='coerce')

today = pd.Timestamp.today()

df['age'] = ((today - df['birth_date']).dt.days / 365.25).round(1)
df['years_in_team'] = ((today - df['team_join_date']).dt.days / 365.25).round(1)


df['age'].fillna(df['age'].mean(), inplace=True)
df['years_in_team'].fillna(df['years_in_team'].mean(), inplace=True)

# List the columns you want to drop
columns_to_drop = ['can_transact', 'news', 'news_added', 'removed' , 'code' , 'id' , 'first_name' , 'second_name' , 
                   'web_name' , 'photo','team','team_code','team_id' ,'element_type', 'team_join_date' ,'birth_date','now_cost_rank',
                   'influence_rank','creativity_rank','threat_rank','ict_index_rank','form_rank','points_per_game_rank',
                   'selected_rank']  

# Drop them
df = df.drop(columns=columns_to_drop)

#fill null

df['chance_of_playing_next_round'] = df['chance_of_playing_next_round'].fillna(0)
df['chance_of_playing_this_round'] = df['chance_of_playing_this_round'].fillna(0)
df['ep_next'] = df['ep_next'].fillna(0)

df['corners_and_indirect_freekicks_order'] = df['corners_and_indirect_freekicks_order'].fillna(10)
df['direct_freekicks_order'] = df['direct_freekicks_order'].fillna(10)
df['penalties_order'] = df['penalties_order'].fillna(10)# Select boolean columns except 'position_name'
bool_cols = [col for col in df.columns if col != 'position_name' and pd.api.types.is_bool_dtype(df[col])]

# Convert bool columns to int (False=0, True=1)
df[bool_cols] = df[bool_cols].astype(int)

# For the rest of non-numeric columns (excluding position_name and bool_cols), get dummies
cols_to_dummy = [col for col in df.columns if col != 'position_name' and 
                 (not pd.api.types.is_numeric_dtype(df[col]) and col not in bool_cols)]

df_dummies = pd.get_dummies(df, columns=cols_to_dummy, drop_first=False)

# Show result
print(f"Remaining columns: {df_dummies.columns.tolist()}")
print(f"Total number of columns: {df_dummies.shape[1]}")


# Save to new CSV
df_dummies.to_csv("ml_ready_players_2025.csv", index=False)
print("✅ Cleaned data saved as 'ml_ready_players.csv'")

