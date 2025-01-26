import pandas as pd
import numpy as np

'''
The pandas.from_dummies() function is 
used to convert the output of get_dummies() back into a categorical Series.
'''
# Create a DataFrame with dummy variables
df = pd.DataFrame({"Col_a": [0, 1, 0, 1, 1, 1, 1, 1, 1], "Col_b": [1, 0, 1, 0, 0, 0, 0, 0 , 0]})

#Display the Input DataFrame
print('Input DataFrame:\n',df)

# Convert the Dummies back to categorical
original_series = pd.from_dummies(df, sep="_")

print('Resultant Categorical Variables:\n',original_series )