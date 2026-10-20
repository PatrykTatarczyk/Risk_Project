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
