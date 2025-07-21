# Fantasy Premier League Dataset Columns Explanation (used for model)

## Player Availability & Selection
- **can_select**: Whether the player can be selected (e.g., not injured or suspended).  
- **chance_of_playing_next_round**: % chance player plays next gameweek.  
- **chance_of_playing_this_round**: % chance player plays current gameweek.  
- **status**: Player availability status (e.g., `a` for available, `i` injured, `d` doubtful,  's' Suspended 'u'Unavailable (left) ).  
- **removed**: Whether player is removed from the game (e.g., transferred out). 


## Player Identity & Basic Info
- **team_name**: Team full name (e.g., Arsenal).  
- **position_name**: Position name (Goalkeeper, Defender, Midfielder, Forward , manager).  ✅
- **years_in_team**: number of days since the player joined his team 🛠️
- **age**: generated from birth date 🛠️

## Performance & Form
- **form**: Recent form rating (average points over last few games). (season 24 25 all 0) 
- **ep_next**: Expected points next gameweek.  
- **ep_this**: Expected points this gameweek.  
- **event_points**: Points scored in the current gameweek.  
- **total_points**: Total points scored this season.  
- **points_per_game**: Average points per game played.  
- **minutes**: Minutes played this season.  
- **starts**: Number of matches started.  
- **selected_by_percent**: % of fantasy managers owning the player.  
- **transfers_in**: Total transfers in by all managers this season.  
- **transfers_in_event**: Transfers in this gameweek.  
- **transfers_out**: Total transfers out this season.  
- **transfers_out_event**: Transfers out this gameweek.  
- **value_form**: Form relative to player cost.  
- **value_season**: Season value relative to cost.  
- **now_cost**: Current price (in tenths, e.g., 55 = £5.5m).  
- **now_cost_rank_type**: Rank type (e.g., by position).  

## Match & Scoring Stats
- **goals_scored**: Number of goals scored.  
- **assists**: Number of assists.  
- **clean_sheets**: Number of matches with no goals conceded.  
- **goals_conceded**: Goals conceded by the player’s team while playing.  
- **own_goals**: Own goals scored.  
- **penalties_saved**: Penalties saved (for goalkeepers).  
- **penalties_missed**: Penalties missed.  
- **yellow_cards**: Yellow cards received.  
- **red_cards**: Red cards received.  
- **saves**: Number of saves made (goalkeepers).  
- **bonus**: Bonus points scored.  
- **bps**: Bonus point system score (raw score before bonus).  
- **influence**: Composite metric measuring player influence.  
- **creativity**: Composite metric measuring chance creation.  
- **threat**: Composite metric measuring goal threat.  
- **ict_index**: Combined metric (Influence, Creativity, Threat).  

## Expected & Advanced Stats (xG, xA, etc.)
- **expected_goals**: Expected goals (xG).  
- **expected_assists**: Expected assists (xA).  
- **expected_goal_involvements**: xG + xA combined.  
- **expected_goals_conceded**: xG conceded (for defenders/GKs).  
- **expected_goals_per_90**: xG per 90 minutes.  
- **expected_assists_per_90**: xA per 90 minutes.  
- **expected_goal_involvements_per_90**: Combined per 90.  
- **expected_goals_conceded_per_90**: xG conceded per 90.  
- **goals_conceded_per_90**: Actual goals conceded per 90.  
- **saves_per_90**: Saves per 90 minutes.  
- **starts_per_90**: Starts per 90 minutes.  
- **clean_sheets_per_90**: Clean sheets per 90 minutes.  

## Managerial Stats (usually for fantasy managers)
- **mng_win**: Number of wins when player played.  
- **mng_draw**: Number of draws.  
- **mng_loss**: Number of losses.  
- **mng_underdog_win**: Wins as underdog.  
- **mng_underdog_draw**: Draws as underdog.  
- **mng_clean_sheets**: Clean sheets in matches player played.  
- **mng_goals_scored**: Goals scored in matches player played.  

## Rankings & Orders
- **influence_rank_type**, **creativity_rank_type**, **threat_rank_type**, **ict_index_rank_type**: Rank type (usually by position).  
- **form_rank_type**, **points_per_game_rank_type**, **selected_rank_type**: Their respective types.  

## Set Piece Orders & Texts
- **corners_and_indirect_freekicks_order**: Priority order for set pieces.  
- **direct_freekicks_order**: Priority order for direct free kicks.  
- **penalties_order**: Priority order for penalties.  

-**cost_change_event**: Price change in current gameweek (upwards, in tenths).
-**cost_change_event_fall**: Price drop in current gameweek (in tenths).
-**cost_change_start**: Total price rise since season start (in tenths).
-**cost_change_start_fall**: Total price fall since season start (in tenths).
-**dreamteam_count**: Number of times the player made it into the Dream Team (best 11 of the gameweek).



- ## totalnumber of columns : 76
