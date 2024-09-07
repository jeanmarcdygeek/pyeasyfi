import numpy as np
import pandas as pd
import math

class RandomWalkSimulation : 
    def __init__(self, returns : np.ndarray, last_known_price: float) -> None:
        variance = np.var(returns, ddof=0)
        self.std_p = math.sqrt(variance)
        self.drift = np.mean(returns) - variance/2
        self.mean  = np.mean(returns)
        self.starting_price = last_known_price
        pass

    def run(self, n_simulations=100, horizon=365, return_df=True) : #only log returns
        simulated_results = self.starting_price * np.exp(np.cumsum(self.drift + self.std_p * np.random.randn(horizon, n_simulations), axis=0))
        #random_factors = np.exp(self.drift + self.std_p * np.random.randn(horizon, n_simulations))
        #random_factors[0, :] = self.starting_price * random_factors[0, :]
        #simulated_results = np.cumprod(random_factors, axis=0)
        if return_df : 
            return pd.DataFrame(simulated_results, columns=[f"sim_{i}" for i in range(1,n_simulations + 1)])
        return simulated_results