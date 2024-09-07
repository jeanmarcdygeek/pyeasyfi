from pyeasyfi.utils.Historical_data import HistoricalData
import pandas as pd
import pickle as pkl

def get_data_from_cb(cryptos_list : list,**kwargs):
    result_df = pd.DataFrame()
    for crypto in cryptos_list : 
        try : 
            data = HistoricalData(f'{crypto}-USD', **kwargs).retrieve_data()
            data['crypto'] = crypto
            result_df = pd.concat([result_df, data], sort=False)
        except : 
            pass
    return result_df