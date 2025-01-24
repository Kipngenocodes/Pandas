import pandas as pd

''''
Pivoting in Python Pandas is a powerful data transformation
technique that reshapes data for easier analysis and visualization.
It change the data representation from a "long" format to a "wide" format,
making it simpler to perform aggregations and comparisons.'''

# Creating a Dataframe
df = pd.DataFrame({"Col1": range(12),"Col2": ["A", "A", "A", "B", "B","B", "C", "C", "C", "D", "D", "D"],
"date": pd.to_datetime(["2024-01-03", "2024-01-04", "2024-01-05"] * 4)})

# output the  following dataframe:
print('\n Original DataFrame:\n', df)

# Pivoting the Dataframe
pivoted_df =  df.pivot(index="date", columns="Col2", values="Col1")

# Display the output
print('\nPivoted DataFrame:\n', pivoted_df)