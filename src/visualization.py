import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import quantstats as qs
import os

def drawdown_plot(returns, save_path="assets/underwater_plot.png"):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    qs.plots.drawdown(returns, savefig=save_path, show=False)


