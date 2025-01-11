import pandas as pd
import numpy as np

'''
Sorting is a fundamental operation when working with data in Pandas,
whether you're organizing rows, columns, or specific values. Sorting can
help you to arrange your data in a meaningful way for better understanding and easy analysis.
    Sorting by Label − This involves sorting the data based on the index labels.
    Sorting by Value − This involves sorting data based on the actual values in the DataFrame or Series.
'''
# Sorting DataFrames by labels - To sort by the index labels,
# you can use the sort_index() method, by passing the axis arguments and the order of sorting, 
# data structure object can be sorted.

unsorted_pd =pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])

# output
print('Output of unsorted data')
print(unsorted_pd)
# sorting the data by index labels
sorted_pd = unsorted_pd.sort_index()
# output
print('Output of sorted data \n', sorted_pd
      )


# Controlling the order of sorting - By default, sort_index() sorts in ascending order.
sorted_df = unsorted_pd.sort_index(ascending=False)
print("\nOutput Sorted DataFrame:\n", sorted_df)