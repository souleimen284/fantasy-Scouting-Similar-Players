import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

df = pd.read_csv('ml_ready_players_2025.csv')

# Convert all bool columns to int automatically
bool_cols = df.select_dtypes(include=['bool']).columns
df[bool_cols] = df[bool_cols].astype(int)
# Initialize cluster column
df['cluster'] = -1  # Default value

# Get unique positions excluding Manager
positions = df['position_name'].unique()

# Loop through each position group
for pos in positions:
    print(f"Processing position: {pos}")

    # Filter data for current position
    df_pos = df[df['position_name'] == pos].copy()

    df_features = df_pos.drop(columns=['position_name'])
    df_features = df_features.dropna(axis=1)

    # Scale the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_features)


    kmeans = KMeans(n_clusters=20, random_state=42, n_init='auto')
    clusters = kmeans.fit_predict(X_scaled)
        
   
    n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
    print(f'Number of clusters: {n_clusters}')


    # Assign clusters back to main DataFrame
    df.loc[df['position_name'] == pos, 'cluster'] = clusters
    
# Done
print("✅ Clustering complete. Sample of updated DataFrame:")
print(df[['position_name', 'cluster']].head())
# Assuming your dataframe is named df and cluster column is 'clusters'
unique_clusters = df['cluster'].nunique()
print(f"Number of unique clusters: {unique_clusters}")

df2 = pd.read_csv('full_data_2025.csv')
df2['cluster'] = df['cluster']
df2.to_csv('clustered_data_2025.csv', index=False)
print("data saved to clustered_data_2025.csv ")