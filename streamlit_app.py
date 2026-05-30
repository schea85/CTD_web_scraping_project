# STREAMLIT DASHBOARD

import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# load db 
conn = sqlite3.connect("db/weather.db")
df = pd.read_sql_query("SELECT * FROM weather", conn)
conn.close()

# streamlit
st.title("World City Temperature Dashboard")
st.text("Explore the Weather Around the World")

st.write(df.head())