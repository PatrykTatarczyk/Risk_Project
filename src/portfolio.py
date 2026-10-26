import pandas as pd
import numpy as np
from scipy.optimize import minimize, Bounds, LinearConstraint
from src.metrics import sharpe_ratio

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


def monte_carlo_simulation(returns,risk_free_rate = 0.04198):
    mean_returns = returns.mean()
    std_returns = returns.std()
    cov_matrix = returns.cov()
    results = []
    for i in range(1,5000):
        rng = np.random.uniform(size=len(returns.columns))
        weigths = rng/rng.sum()
        ex_return = weigths @ mean_returns
        ex_std = np.sqrt(weigths @ cov_matrix @ weigths)
        results.append({"Return":ex_return,"Volatility": ex_std,"Sharpe":(ex_return - risk_free_rate)/ex_std})
    results_df = pd.DataFrame(results)
    return results_df



