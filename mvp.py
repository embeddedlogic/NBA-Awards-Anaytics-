import streamlit as st
from nba_api.stats.endpoints import  leaguedashplayerstats


def mvp():
     st.subheader("MVP Rankings")
     stats = leaguedashplayerstats.LeagueDashPlayerStats( #NBA stats endpoint
        season = "2025-26", # NBA season we want 
        season_type_all_star = "Regular Season",
        per_mode_detailed = "PerGame", # show stats as per game averages
        measure_type_detailed_defense="Base"
)
