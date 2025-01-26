import pandas as pd
import numpy as np

'''
categorical data refers to a data type that represents categorical variables, 
similar to the concept of factors in R.
It is a specialized data type designed for handling categorical variables, commonly used in statistics.
A categorical variable can represent values like "male" or "female," or 
ratings on a scale such as "poor," "average," and "excellent." Unlike numerical data,
you cannot perform mathematical operations like addition or division on categorical data.
'''
# Create a categorical data with series
data = pd.Series(['apple', 'banana', 'cherry', 'date', 'elderberry'], dtype ='category')
                  
# Display the categorical Series 
print('Series with Categorical Data:\n', data)
