import streamlit as st
from roty import roty
from mvp import mvp
from mip import mip





st.title("NBA Award Analytics")
award = st.sidebar.selectbox(
    "Select Award",
    [
        "Most Valuable Player(MVP)",
        "Rookie of the Year(ROTY)",
        "Defensive Player of the Year(DPOTY)",
        "Sixth Man of the Year(6MOTY)",
        "Most Improved Player(MIP)",
    ]
)
st.header(f"2026 {award} Predictions")
st.write("NBA analytics dashboard using player stats.")
if award == "Rookie of the Year(ROTY)":
    roty()
elif award == "Most Valuable Player(MVP)":
    mvp()
elif award == "Most Improved Player(MIP)":
    mip()