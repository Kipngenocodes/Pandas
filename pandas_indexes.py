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