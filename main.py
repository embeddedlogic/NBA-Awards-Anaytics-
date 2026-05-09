import streamlit as st


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