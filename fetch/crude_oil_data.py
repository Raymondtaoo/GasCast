import yfinance as yf
import pandas as pd

def fetch_crude_oil_data():
    ticker = "CL=F"  # WTI Crude Oil Futures

    # Fetch historical data
    crude_oil_data = yf.download(ticker, start="2000-01-01", end="2024-07-31")

    # Save data to CSV
    crude_oil_data.to_csv('data/crude_oil_prices_2000_2024.csv')

    return crude_oil_data

if __name__ == "__main__":
    data = fetch_crude_oil_data()
    print(data.head())