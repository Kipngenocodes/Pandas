import  pandas as pd
import  numpy as np

'''
Unstacking reverses the stacking operation by moving the row index level back to the columns.
The Pandas DataFrame.unstack() method is used to pivot a level of the row index to become a column,
which is essentially useful for converting a long-format DataFrame into a wide format.'''

# Create a multiindex 
my_tuples = [["x", "x", "y", "y", "", "f", "z", "z"],["1", "2", "1", "2", "1", "2", "1", "2"]]
index = pd.MultiIndex.from_arrays(my_tuples, names=["first", "second"])
# Create a dataframe with the multiindex
df = pd.DataFrame(np.random.randint(0, 100, size=(8, 2)), index=index, columns=["A", "B"])

# Output of the dataframe before unstacking:
print("\n Dataframe before unstacking: \n", df)

# Unstacking the dataframe
df_unstacked = df.unstack(level=0)
# Output of the dataframe after unstacking:
print("\n Dataframe after unstacking: \n", df_unstacked)