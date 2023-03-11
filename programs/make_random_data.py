## make random data
import numpy as np
import pandas as pd

start = '2023-02-27 00:00:00'
end = '2023-03-05 23:59:59'
codes = ['1AD010', '1AD020', '1BB040', '1BB050', '2AA010', '2AC045', '2DB100', '3CA020', '3HD100']

date_range = pd.date_range(start=start, end=end, freq='S')
random_dates = np.random.choice(date_range, size=100)
random_numbers = np.random.uniform(low=0.0, high=1.0, size=100)
random_numbers = np.round(random_numbers, 4)
random_codes = np.random.choice(codes, size=100)
random_bools = np.random.choice([True, False], size=100)

data = {'ID':random_codes,
        'time':random_dates,
        'TF':random_bools,
        'value':random_numbers}

df = pd.DataFrame(data)
df.to_csv('sample_data.csv', index=False)