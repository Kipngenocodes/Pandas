import pandas as pd

if pd.Series([False, True, False]).any():
   print("I am any")