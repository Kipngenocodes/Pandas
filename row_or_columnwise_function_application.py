import pandas as pd
import numpy as np

'''
The apply() function is versatile and allows you to apply a function along the axes of a DataFrame.
By default, it applies the function column-wise, 
but you can specify row-wise application using the axis parameter.'''

# create a dataframe with five column and five rows
df = pd.DataFrame(np.random.randint(0,100,size=(5, 5)), columns=list
                  ('ABCDE'))
print('\n Original DataFrame:\n', df)

result = df.apply(np.mean)
print('\n Result on column-wise:\n',result)


# Applying a Function Row-wise
result = df.apply(np.mean, axis=1)
print('\nResult on row-wise :\n',result)