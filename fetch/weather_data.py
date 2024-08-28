import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import time

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

# Define the location (latitude and longitude for Toronto, Canada)
lat, lon = 43.65107, -79.347015

def fetch_daily_weather_data(date):
    url = "https://api.openweathermap.org/data/3.0/onecall/day_summary"
    params = {
        'lat': lat,
        'lon': lon,
        'date': date.strftime('%Y-%m-%d'),  # Format date as YYYY-MM-DD
        'appid': api_key,
        'units': 'metric'  # Set units to metric
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(f"Successfully fetched data for {date.strftime('%Y-%m-%d')}")
        return response.json()
    else:
        print(f"Failed to fetch data for {date}: {response.status_code} - {response.text}")
        return None

def collect_weather_data():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 7, 31)

    weather_data = []
    current_date = start_date

    while current_date <= end_date:
        data = fetch_daily_weather_data(current_date)
        if data:
            weather_data.append(data)
        current_date += timedelta(days=1)

    # Convert the list of JSON data to a DataFrame
    weather_df = pd.json_normalize(weather_data)

    # Save data to CSV
    weather_df.to_csv('data/weather_data_2022_2024.csv', index=False)

    return weather_df

if __name__ == "__main__":
    df = collect_weather_data()
    print(df.head())