import pandas as pd 
# Arithmetic Operations on DataFrame with Scalar Value

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Display the input DataFrame
print("Input DataFrame:\n", df)

# Perform arithmetic operations
print("\nAddition:\n", df + 2)
print("\nSubtraction:\n", df - 2)
print("\nMultiplication:\n", df * 2)
print("\nDivision:\n", df / 2)
print("\nExponentiation:\n", df ** 2)
print("\nModulus:\n", df % 2)
print("\nFloor Division:\n", df // 2)


# Arithmetic Operations Between Two DataFrames
# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
df2 = pd.DataFrame({'A': [10, 20, 30], 'B': [50, 60, 70]}, index=[1, 2, 3])

# Display the input DataFrames
print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# Perform arithmetic operations
print("\nAddition:\n", df1 + df2)
print("\nSubtraction:\n", df1 - df2)
print("\nMultiplication:\n", df1 * df2)
print("\nDivision:\n", df1 / df2)