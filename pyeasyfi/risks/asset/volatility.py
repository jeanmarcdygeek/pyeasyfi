import pandas as pd
import numpy as np
import math
from arch import arch_model

from pyeasyfi.constants.constants import PERIODIC_FACTORS

def compute_historical_volatility(returns : np.ndarray, generalization : str="annual") : 
    # We compute and generalize the volatility
    volatility = np.std(returns) * math.sqrt(PERIODIC_FACTORS[generalization])
    return volatility


def compute_GARCH_volatility(returns, generalization : str="annual"): # https://vlab.stern.nyu.edu/docs/volatility/GARCH
    am = arch_model(returns, vol="Garch", p=1, o=0, q=1, dist="Normal")
    res = am.fit(update_freq=0)
    volatility = res.conditional_volatility[-1] * math.sqrt(PERIODIC_FACTORS[generalization])
    return volatility, res
