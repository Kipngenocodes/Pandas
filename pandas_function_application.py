import pandas as pd
import numpy as np

# Table-wise Function Application
'''
The pipe() function allows you to apply chainable 
functions that expect a DataFrame or Series as input.
This method is useful for performing custom operations
on the entire DataFrame in a clean and readable manner.
'''


def adder(dataframe, column_name):
    # Add 10 to all values in the specified column
    dataframe[column_name] += 10
    return dataframe

def multiplier(dataframe, column_name):
    # Multiply all values in the specified column by 2
    dataframe[column_name] *= 20
    return dataframe


# create a dataframe 
df = pd.DataFrame({'A': [1, 2, 3], 'B': [6, 8, 10],
                   'C': [12, 14, 16], 'D': [18, 20, 22]})


# output the original dataframe and series
print("Original DataFrame:\n", df)

df.pipe(adder, column_name ='A')
print("\n DataFrame after applying adder function:\n", df)

df.pipe(multiplier, column_name ='B')
print("\n DataFrame after applying Multiplier function:\n", df)