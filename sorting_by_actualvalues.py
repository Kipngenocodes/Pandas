import pandas as pd

# Sorting by actual values - series values
df = pd.Series([1, 20, 3, 41, 5])

print('unsorted  Pandas series: \n', df)

panda_series_sorted = df.sort_values(ascending=True)
print("\nSorted Pandas Series: \n", panda_series_sorted)


unsorted_df = pd.DataFrame({'col1':[2,9,5,0],'col2':[1,3,2,4]})
print("Original DataFrame:\n", unsorted_df)

# Sort the DataFrame by values
sorted_df = unsorted_df.sort_values(by='col1')
print("\nOutput Sorted DataFrame:\n", sorted_df)