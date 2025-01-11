import pandas as pd

# Sorting by actual values - series values
df = pd.Series([1, 20, 3, 41, 5])

print('unsorted  Pandas series: \n', df)

panda_series_sorted = df.sort_values(ascending=True)
print("\nSorted Pandas Series: \n", panda_series_sorted)