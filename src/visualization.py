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



