# STREAMLIT DASHBOARD

import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# load db 
conn = sqlite3.connect("db/weather.db")
df = pd.read_sql_query("SELECT * FROM weather", conn)
conn.close()

# streamlit dashboard

st.title("World City Temperature Dashboard")
st.text("Explore the Weather Around the World")

# section 1 - display dropdown of city - weather data
st.subheader("City Weather Data:")
selected_city = st.selectbox("Select a City to View Weather Details", df["City"])
filtered_city = df[df["City"] == selected_city].iloc[0]
col1, col2, col3 = st.columns(3)
col1.metric("City", filtered_city["City"])
col2.write("Weather Description")
col2.write(filtered_city["Weather Description"])
col3.metric("Temperature", f"({filtered_city['Temperature']} °F)")
