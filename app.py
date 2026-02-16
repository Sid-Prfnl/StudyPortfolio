import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dirk Nowitzki Performance Dashboard")

df = pd.read_csv("E:\Conda projects/data/Dirk.csv")

df["TS_pct"] = df["PTS"] / (2 * (df["FGA"] + 0.44 * df["FTA"]))

metric = st.selectbox(
    "Select Metric",
    ["PTS", "AST", "3P", "FGA", "TS_pct"]
)

st.line_chart(df[metric])

st.write("Summary Statistics")
st.write(df[metric].describe())