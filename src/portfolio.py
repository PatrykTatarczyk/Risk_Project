import pandas as pd
import numpy as np
from scipy.optimize import minimize, Bounds, LinearConstraint

def portfolio_variance(w, cov_matrix):
    return w @ cov_matrix @ w

def optimization(returns):
    cov_matrix = returns.cov()
    length = len(returns.columns)
    w = np.linspace(0,1,length)
    bounds = tuple((0, 1) for _ in range(length))
    constraint = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
    res = minimize(fun=portfolio_variance,x0=w,args=(cov_matrix,),method="SLSQP",bounds=bounds,constraints=constraint)
    return pd.Series(res.x, index=returns.columns)

def optimized_returns(returns,weights):
    r =returns @ weights
    return  (1+r).prod() - 1