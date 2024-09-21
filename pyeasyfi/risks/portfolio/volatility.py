import pandas as pd
import numpy as np
import math

from pyeasyfi.constants.constants import PERIODIC_FACTORS


def compute_portfolio_historical_volatility(assets_returns_df : pd.DataFrame, weights, generalization : str="annual"):
    weights = np.array(weights)
    weights_matrix = weights @ weights.T
    cov_matrix = np.cov(assets_returns_df, rowvar=False)
    volatility_matrix = weights_matrix * cov_matrix
    variance = np.sum(volatility_matrix)
    volatility = math.sqrt(variance * PERIODIC_FACTORS[generalization])
    return volatility
