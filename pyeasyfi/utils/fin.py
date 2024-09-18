import pandas as pd
import numpy as np

def compute_log_returns(asset_series : pd.Series | pd.DataFrame, used_periodicity : str ="24h", return_pandas=False) : 
    asset_series = asset_series.copy()
    # Extract asset value at the chose frequency : 
    frequency_based_asset = asset_series.resample(used_periodicity).last()
    log_prices = np.log(frequency_based_asset)
    # We compute the returns
    log_returns = np.diff(log_prices, axis=0)

    if return_pandas : 
        log_returns = pd.DataFrame(log_returns)
        log_returns.columns = list(asset_series.columns)

    return log_returns

def compute_returns(asset_series : pd.Series | pd.DataFrame, used_periodicity : str ="24h", return_pandas=False) : 
    asset_series = asset_series.copy()
    # Extract asset value at the chose frequency : 
    frequency_based_asset = asset_series.resample(used_periodicity).last()
    # We compute the returns
    returns = 100 * frequency_based_asset.pct_change().iloc[1:]
    if not return_pandas : 
        returns = returns.to_numpy()

    return returns