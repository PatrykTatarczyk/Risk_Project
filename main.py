from src.data_loader import fetch_price_data
from src.returns import log_returns
from src.metrics import mean_log_return, std_log_return,skewness,kurtosis


def main():
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA']
    start_date = '2023-01-01'
    end_date = '2026-01-01'

    prices = fetch_price_data(tickers, start_date, end_date)
    print(prices.head())

    returns = log_returns(prices)
    print(returns.head())

    mean_returns = mean_log_return(returns)
    print(mean_returns)

    mean_stds = std_log_return(returns)
    print(mean_stds)

    returns_skewness = skewness(returns)
    print(returns_skewness)

    returns_kurtosis = kurtosis(returns)
    print(returns_kurtosis)

if __name__ == "__main__":
    main()