import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import quantstats as qs
import os
from scipy import stats

def drawdown_plot(returns, save_path="assets/underwater_plot.png"):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    qs.plots.drawdown(returns, savefig=save_path, show=False)

def kde_plot(returns, var, cvar, save_path="assets/kde_plot.png"):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.linspace(returns.min().min(), returns.max().max(), 200)
    for i in returns.columns:
        kde = stats.gaussian_kde(returns[i].dropna())
        y = kde(x)
        (line,) = ax.plot(x, y, label=i)
        color = line.get_color()
        ax.axvline(-abs(var[i]), color=color, linestyle="--", alpha=0.7)
        ax.axvline(-abs(cvar[i]), color=color, linestyle=":", alpha=0.7)
    ax.set_title("Density of Returns (VaR: -- | CVaR: :)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(save_path, dpi=300, bbox_inches="tight")
    return fig

def effective_frontier(results_df, save_path="assets/effective_frontier.png",risk_free_rate = 0.04198):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 6))

    scatter = ax.scatter(results_df['Volatility'], results_df['Return'], c=results_df['Sharpe'], cmap='viridis',
                         alpha=0.6, s=15)
    fig.colorbar(scatter, ax=ax, label="Sharpe Ratio")

    max_sharpe = results_df.loc[results_df['Sharpe'].idxmax()]
    min_vol = results_df.loc[results_df['Volatility'].idxmin()]

    ax.scatter(max_sharpe['Volatility'], max_sharpe['Return'], color='red', s=40, label='Max Sharpe', zorder=5)
    ax.scatter(min_vol['Volatility'], min_vol['Return'], color='blue', s=40, label='Min Volatility', zorder=5)

    bins = np.linspace(results_df['Return'].min(), results_df['Return'].max(), 50)
    frontier_vol = []
    frontier_ret = []

    for i in range(len(bins) - 1):
        binned = results_df[(results_df['Return'] >= bins[i]) & (results_df['Return'] < bins[i + 1])]
        if not binned.empty:
            min_row = binned.loc[binned['Volatility'].idxmin()]
            frontier_vol.append(min_row['Volatility'])
            frontier_ret.append(min_row['Return'])

    ax.plot(frontier_vol, frontier_ret, color='black', linestyle='--', linewidth=1.5, label='Efficient Frontier')

    ax.set_title("Efficient Frontier - Monte Carlo Simulation")
    ax.set_xlabel("Volatility")
    ax.set_ylabel("Return")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(save_path, dpi=300, bbox_inches="tight")

    return fig