''' 
The Index class is a basic object for storing all index types in Pandas objects. 
It provides the basic functionality for accessing and manipulating data.
        Feature of Index class
        - Immutable
        - Sliceable
        -alignment
        
syntax for class Index:
class pandas.Index(data=None, dtype=None, copy=False, name=None, tupleize_cols=True, **kwargs)

Types of Indexes in Pandas
1. Numeric Index: 
2. Categorical Index:
3. Datetime Index:
4. Period Index:
5. MultiIndex:
6. Interval Index:
7. TimedeltaIndex:
'''

'''
Numeric Index  is the basic index type in Pandas,
it contains numerical values. NumericIndex is a default index and 
Pandas automatically assigns this if you did not provided any index.
'''
# Demonstration of howdemonstrates 
# how pandas automatically assigns NumericIndex to a pandas DataFrame object.
import pandas as pd

# Generate some data for DataFrame
data = {
   'Name': ['Steve', 'Lia', 'Vin', 'Katie'],
   'Age': [32, 28, 45, 38],
   'Gender': ['Male', 'Female', 'Male', 'Female'],
   'Rating': [3.45, 4.6, 3.9, 2.78]
}
# Creating the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

print("\nDataFrame Index Object Type:",df.index.dtype)


'''
Categorical Index
The CategoricalIndex is used to deal the duplicate labels. 
This index is efficient in terms of memory usage and handling the large number of duplicate elements.
'''
# Demonstration of  how to create a CategoricalIndex in Pandas
import pandas as pd
# creating a CategoricalIndex
categotical_index = pd.CategoricalIndex(['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'])
df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                   'B': ['Kericho', 'Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret', 'Kisii', 'Kakamega', 'Kisumu']},
                  index=categotical_index)

print('Input DataFrame:\n',df)
print("\nDataFrame Index Object Type:",df.index.dtype)


''' 
        Interval  index
IntervalIndex is used to represent the intervals in the data.
It is used to represent the ranges of values in the data.
An IntervalIndex is used to represent intervals (ranges) in your data.
This type of index will be created using the interval_range() method.

'''
# Following example creates a DataFrame with IntervalIndex using the interval_range() method.


import pandas as pd
# Creating a DataFrame with IntervalIndex
interval_index = pd.interval_range(start=0, end=10)
# create a DataFrame with IntervalIndex
data = {'A': ['Kipngeno', 'Chepkwony', 'Danny', 'Manning', 'David', 'Popal', 'FameOne', 'Chana', 'Giga', 'Kiprotich'],
        'age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70], 
        'Occupation': ['Engineer', 'Doctor', 'Teacher', 'Lawyer', 'Nurse', 'Pilot', 'Farmer', 'Driver', 'Carpenter', 'Plumber'],
        'region': ['Nairobi', 'Kisumu', 'Mombasa', 'Nakuru', 'Eldoret', 'Kisii', 'Kakamega', 'Kericho', 'Nyeri', 'Nanyuki']}

df = pd.DataFrame(data, index=interval_index)
print('Input DataFrame:\n',df)
print("\nDataFrame Index Object Type:",df.index.dtype)

'''
MultiIndex
Pandas MultiIndex is used to represent multiple levels or layers in index of Pandas data structures,
which is also called as hierarchical.
'''
import pandas as pd
# creating a MultiIndex
arr = [['A', 'A', 'A', 'B', 'B', 'B'],
         [1, 2, 3, 1, 2, 3], ['red', 'green', 'blue', 'red', 'green', 'blue']]
multi_index = pd.MultiIndex.from_arrays(arr, names=('Letter', 'Number',  'Color'))
# create a DataFrame with MultiIndex
data = {'A': ['Kipngeno', 'Chepkwony', 'Danny', 'Manning', 'David', 'Popal'],
        'age': [25, 30, 35, 40, 45,50]
        , 'Occupation': ['Engineer', 'Doctor', 'Teacher', 'Law', 'Nurse', 'Pilot'],
        'region': ['Nairobi', 'Kisumu', 'Mombasa', 'Nakuru', 'Eldoret', 'Kisii']}
