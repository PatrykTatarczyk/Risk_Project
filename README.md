# Market Risk Analysis

A modular Python project for quantitative risk analysis, tail-risk modeling, and portfolio optimization using real market data (`yfinance`).

## What it does

- **Returns & Basic Risk**: Fetches historical data, computes simple/log returns, volatility, Sharpe Ratio, Sortino Ratio, and Maximum Drawdown.
- **Tail Risk**: Calculates Value at Risk (VaR) and Expected Shortfall (CVaR) using Historical and Parametric methods.
- **Portfolio Optimization**: Finds the Global Minimum Variance (GMV) portfolio and runs Monte Carlo simulations to plot the Efficient Frontier.

## Quick Start

```bash
# Clone and setup
git clone https://github.com/PatrykTatarczyk/Risk_Project.git
cd Risk_Project

# Activate venv & install
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run
python main.py