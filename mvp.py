import streamlit as st
from nba_api.stats.endpoints import  leaguedashplayerstats
from nba_api.stats.endpoints import  leaguedashplayerclutch
from nba_api.stats.endpoints import playerdashboardbyonoff


def mvp():
     st.subheader("MVP Rankings")
     stats = leaguedashplayerstats.LeagueDashPlayerStats( #NBA stats endpoint
        season = "2025-26", # NBA season we want 
        season_type_all_star = "Regular Season",
        per_mode_detailed = "PerGame", # show stats as per game averages
        measure_type_detailed_defense="Base",
    )
     clutch_stats = leaguedashplayerclutch.LeagueDashPlayerClutch(
     season="2025-26", # the season
     season_type_all_star="Regular Season", # regular szn only
     per_mode_detailed="PerGame", # game averages 
     measure_type_detailed_defense="Base", # normal stats box score stats 
     clutch_time="Last 5 Minutes", # clutch gene we see who really is clutch
     point_diff=5, # score difference must be 5 pts or less 
     ahead_behind="Ahead or Behind" # cluch stats from if team is winning or losing 
    )
     player_on_off = playerdashboardbyonoff(
     season="2025-26", 
     season_type_playoffs="Regular Season",
     per_mode_detailed="PerGame",
     measure_type_detailed="Advanced", # advanced analtyics stats
     pace_adjust="N", # dont adjust stats based on team pace 
     plus_minus="N", # dont include plus/minus calculations 
     rank="N", # dont add ranking colums 
     )
     mvp = stats.get_data_frames()[0]
     mvp_table = mvp[[
            "PLAYER_NAME",
            "TEAM_ABBREVIATION",
            "AGE",
            "GP",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "PTS",
            "REB",
            "AST",
            "STL",
            "BLK",
            "OREB",
            "DREB",
            "TOV",
            "PLUS_MINUS",

    ]] 