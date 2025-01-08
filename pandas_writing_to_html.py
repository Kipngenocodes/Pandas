import pandas as pd

# Create a DataFrame
df = pd.DataFrame([[1, 2], [3, 4]], columns=["A", "B"])

# Convert the DataFrame to HTML table
html = df.to_html()

# Display the HTML string
print(html)