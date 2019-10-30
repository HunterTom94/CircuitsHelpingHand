from itertools import permutations, combinations
import numpy as np
import pandas as pd

resistor_df = pd.read_pickle('C:\\Users\\hunte\\OneDrive\\Lab\\Misc\\resistor_df.pkl')

target = 3255
number_of_resistor = 2

value_ls = list(resistor_df['resistor_value'].to_numpy())*number_of_resistor

combos = list(combinations(value_ls, number_of_resistor))

sum_ls = np.array([np.sum(pair) for pair in combos])
optimal_pair = combos[np.argsort(np.abs(sum_ls - target))[0]]

print('Target: {}'.format(target))
print('Get: {}'.format(np.sum(optimal_pair)))
print(resistor_df[resistor_df['resistor_value'] == optimal_pair[0]])
print(resistor_df[resistor_df['resistor_value'] == optimal_pair[1]])
