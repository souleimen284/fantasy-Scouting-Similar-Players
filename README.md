# 🔍 Fantasy Scouting: Similar Players Finder

This project helps Fantasy Premier League (FPL) managers discover **similar players** using **unsupervised machine learning**. It clusters players based on performance, expected stats, and play style — enabling users to easily find suitable replacements or hidden gems in the game.

---

## 📁 Project Overview

### 1. 🛠️ Data Fetching
- `fetch_players.py`: Fetches real-time data from the official FPL API.

### 2. 🧹 Data Transformation
- `analyse_players.py`: Cleans and transforms the data into a structured format with 76 relevant features.

### 3. 📊 Clustering Model
- Uses **KMeans** to cluster players based on stats and performance.
- Each cluster contains players with similar profiles and roles.

### 4. 🔎 Scouting Tool
- `scout_players.py`: Input a player's name and retrieve a list of similar players in the same cluster.

---

## 📊 Dataset Columns (After Transformation)

### ⚽ Player Availability & Selection
- `can_select`: Whether player can be selected.
- `status`: Availability (`a`, `i`, `d`, `s`, `u`).
- `chance_of_playing_next_round`
- `chance_of_playing_this_round`
- `removed`

### 🧾 Player Identity & Info
- `team_name`, `position_name`, `years_in_team`, `age`

### 📈 Performance & Form
- `form`, `ep_next`, `total_points`, `points_per_game`, `minutes`, `starts`
- `value_form`, `value_season`, `now_cost`, `now_cost_rank_type`

### 🥅 Match & Scoring Stats
- `goals_scored`, `assists`, `clean_sheets`, `yellow_cards`, `red_cards`
- `bps`, `bonus`, `ict_index`, `influence`, `creativity`, `threat`

### 📊 Expected Stats (xG, xA, etc.)
- `expected_goals`, `expected_assists`, `expected_goal_involvements`
- `expected_goals_per_90`, `expected_assists_per_90`
- `expected_goals_conceded_per_90`, `saves_per_90`, `clean_sheets_per_90`

### 🧠 Managerial Stats
- `mng_win`, `mng_draw`, `mng_loss`, `mng_clean_sheets`, etc.

### 🎯 Rankings & Orders
- `ict_index_rank_type`, `form_rank_type`, `selected_rank_type`
- `direct_freekicks_order`, `penalties_order`, `corners_and_indirect_freekicks_order`

---

## 🤖 Machine Learning
- **Algorithm**: KMeans (Unsupervised)
- **Goal**: Group similar players into clusters
- **Input**: 76 statistical and contextual features
- **Output**: Cluster labels for each player

---

## 🧠 Use Case
- Replace injured/suspended players with similar options.
- Discover budget alternatives to expensive picks.
- Build creative differential teams with under-the-radar talent.

---

## 📂 Files
- `fetch_players.py`: Fetches raw player data.
- `analyse_players.py`: Processes and transforms the data.
- `scout_players.py`: Main tool to find similar players by name.

---

## ⚙️ Tools & Libraries
- Python, Pandas, Scikit-learn, Fantasy Premier League API

---

## ✅ Example Usage

```bash
python scout_players.py --player "Mohamed Salah"
