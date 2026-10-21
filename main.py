from src.data_loader import fetch_price_data
from src.returns import log_returns,simple_returns
from src.metrics import mean_log_return, std_log_return,skewness,kurtosis,sharpe_ratio,sortino_ratio


def main():
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA']
    start_date = '2023-01-01'
    end_date = '2026-01-01'

    prices = fetch_price_data(tickers, start_date, end_date)
    print(prices.head())

    print("---Log Returns---")
    returns = log_returns(prices)
    print(returns.head())

    print("---Simple Returns---")
    simple_ret = simple_returns(prices)
    print(simple_ret.head())

    print("---Mean Log Returns---")
    mean_returns = mean_log_return(returns)
    print(mean_returns)

    print("---Std Log Returns---")
    mean_stds = std_log_return(returns)
    print(mean_stds)

    print("---Skewness---")
    returns_skewness = skewness(returns)
    print(returns_skewness)

    print("---Kurtosis---")
    returns_kurtosis = kurtosis(returns)
    print(returns_kurtosis)

    print("---Sharpe_ratio---")
    sharpe = sharpe_ratio(simple_ret)
    print(sharpe)

    print("---Sortino_ratio---")
    sortino = sortino_ratio(simple_ret)
    print(sortino)

if __name__ == "__main__":
    main()