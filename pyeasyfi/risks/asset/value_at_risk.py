import numpy as np
import scipy

from pyeasyfi.utils.simulation_kernels.random_walk import RandomWalkSimulation

def compute_historical_VaR(returns, confidence_level=0.95):
    value_at_risk = np.percentile(returns, (1-confidence_level) * 100)
    return value_at_risk

def compute_var_covar_VaR(returns, confidence_level=0.95):
    dist_mean = np.mean(returns)
    dist_std = np.std(returns)
    #value_at_risk = scipy.stats.norm.ppf(1-confidence_level, loc=dist_mean, scale=dist_std)
    value_at_risk = dist_mean + dist_std * scipy.stats.norm.ppf(1-confidence_level)
    return value_at_risk

def compute_montecarlo_VaR(returns, start_price, n_simulations=1000, horizon=365, confidence_level=0.95):
    simulator  = RandomWalkSimulation(returns, start_price)
    sim_results = simulator.run(n_simulations, horizon=horizon, return_df=False)
    sim_returns = 100 * (sim_results[-1,:] - sim_results[0, :])/sim_results[0,:] 
    value_at_risk = np.percentile(sim_returns, (1-confidence_level) * 100)# * start_price # Should we mult by start price?
    return value_at_risk