import pandas as pd
import numpy as np

def compute_portfolio_historical_variance(assets_df : pd.DataFrame, weights):
    weights = np.array(weights)
    weights_matrix = weights @ weights.T
    cov_matrix = np.cov(assets_df, rowvar=False)
    variance_matrix = np.diag([np.var(assets_df[x])  for x in assets_df.columns])
    volatility_matrix = weights_matrix * (cov_matrix + variance_matrix - np.eye(len(weights)))
    print(volatility_matrix)
    variance = np.sum(volatility_matrix)
    return variance