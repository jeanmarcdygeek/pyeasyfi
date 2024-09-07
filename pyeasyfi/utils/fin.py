import pandas as pd
import numpy as np

def compute_log_returns(asset_series : pd.Series, used_periodicity : str ="24h") : 
    asset_series = asset_series.copy()
    # Extract asset value at the chose frequency : 
    frequency_based_asset = asset_series.resample(used_periodicity).last()
    log_prices = np.log(frequency_based_asset)
    # We compute the returns
    log_returns = np.diff(log_prices)

    return log_returns

def compute_returns(asset_series : pd.Series, used_periodicity : str ="24h") : 
    asset_series = asset_series.copy()
    # Extract asset value at the chose frequency : 
    frequency_based_asset = asset_series.resample(used_periodicity).last()
    # We compute the returns
    returns = 100 * frequency_based_asset.pct_change()

    return returns.to_numpy()[1:]