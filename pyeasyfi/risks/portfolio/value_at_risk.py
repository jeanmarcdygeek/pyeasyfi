import pandas as pd
import numpy as np
import scipy

from pyeasyfi.risks.portfolio.volatility import compute_portfolio_historical_volatility

from pyeasyfi.constants.constants import PERIODIC_FACTORS

def compute_portfolio_VaR(assets_returns_df : pd.DataFrame, weights, confidence_level=0.95, generalization : str="annual"):
    ptf_volatility = compute_portfolio_historical_volatility(assets_returns_df, weights, generalization)
    mean_returns = np.mean(assets_returns_df)
    value_at_risk = mean_returns + ptf_volatility * scipy.stats.norm.ppf(1-confidence_level)
    return value_at_risk