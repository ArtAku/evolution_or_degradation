import pandas as pd
import numpy as np


def tupled_agressivity_table():
    min_agressivity, max_agressivity = 0, 100
    min_twin_gain, max_twin_gain = 0.0, 0.5

    gain_step = (max_twin_gain - min_twin_gain) / (max_agressivity - min_agressivity)
    agressivity_df = pd.DataFrame()

    cur_twin_gain = max_twin_gain
    for i in range(min_agressivity, max_agressivity + 1):

        row = []
        cur_gain = cur_twin_gain
        for j in range(0, i):
            row.append(cur_gain)
            cur_gain += gain_step

        row.append(cur_twin_gain)
        cur_twin_gain -= gain_step

        cur_gain = max_twin_gain + gain_step
        for j in range(i + 1, max_agressivity + 1):
            row.append(cur_gain)
            cur_gain += gain_step
        agressivity_df[str(i)] = row
    agressivity_df.to_csv('agressivity_df.csv', index=False)

if __name__ == '__main__':
    tupled_agressivity_table()