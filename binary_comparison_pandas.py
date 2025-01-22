import  pandas as  pd
import  numpy as np

# Create a dataframe 
data = { 'Age': [20, 21, 19, 18],
        'Score': [90, 85, 88, 92] }
df = pd.DataFrame(data)

# Creating a binary comparison in the dataframe
# Perform binary comparison operations
print("\nLess than 5:\n", df < 50)
print("\nGreater than 5:\n", df > 50)
print("\nLess than or equal to 5:\n", df <= 50)
print("\nGreater than or equal to 5:\n", df >= 50)
print("\nEqual to 5:\n", df == 50)
print("\nNot equal to 5:\n", df != 50)