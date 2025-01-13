import pandas as pd
import numpy as np

''''
Pandas provides a API to customize various aspects of its behavior, 
particularly related to display settings. 
This customization is essential for adjusting how data is presented based on your needs.
How many rows and columns are displayed or change the precision of floating-point numbers, 
Pandas provides a flexible and powerful API for these customization's

The primary functions available for these customization's are −
        get_option()
        set_option()
        reset_option()
        describe_option()
        option_context()
'''

'''
Frequently used Parameters
1	display.max_rows: Maximum number of rows to display.
2 display.max_columns: Maximum number of columns to display.
3	display.expand_frame_repr: Whether to expand the display of DataFrames across multiple lines.
4	display.max_colwidth : Maximum width of columns.
5	display.precision : Precision to display for decimal numbers.'''

# getting current options
print(pd.get_option('display.max_rows'))

# checking the maximum number of columns being displayed
print(pd.get_option('display.max_columns'))

# Setting new options
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 5)

print(pd.get_option('display.max_rows'))
print(pd.get_option('display.max_columns'))

# Resetting the options to their default values
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')

print(pd.get_option("display.max_rows"))
print(pd.get_option("display.max_column"))

# Describing Maximum Rows Displayed
pd.describe_option("display.max_rows")

# Temporarily Changing Maximum Rows Displayed
with pd.option_context("display.max_rows",10):
   print(pd.get_option("display.max_rows"))
print(pd.get_option("display.max_rows"))