from src.data_loader import fetch_price_data
from src.returns import log_returns,simple_returns
from src.metrics import mean_log_return, std_log_return,skewness,kurtosis,sharpe_ratio,sortino_ratio,MDD,value_at_risk_historical,value_at_risk_parametrical,expected_shortfall
from src.visualization import drawdown_plot,kde_plot
from src.portfolio import optimization,optimized_returns
import matplotlib.pyplot as plt
import numpy as np
plt.ioff()

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

    print("---Maximum Drawdown---")
    maxdrawdown = MDD(prices)
    print(maxdrawdown)

    drawdown_plt = drawdown_plot(prices)

    print("---Value at Risk Historical---")
    historical_var = value_at_risk_historical(returns)
    print(historical_var)

    print("---Value at Risk Parametric---")
    parametric_var = value_at_risk_parametrical(returns)
    print(parametric_var)

    print("---Expected Shortfall--")
    es = expected_shortfall(returns,historical_var)
    print(es)

    kde = kde_plot(returns,parametric_var,es)

    print("---Optimized Portfolio Weights---")
    optimized = optimization(simple_ret)
    print(optimized)

    print("---Optimized Portfolio Returns---")
    optimized_return = optimized_returns(simple_ret,optimized)
    print(f"optimized_return: {round(optimized_return,2)*100}%")
    print(f"non_optimized_return: {round(optimized_returns(simple_ret,np.ones(5)/5) )* 100}%")

if __name__ == "__main__":
    main()