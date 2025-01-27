import pandas as pd
import numpy as np

# Create DataFrame 
df = pd.DataFrame({'one':[10,20,30,40,50,2000], 'two':[1000,0,30,40,50,60]})

# Replace the generic values
print(df.replace({1000:10,2000:60}))