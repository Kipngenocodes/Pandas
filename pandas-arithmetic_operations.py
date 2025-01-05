import pandas as pd
import numpy as np
'''
Arithmetic Operations on a Series with Scalar Value
Arithmetic operations on a Pandas Series object can be directly applied to an entire Series elements,
which means the operation is executed element-wise across all values.
This is very similar to how operations work with NumPy arrays.
'''
'''
Operation	Example	Description
Addition	s + 2	Adds 2 to each element
Subtraction	s - 2	Subtracts 2 from each element
Multiplication	s * 2	Multiplies each element by 2
Division	s / 2	Divides each element by 2
Exponentiation	s ** 2	Raises each element to the power of 2
Modulus	s % 2	Finds remainder when divided by 2
Floor Division	s // 2	Divides and floors the quotient by 2 (removes the remainder)'''


# Example demonstrates arithmetic operations on a Series with a scalar value.
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# Display the original series
print("Original Series:\n", s)

# Perform arithmetic operations on the series
# Addition
print("\nAddition:")
print(s + 2)
print("\nSubtraction:")
print(s - 2)
print("\nMultiplication:")
print(s * 2)
print("\nDivision:")
print(s / 2)
print("\nExponentiation:")
print(s ** 2)
print("\nModulus:")
print(s % 2)
print("\nFloor Division:")
print(s // 2)
