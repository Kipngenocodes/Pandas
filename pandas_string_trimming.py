import pandas as pd

'''
String Trimming and Removal Operations
1. Series.str.lstrip(): Removes leading characters (by default, whitespace) from each string.
2. Series.str.strip(): Removes leading and trailing characters (by default, whitespace) from each string.
3. Series.str.rstrip(): Removes trailing characters (by default, whitespace) from each string.
4. Series.str.removeprefix(prefix): Removes the specified prefix from each string in the Series or Index, if it exists.
5. Series.str.removesuffix(suffix): Removes the specified suffix from each string in the Series or Index.
'''

# Create a Series with strings containing extra spaces, prefixes, and suffixes
s = pd.Series(['   Hello World   ', '   Python Programming   ', '   Data Science   ', 'Pre_Hello', 'Hello_Suffix'])

print("Original Series:")
print(s)

# Remove leading characters (default: whitespace)
print("\nRemoving leading whitespace using lstrip():")
print(s.str.lstrip())

# Remove both leading and trailing characters (default: whitespace)
print("\nRemoving leading and trailing whitespace using strip():")
print(s.str.strip())

# Remove trailing characters (default: whitespace)
print("\nRemoving trailing whitespace using rstrip():")
print(s.str.rstrip())

# Remove a specific prefix
print("\nRemoving the prefix 'Pre_' using removeprefix():")
print(s.str.removeprefix('Pre_'))

# Remove a specific suffix
print("\nRemoving the suffix '_Suffix' using removesuffix():")
print(s.str.removesuffix('_Suffix'))
