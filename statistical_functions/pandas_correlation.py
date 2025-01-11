import pandas as pd
import numpy as np

'''
Correlation shows the linear relationship between any two array of values (series).
Pandas corr() function supports different correlation methods,
including Pearson (default), Spearman, and Kendall.'''

# Create a DataFrame with two columns
data_frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])

print(data_frame['a'].corr(data_frame['b']))
print(data_frame.corr())
