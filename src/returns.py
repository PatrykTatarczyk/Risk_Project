import pandas as pd
import numpy as np


def log_returns(df):
    returns = np.log(df.shift(1)/df)
    return returns
def simple_returns(df):
    simple = df.pct_change()
    return simple



