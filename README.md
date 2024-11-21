# Trade Candidates Analysis (Offense)- NFL 2024 Season

This project identifies top trade candidates for NFL teams with a focus on wide receivers (WR), tight ends (TE), and running backs (RB). By analyzing advanced stats such as yards, EPA (Expected Points Added), and efficiency metrics, the script provides a ranking of players most suitable for trades.

## Table of Contents
- [Introduction](#introduction)
- [Data Requirements](#data-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Outputs](#outputs)
- [License](#license)

## Introduction
The project aims to assist NFL analysts and teams by identifying top trade candidates based on advanced player statistics. It leverages 2024 season data and focuses on teams with a win percentage below 50%.

## Data Requirements
The script requires the following CSV files:
1. `ngs_receiving.csv` - Next Gen Stats data for receiving players.
2. `ngs_rushing.csv` - Next Gen Stats data for rushing players.
3. `team_records.csv` - Team performance records for the 2024 season.
4. `player_stats_season_2024.csv` - Player statistics for the 2024 season.

Ensure these files are properly formatted and available in the project directory.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. Install required libraries:
   ```bash
   pip install pandas
   ```

## Usage
1. Place the required CSV files in the project directory.
2. Run the script:
   ```bash
   python analysis.py
   ```
3. The script will process the data, calculate trade ratings for players, and output rankings for WRs, TEs, and RBs.

## Outputs
The script generates the following CSV files:
- `top_wr_trade_candidates_2024.csv` - Top 20 wide receiver trade candidates.
- `top_te_trade_candidates_2024.csv` - Top 10 tight end trade candidates.
- `top_rb_trade_candidates_2024.csv` - Top 20 running back trade candidates.

These outputs include:
- Player name
- Team abbreviation
- Trade rating

### Example Output (Console)
```text
Top WR Trade Candidates:
   player_display_name    team_abbr    trade_rating

Top TE Trade Candidates:
   player_display_name    team_abbr    trade_rating

Top RB Trade Candidates:
   player_display_name    team_abbr    trade_rating
```

## License
This project is open-source and available under the [MIT License](LICENSE).
