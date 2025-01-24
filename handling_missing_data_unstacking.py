import pandas as pd
import numpy as np

# Create a MultiIndex for rows
index = pd.MultiIndex.from_product(
    [["bar", "baz", "foo", "qux"], ["one", "two"]],
    names=["first", "second"]
)

# Create a MultiIndex for columns
columns = pd.MultiIndex.from_tuples(
    [("A", "cat"), ("B", "dog"), ("B", "cat"), ("A", "dog")],
    names=["exp", "animal"]
)

# Create the DataFrame
df = pd.DataFrame(
    np.random.randint(0, 100, size=(8, 4)),  
    index=index,
    columns=columns
)

# Select specific rows and columns using iloc
df3 = df.iloc[[0, 2, 3, 1], [3, 1]]  

# Output the DataFrame
print("\nBefore unstacking:\n", df3)


# Unstack the DataFame
unstacked = df3.unstack()

# Display the Unstacked DataFrame
print("\n Unstacked DataFrame without Filling:\n",unstacked)

unstacked_filled = df3.unstack(fill_value=1)
print("\n Unstacked DataFrame with Filling:\n",unstacked_filled)