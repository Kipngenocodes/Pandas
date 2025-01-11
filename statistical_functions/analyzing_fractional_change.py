import pandas as pd
import numpy as np

'''
The pct_change() function in Pandas calculates the fractional 
change between the current and a prior element. 
It is a valuable tool for understanding how data evolves over time,
commonly used in financial data analysis.
'''

# creating a series a with 10 random values
a_series = pd.Series(np.random.randint(1, 100, 10))
print(a_series.pct_change())

df = pd.DataFrame(np.random.randn(5, 2))
print(df.pct_change())

# applying pct_change() to a DataFrame with a specified axis
print(df.pct_change(axis=1))
