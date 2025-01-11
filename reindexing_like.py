import pandas as pd
import numpy as np

# creating a dataframe
df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])

# Reindexing df2 like df1
df2 = df2.reindex_like(df1)

# outputing the dataframe  after reindexing
print(df2)