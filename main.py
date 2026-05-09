import streamlit as st
from roty import roty


st.title("NBA Award Predictor")
award = st.sidebar.selectbox(
    "Select Award",
    [
        "Most Valuable Player(MVP)",
        "Rookie of the Year(ROTY)",
        "Defensive Player of the Year(DPOTY)",
        "Sixth Man of the Year(6MOTY)",
        "Most Improved Player(MIP)",
        "Coach of the Year(COY)"
    ]
)
st.header(f"2026 {award} Predictions")
st.write("NBA analytics dashboard using player stats.")
if award == "Rookie of the Year(ROTY)":
    roty()
elif award == "Most Valuable Player(MVP)":
    pass
elif award == "Defensive Player of the Year(DPOTY)":
    pass
elif award == "Sixth Man of the Year(6MOTY)":
    pass
elif award == "Most Improved Player(MIP)":
    pass
elif award == "Coach of the Year(COY)":
    pass
