import streamlit as st
from nba_api.stats.endpoints import leaguedashplayerstats


def mip():
    st.subheader("MIP Rankings")

    current_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season="2025-26",
        season_type_all_star="Regular Season",
        per_mode_detailed="PerGame",
        measure_type_detailed_defense="Base",
    )

    last_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season="2024-25",
        season_type_all_star="Regular Season",
        per_mode_detailed="PerGame",
        measure_type_detailed_defense="Base",
    )

    current = current_stats.get_data_frames()[0]
    last = last_stats.get_data_frames()[0]

    current = current[[
        "PLAYER_NAME", "TEAM_ABBREVIATION", "AGE", "GP", "MIN",
        "PTS", "REB", "AST", "STL", "BLK", "FG_PCT", "FG3_PCT", "TOV"
    ]]

    last = last[[
        "PLAYER_NAME", "GP", "MIN", "PTS", "REB", "AST", "FG_PCT", "FG3_PCT"
    ]]

    mip_table = current.merge(
        last,
        on="PLAYER_NAME",
        how="inner",
        suffixes=("_CUR", "_LAST")
    )

    mip_table = mip_table[mip_table["GP_CUR"] >= 40]
    mip_table = mip_table[mip_table["MIN_CUR"] >= 24]
    mip_table = mip_table[mip_table["GP_LAST"] >= 30]
    mip_table = mip_table[mip_table["MIN_LAST"] >= 12]

    mip_table["PTS_IMPROVEMENT"] = mip_table["PTS_CUR"] - mip_table["PTS_LAST"]
    mip_table["REB_IMPROVEMENT"] = mip_table["REB_CUR"] - mip_table["REB_LAST"]
    mip_table["AST_IMPROVEMENT"] = mip_table["AST_CUR"] - mip_table["AST_LAST"]
    mip_table["MIN_IMPROVEMENT"] = mip_table["MIN_CUR"] - mip_table["MIN_LAST"]
    mip_table["FG_IMPROVEMENT"] = mip_table["FG_PCT_CUR"] - mip_table["FG_PCT_LAST"]

    mip_table["MIP_SCORE"] = (
        mip_table["PTS_IMPROVEMENT"] * 4 +
        mip_table["REB_IMPROVEMENT"] * 2.5 +
        mip_table["AST_IMPROVEMENT"] * 2.5 +
        mip_table["MIN_IMPROVEMENT"] * 0.3 +
        mip_table["FG_IMPROVEMENT"] * 25
    )

    mip_table = mip_table.sort_values(
        by="MIP_SCORE",
        ascending=False
    )

    top_3 = mip_table.head(3)

    st.subheader("Top 3 MIP Candidates")
    st.dataframe(top_3)

    st.subheader("Full MIP Rankings")
    st.dataframe(mip_table)
