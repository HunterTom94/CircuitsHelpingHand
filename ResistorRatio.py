from itertools import permutations
import numpy as np
import pandas as pd

bag_name_ls = ['1k_to_100k']
resistor_1k_to_100k = [47000, 18000, 6800, 68000, 15000, 82000, 33000, 1200, 1800, 22000, 10000, 39000, 12000, 56000,
                       1500, 27000, 2700, 2200, 4700, 3900, 3300, 5500, 1000, 8200]
resistors = np.asarray(resistor_1k_to_100k)
perm = permutations(resistors, 2)
first_ls = []
second_ls = []
first_bag = []
second_bag = []
ratio_ls = []
for combination in list(perm):
    first_bag_ls = [combination[0] in resistor_1k_to_100k]
    second_bag_ls = [combination[1] in resistor_1k_to_100k]
    first_ls.append(combination[0])
    second_ls.append(combination[1])
    ratio_ls.append(combination[1] / combination[0])

    first_bag.append(bag_name_ls[np.nonzero(first_bag_ls)[0][0]])
    second_bag.append(bag_name_ls[np.nonzero(second_bag_ls)[0][0]])

df = pd.DataFrame.from_dict(
    {'first': first_ls, 'second': second_ls, 'ratio': ratio_ls, 'first_bag': first_bag, 'second_bag': second_bag})
cols = df.columns.tolist()

cols = cols[0:2] + cols[3:5] + [cols[2]]
df = df[cols]

condition1 = df['ratio'] > 3.8
condition2 = df['ratio'] < 4.2
conditions = condition1 & condition2

print(df.loc[conditions].sort_values(by=['ratio']))
