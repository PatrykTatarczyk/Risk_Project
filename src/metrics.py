import numpy as np
import pandas as pd
import datetime
from scipy.stats import skew
def mean_log_return(df):
    return df.groupby(df.index.year).mean()

def std_log_return(df):
    return df.groupby(df.index.year).mean()

def skewness(df):
    return df.skew(numeric_only=True)

def kurtosis(df):
    return df.kurtosis()

def sharpe_ratio(df,risk_free_rate = 0.04198, trading_days = 252):
    daily_rf = risk_free_rate / trading_days
    return (((df.mean()) - daily_rf) / df.std()) * np.sqrt(trading_days)

def sortino_ratio(df,risk_free_rate = 0.04198, trading_days = 252):
    daily_rf = risk_free_rate / trading_days

    diff = df - daily_rf
    diff = diff.clip(upper=0)
    diff = diff**2
    print(diff)
    dd = np.sqrt(diff.sum()/len(diff))
    return (((df.mean()) - daily_rf) / dd) * np.sqrt(trading_days)