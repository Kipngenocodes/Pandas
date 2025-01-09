import pandas as pd

# Read clipboard content into a DataFrame when using a tabular form
df = pd.read_clipboard()
print(df)