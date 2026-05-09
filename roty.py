import streamlit as st
from nba_api.stats.endpoints import leaguedashplayerstats

def roty():
    st.subheader("ROTY Rankings")
    stats = leaguedashplayerstats.LeagueDashPlayerStats( #NBA stats endpoint
        season = "2025-26", # NBA season we want 
        season_type_all_star = "Regular Season", # Only counting the regular szn
        player_experience_nullable = "Rookie", # Only want the Rookies from this season
        per_mode_detailed = "PerGame", # show stats as per game averages

    )
    rookies = stats.get_data_frames()[0]# return a list if tables from the API
    roty_table = rookies[[
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
    roty_table = roty_table[roty_table["GP"] >= 65] # have to play over 65 games
    roty_table = roty_table[roty_table["MIN"] >= 20] #have 20 mins played
    roty_table["ROTY_SCORE"] = (
        
        roty_table["PTS"] * 0.32 + 
        roty_table["REB"] * 0.15 +
        roty_table["AST"] * 0.15 +
        roty_table["STL"] * 0.10 +
        roty_table["BLK"] * 0.10 +
        roty_table["FG_PCT"] * 15 +
        roty_table["FG3_PCT"] * 10 +
        roty_table["PLUS_MINUS"] * 0.08 -
        roty_table["TOV"] * 0.18
)
    roty_table = roty_table.sort_values(
    by="ROTY_SCORE",
    ascending=False # will sort highest to lowest 
)
    top_3 = roty_table.head(3)

    st.subheader("Top 3 ROTY Candidates")
    st.dataframe(top_3)
    st.subheader("Full ROTY Rankings")
    st.dataframe(roty_table)

