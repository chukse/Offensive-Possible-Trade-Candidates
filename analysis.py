# Import necessary libraries
import pandas as pd

# Load data
ngs_receiving = pd.read_csv('ngs_receiving.csv')
ngs_rushing = pd.read_csv('ngs_rushing.csv')
team_records = pd.read_csv('team_records.csv')
player_stats_season_2024 = pd.read_csv('player_stats_season_2024 (3).csv')

# Map full team names to abbreviations for filtering purposes
team_name_to_abbr = {
    'Buffalo Bills': 'BUF', 'Miami Dolphins': 'MIA', 'New England Patriots': 'NE',
    'New York Jets': 'NYJ', 'Pittsburgh Steelers': 'PIT', 'Cleveland Browns': 'CLE',
    'Cincinnati Bengals': 'CIN', 'Indianapolis Colts': 'IND', 'Jacksonville Jaguars': 'JAX',
    'Tennessee Titans': 'TEN', 'Denver Broncos': 'DEN', 'Kansas City Chiefs': 'KC',
    'Las Vegas Raiders': 'LV', 'Dallas Cowboys': 'DAL', 'Philadelphia Eagles': 'PHI',
    'Washington Commanders': 'WAS', 'New York Giants': 'NYG', 'Green Bay Packers': 'GB',
    'Detroit Lions': 'DET', 'Minnesota Vikings': 'MIN', 'Chicago Bears': 'CHI',
    'Atlanta Falcons': 'ATL', 'Carolina Panthers': 'CAR', 'New Orleans Saints': 'NO',
    'Tampa Bay Buccaneers': 'TB', 'San Francisco 49ers': 'SF', 'Seattle Seahawks': 'SEA',
    'Los Angeles Rams': 'LA', 'Los Angeles Chargers': 'LAC', 'Arizona Cardinals': 'ARI'
}

# Filter low-performing teams (below 0.5 win percentage)
low_record_teams = team_records[team_records['PCT'] < 0.5]
low_record_team_abbr = low_record_teams['Team'].map(team_name_to_abbr).dropna()

# Filter for 2024 season data
ngs_receiving_2024 = ngs_receiving[(ngs_receiving['season'] == 2024) & (ngs_receiving['team_abbr'].isin(low_record_team_abbr))]
ngs_rushing_2024 = ngs_rushing[(ngs_rushing['season'] == 2024) & (ngs_rushing['team_abbr'].isin(low_record_team_abbr))]
player_stats_season_2024_filtered = player_stats_season_2024[player_stats_season_2024['recent_team'].isin(low_record_team_abbr)]

# Merge player stats with receiving and rushing data to enrich the dataset
merged_receiving = ngs_receiving_2024.merge(player_stats_season_2024_filtered, on='player_display_name', how='inner')
merged_rushing = ngs_rushing_2024.merge(player_stats_season_2024_filtered, on='player_display_name', how='inner')

# WR - Wide Receivers
wr_candidates = merged_receiving[merged_receiving['player_position'] == 'WR']
wr_candidates['trade_rating'] = (
    0.3 * wr_candidates['yards'] + 
    0.3 * wr_candidates['avg_separation'] + 
    0.2 * wr_candidates['percent_share_of_intended_air_yards'] + 
    0.2 * wr_candidates['avg_yac'] +
    0.4 * wr_candidates['receiving_epa'] +
    0.4 * wr_candidates['avg_cushion'] +
    0.3 * wr_candidates['wopr'] +
    0.2 * wr_candidates['catch_percentage'] 
)
top_wr_trade_candidates = wr_candidates.sort_values(by='trade_rating', ascending=False).drop_duplicates('player_display_name').head(20)

# TE - Tight Ends
te_candidates = merged_receiving[merged_receiving['player_position'] == 'TE']
te_candidates['trade_rating'] = (
    0.4 * te_candidates['yards'] + 
    0.2 * te_candidates['avg_separation'] + 
    0.2 * te_candidates['percent_share_of_intended_air_yards'] + 
    0.2 * te_candidates['avg_yac'] +
    0.4 * te_candidates['receiving_epa'] +
    0.4 * te_candidates['avg_cushion'] +
    0.3 * te_candidates['wopr'] + 
    0.2 * te_candidates['catch_percentage'] 
)
top_te_trade_candidates = te_candidates.sort_values(by='trade_rating', ascending=False).drop_duplicates('player_display_name').head(10)

# RB - Running Backs
rb_candidates = merged_rushing[merged_rushing['player_position'] == 'RB']
rb_candidates['trade_rating'] = (
    0.1 * rb_candidates['rush_attempts'] + 
    0.3 * rb_candidates['efficiency'] + 
    0.2 * rb_candidates['rush_yards'] + 
    0.1 * rb_candidates['rush_touchdowns'] +
    0.3 * rb_candidates['avg_rush_yards'] +
    0.3 * rb_candidates['percent_attempts_gte_eight_defenders'] +
    0.2 * rb_candidates['avg_time_to_los'] +
    0.3 * rb_candidates['wopr'] + 
    0.3 * rb_candidates['rushing_epa'] + 
    0.3 * rb_candidates['receiving_epa']
)
top_rb_trade_candidates = rb_candidates.sort_values(by='trade_rating', ascending=False).drop_duplicates('player_display_name').head(20)

# Display or save results
print("Top WR Trade Candidates:\n", top_wr_trade_candidates[['player_display_name', 'team_abbr', 'trade_rating']])
print("\nTop TE Trade Candidates:\n", top_te_trade_candidates[['player_display_name', 'team_abbr', 'trade_rating']])
print("\nTop RB Trade Candidates:\n", top_rb_trade_candidates[['player_display_name', 'team_abbr', 'trade_rating']])

# Optional: Save to CSV
top_wr_trade_candidates.to_csv('top_wr_trade_candidates_2024.csv', index=False)
top_te_trade_candidates.to_csv('top_te_trade_candidates_2024.csv', index=False)
top_rb_trade_candidates.to_csv('top_rb_trade_candidates_2024.csv', index=False)
