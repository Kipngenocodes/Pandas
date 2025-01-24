import pandas as pd
import numpy as np



'''
Creating Dummy Variables with get_dummies()
The get_dummies() function in Pandas used 
to convert categorical variables of a Series or a DataFrame into dummy variables.'''
# Create a DataFrame with a categorical column
dataframe = pd.DataFrame({ 'Keys':list("aeiou"), 'Values':[1, 2, 3, 4, 5]})

# Display the dataframe 
print('\n Original Dataframe:', dataframe)

# Create dummy variables for the keys column
dummies = pd.get_dummies(dataframe["Keys"])
print('\n Resultant Dummy Variables:\n',dummies)