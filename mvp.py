import streamlit as st
from nba_api.stats.endpoints import  leaguedashplayerstats
from nba_api.stats.endpoints import  leaguedashplayerclutch
from nba_api.stats.endpoints import leaguestandings


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
     point_diff= 5, # score difference must be 5 pts or less 
     ahead_behind="Ahead or Behind" # cluch stats from if team is winning or losing 
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
     clutch = clutch_stats.get_data_frames()[0]
     clutch_table = clutch[[
        "PLAYER_NAME",
        "TEAM_ABBREVIATION",
         "PTS",
         "REB",
         "AST",
        "TOV",
        "STL",
        "BLK",
    ]]
     clutch_table["CLUTCH_SCORE"] = (
        clutch_table["PTS"] * 2.0 +
        clutch_table['AST'] * 1.3 +
        (clutch_table['STL'] + clutch_table["BLK"]) * 2 +
        clutch_table['REB'] * 1.3 -
        clutch_table['TOV'] * 4
    )
     mvp_table = mvp_table.merge(
        clutch_table[["PLAYER_NAME","CLUTCH_SCORE"]],
        on = "PLAYER_NAME",
        how= "left"
     )
     mvp_table["CLUTCH_SCORE"] = mvp_table["CLUTCH_SCORE"].fillna(0)
     
     mvp_table = mvp_table[mvp_table["GP"] >= 64] # have to play over 65 games
     mvp_table["MVP_SCORE"] = (
        mvp_table["PTS"] * 1.4 +
        mvp_table["REB"] * 1.2 +
        mvp_table["AST"] * 1.2 +
        mvp_table["CLUTCH_SCORE"] * 1.5 +
        (mvp_table["STL"] + mvp_table["BLK"]) * 2 -
        mvp_table["TOV"] * 4
)
     
     mvp_table = mvp_table.sort_values(
        by="MVP_SCORE",
        ascending=False
     )
     top_3 = mvp_table.head(3)
     st.subheader("Top 3 MVP Candidates")
     st.dataframe(top_3)
     st.dataframe(mvp_table) 

        

     