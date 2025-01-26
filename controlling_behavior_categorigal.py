import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype

# creating a dataframe 
df = pd.DataFrame({ 'A' : list ('abcde'), 'B' : list ('bccde'), 'C' : list ('aebcd')})

# output the dataframe and it data type
print("\n Original DataFrame: \n", df)
print('\n Data Type of DataFrame: \n', df.dtypes)


# Applying CategoricalDtype to a DataFrame
cat_type = CategoricalDtype(categories=list("abcde"), ordered=True)
df_cat = df.astype(cat_type)

# Display the Input DataFrame
print('\n Converted DataFrame:\n', df_cat)
print('\n Verify the Data type of each column:\n', df_cat.dtypes) 
