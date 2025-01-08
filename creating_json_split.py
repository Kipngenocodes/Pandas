import pandas as pd
from json import loads, dumps

# Create a DataFrame
df = pd.DataFrame(
   [["x", "y"], ["z", "w"]],
   index=["row_1", "row_2"],
   columns=["col_1", "col_2"],
)

# Convert DataFrame to JSON with 'split' orientation
result = df.to_json(orient="split")
parsed = loads(result)

# Display the JSON output
print("JSON Output (split orientation):")
print(dumps(parsed, indent=4))