import pandas as pd
import numpy as np
 
unsorted_df = pd.DataFrame(np.random.randn(6,4),index=[1,4,2,3,5,0],
                           columns = ['col2','col1', 'col4', 'col3'])

print("Original DataFrame:\n", unsorted_df)

# sorting the dataframe columns
sorted_df = unsorted_df.sort_index(axis=1, ascending=True)
print("\nSorted DataFrame:\n", sorted_df)