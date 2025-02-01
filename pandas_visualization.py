import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a DataFrame with random data
df = pd.DataFrame(
    np.random.randn(10, 4),  # 10 rows, 4 columns of random numbers
    index=pd.date_range('1/1/2000', periods=10),  # Date index
    columns=list('ABCD')  # Column names
)

# Print the DataFrame
print("DataFrame:")
print(df)

# Plot the DataFrame as a bar chart
df.plot(kind='bar')

# Display the plot
plt.show()