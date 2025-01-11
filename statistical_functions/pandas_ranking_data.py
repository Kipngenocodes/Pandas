import pandas as pd
import numpy as np


s = pd.Series(np.random.randn(5), index=list('abcde'))
s['d'] = s['b'] # so there's a tie
print(s.rank())