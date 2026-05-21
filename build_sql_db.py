# Build SQL Database

import pandas as pd
import sqlite3

# load cleaned csv
df = pd.read_csv("weather_data_clean.csv")

# connect to the database
with sqlite3.connect("db/weather.db") as conn:
    
    # write df into sql table
    df.to_sql("weather", conn, if_exists="replace", index=False)

print("Database created and data inserted successfully.")    
    