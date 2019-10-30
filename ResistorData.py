import numpy as np
import pandas as pd

resistor_df = pd.DataFrame(columns=['bag_name', 'resistor_value'])

def add_bag(df, bag_name, resistor_value_ls, min, max):
    bag_name_ls = [bag_name] * len(resistor_value_ls)
    assert np.min(resistor_value_ls) >= min, "Min too low"
    assert np.max(resistor_value_ls) <= max, "Max too high"
    df = df.append(pd.DataFrame({'bag_name': bag_name_ls, 'resistor_value': resistor_value_ls}), ignore_index=True)

    return df


resistor_1k_to_100k = [47000, 18000, 6800, 68000, 15000, 82000, 33000, 1200, 1800, 22000, 10000, 39000, 12000, 56000,
                       1500, 27000, 2700, 2200, 4700, 3900, 3300, 5500, 1000, 8200]
resistor_df = add_bag(resistor_df, '1k_to_100k', resistor_1k_to_100k, min=1000, max=100000)

resistor_100_to_1k = [330, 120, 220, 560, 180, 100, 820, 150, 470, 390, 270, 680]
resistor_df = add_bag(resistor_df, '100_to_1k', resistor_100_to_1k, min=100, max=1000)

resistor_10_to_100 = [12, 82, 39, 33, 10, 68, 56, 15, 27, 18, 22]
resistor_df = add_bag(resistor_df, '10_to_100', resistor_10_to_100, min=10, max=100)

resistor_df.to_pickle('C:\\Users\\hunte\\OneDrive\\Lab\\Misc\\resistor_df.pkl')
print(resistor_df)
