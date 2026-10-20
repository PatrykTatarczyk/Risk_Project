import pandas as pd
import numpy as np


def log_returns(df):
    returns = pd.DataFrame()
    for i in df.columns:
        kolumna = np.log(df[i].shift(-1)/df[i])
        returns[f"{i} Log Returns"] = kolumna
    return returns




