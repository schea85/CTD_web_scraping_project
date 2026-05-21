# Weather Data Cleaning

import pandas as pd
import numpy as np

# load csv
weather = pd.read_csv("weather_data_raw.csv")

# create copy
weather_2 = weather.copy()

# weather info before cleaning
print(weather_2.info())
print("\nWeather - First 5 rows: ")
print(weather_2.head())
print("\nWeather - Describe: ")
print(weather_2.describe(include="all"))
print("\n Weather - Shape (rows | columns):")
print(weather_2.shape)

# handle missing values for all columns
print("\nNull count:")
print(weather_2.isnull().sum(), "\n")
weather_2 = weather_2.replace(["N/A", "NA", "null", "None", "--", "", " "], np.nan)
weather_2 = weather_2.dropna()

# handle duplicates
print("\nDuplicates: ", weather_2.duplicated().sum())
print(weather_2[weather_2.duplicated()])
weather_2 = weather_2.drop_duplicates()

# city
weather_2["City"] = weather_2["City"].str.replace("*", "", regex=False).str.strip()

# time, split into 2 columns
weather_2["Time"] = weather_2["Time"].str.strip()
weather_2[["Day", "Time"]] = weather_2["Time"].str.split(" ", n=1, expand=True)

# description
weather_2["Weather Description"] = weather_2["Weather Description"].str.strip()

# temperature
weather_2["Temperature"] = weather_2["Temperature"].str.replace("°F", "")
weather_2["Temperature"] = weather_2["Temperature"].str.strip()
weather_2["Temperature"] = pd.to_numeric(weather_2["Temperature"], errors="coerce")

# rearrange columns
weather_2 = weather_2[["City", "Day", "Time", "Weather Description", "Temperature"]]

print("\nCleaned Data:")
print(weather_2)
print("\n Weather info():")
print(weather_2.info())

# save cleaned data
weather_2.to_csv("weather_data_clean.csv", index=False)