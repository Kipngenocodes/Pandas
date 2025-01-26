import pandas as pd
import numpy as np
import sklearn



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

# Creating dummies with prefixes
new_dummies = pd.get_dummies(dataframe["Keys"], prefix='key_')
print('\n Resultant Dummy Variables with Prefix:\n',new_dummies)

'''Handling Collinearity While Creating Dummy Variables
To avoid collinearity issues in statistical models,
you can drop the first dummy variable by setting the drop_first parameter to True.'''
# Create dummy variables for the keys column with drop_first=True
dummies = pd.get_dummies(dataframe["keys"], drop_first=True)

print('Resultant Dummy Variables with Prefix:\n',dummies)