df = pd.DataFrame(data, index=multi_index)
print('Input DataFrame:\n',df)
print("\nDataFrame Index Object Type:",df.index.dtype)

'''
                DatetimeIndex
Pandas DatetimeIndex object is used to represent the date and time values. 
Nothing but it used for time-series data where each row is linked to a specific timestamp.
'''
# Following example creates a DataFrame with DatetimeIndex using the date_range() method.
import pandas as pd
# Creating a DataFrame with DatetimeIndex
datetime_idx = pd.date_range('2022-01-01 12:00:00', periods=10)
# create a DataFrame with DatetimeIndex
data = {'First Name': ['Kipngeno', 'Chepkwony', 'Danny', 'Manning', 'David', 'Popal', 'FameOne', 'Chana', 'Giga', 'Kiprotich'],
        'age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70], 
        'Occupation': ['Engineer', 'Doctor', 'Teacher', 'Lawyer', 'Nurse', 'Pilot', 'Farmer', 'Driver', 'Carpenter', 'Plumber'],
        'region': ['Nairobi', 'Kisumu', 'Mombasa', 'Nakuru', 'Eldoret', 'Kisii', 'Kakamega', 'Kericho', 'Nyeri', 'Nanyuki'],
        'Flight type': ['Domestic', 'International', 'Domestic', 'International', 'Domestic', 'International', 'Domestic', 'International', 'Domestic', 'International']}
df = pd.DataFrame(data, index=datetime_idx)
print('Input DataFrame:\n',df)
print("\nDataFrame Index Object Type:",df.index.dtype)

'''
TimeDeltaIndex  is used to represent the time intervals or durations in the data.
It is used to represent the differences between two dates or times.
'''
# Following example creates a DataFrame with TimedeltaIndex using the timedelta_range() method.
import pandas as pd
# Creating a DataFrame with TimedeltaIndex
timedelta_idx = pd.timedelta_range(start='1 days', periods=10)
# create a DataFrame with TimedeltaIndex
data = {'State': ['Washington', 'California', 'Texas', 'Florida', 'New York', 'Illinois', 'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina'],
        'Capital': ['Olympia', 'Sacramento', 'Austin', 'Tallahassee', 'Albany', 'Springfield', 'Harrisburg', 'Columbus', 'Atlanta', 'Raleigh'],
        'Population': [7.6, 39.5, 29.5, 21.5, 19.8, 12.8, 12.8, 11.7, 10.7, 10.4]}  

df = pd.DataFrame(data, index=timedelta_idx)
print('Input DataFrame:\n',df)
print("\nDataFrame Index Object Type:",df.index.dtype)

'''
PeriodIndex: Pandas PeriodIndex is used to represent regular periods in time, like quarters, months, or years.
Example
This example creates a Pandas DataFrame with PeriodIndex object.'''

import pandas as pd
# Creating a DataFrame with PeriodIndex
period_idx = pd.period_range(start='2022-01', periods=10, freq='M')
# create a DataFrame with PeriodIndex
data = {'State': ['Washington', 'California', 'Texas', 'Florida', 'New York', 'Illinois', 'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina'],
        'Capital': ['Olympia', 'Sacramento', 'Austin', 'Tallahassee', 'Albany', 'Springfield', 'Harrisburg', 'Columbus', 'Atlanta', 'Raleigh'],
        'Population': [7.6, 39.5, 29.5, 21.5, 19.8, 12.8, 12.8, 11.7, 10.7, 10.4],
        'Region': ['West', 'West', 'South', 'South', 'Northeast', 'Midwest', 'Northeast', 'Midwest', 'South', 'South']}
df = pd.DataFrame(data, index=period_idx)
print('Input DataFrame:\n',df)
print("\nDataFrame Index Object Type:",df.index.dtype)
