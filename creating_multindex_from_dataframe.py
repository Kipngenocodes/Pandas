import pandas as pd
import numpy as np

# create a datafame with 5 rows and 3 columns
df = pd.DataFrame(np.random.randint(0,100,size=(5, 3)), columns=list ('ABC'))
print(df)