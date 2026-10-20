import yfinance as yf
import pandas as pd
from typing import List

def fetch_price_data(tickers: List[str], start_date: str, end_date: str) -> pd.DataFrame:
    data = yf.download(tickers, start=start_date, end=end_date)['Close']
    if isinstance(data, pd.Series):
        data = data.to_frame()
    data = data.dropna()
    return data

if __name__ == "__main__":
    test_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA']
    df = fetch_price_data(test_tickers, '2023-01-01', '2026-01-01')
    print(df.head())