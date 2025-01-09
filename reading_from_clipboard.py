import pandas as pd

# Read clipboard content into a DataFrame when using a tabular form
df = pd.read_clipboard()
print(df)

# Read clipboard content into a DataFrame when it is non tabular
df = pd.read_clipboard(sep=',',header=None)
print(df)