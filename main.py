from src.data_loader import fetch_price_data

def main():
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA']
    start_date = '2023-01-01'
    end_date = '2026-01-01'

    prices = fetch_price_data(tickers, start_date, end_date)
    print(prices.head())

if __name__ == "__main__":
    main()