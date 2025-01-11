import pandas as pd
import numpy as np

'''
The reindex() method provides an optional parameter method for filling missing values.
The available methods include −
    pad/ffill: Fill values forward.
    bfill/backfill: Fill values backward.
    nearest: Fill from the nearest index values.
'''

df1 = pd.DataFrame(np.random.randn(6, 3), columns=['col1', 'col2', 'col3'])
df2 = pd.DataFrame(np.random.randn(2, 3), columns=['col1', 'col2', 'col3'])

# # Padding NaNs
print(df2.reindex_like(df1))
print('\n')

# Now fill the NaNs with preceding values
print("Data Frame with Forward Fill:")
print(df2.reindex_like(df1, method='ffill'))
print('\n')
#  Now fill the NaNs with preceding values
print("Data Frame with Forward Fill limiting to 1:")
print(df2.reindex_like(df1, method='ffill', limit=1))