import pandas as pd
import numpy as np

# create a datafame with 5 rows and 3 columns
df = pd.DataFrame(np.random.randint(0,100,size=(4, 3)), columns=list ('ABC'))
print(df)

print('\n')
# create a multiindex object 
multi_index = pd.MultiIndex.from_frame(df[['A', 'B']])

# Create a new MultiIndexed DataFrame
multi_df = pd.DataFrame(np.random.randn(4, 3), index=multi_index, columns=["A", "B", "C"])

# Display the output MultiIndexed DataFrame
print("Output MultiIndexed DataFrame:\n", multi_df)