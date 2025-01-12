import pandas as pd

'''
Pandas provides powerful tools for working with text data using the .str accessor. 
This allows us to apply various string operations on Series and Index objects,
which work efficiently on string manipulation within a Pandas DataFrame.

The .str accessor provides a variety of string methods that can perform operations 
like string transformation, concatenation, searching, and many other on string objects.
'''

'''
String Transformation
This category includes methods that transform the strings in some way, such as changing
the case, formatting, or modifying specific characters.
1. Series.str.capitalize(): Transforms the first character of each string in the Series or
   Index to uppercase and the rest to lowercase.
2. Series.str.casefold(): Converts each string to lowercase in a more aggressive manner
   suitable for case-insensitive comparisons.
3. Series.str.lower(): Converts all characters in each string of the Series or Index to lowercase.
4. Series.str.upper(): Converts all characters in each string of the Series or Index to uppercase.
5. Series.str.title(): Converts each string to title case, where the first character
   of each word is capitalized and the rest are lowercase.
6. Series.str.swapcase(): Swaps case – converts uppercase characters to lowercase and vice versa.
7. Series.str.replace(): Replaces occurrences of a pattern or regular expression 
   in each string with another string.
'''

# Create multiple Series
s1 = pd.Series(['hello', 'world', 'python'])
s2 = pd.Series(['Hello', 'World', 'Python'])
s3 = pd.Series(['HELLO', 'WORLD', 'PYTHON'])
s4 = pd.Series(['Hello World', 'World Python', 'Python Hello'])
s5 = pd.Series(['Hello World', 'World Python', 'Python Hello'])

# Applying string transformations
print("String Transformation Examples:")

# Capitalize each string
print("Capitalize:")
print(s1.str.capitalize())
print(s2.str.capitalize())
print(s3.str.capitalize())
print(s4.str.capitalize())
print(s5.str.capitalize())

print("\nCasefold (aggressive lowercase):")
print(s1.str.casefold())
print(s2.str.casefold())
print(s3.str.casefold())
print(s4.str.casefold())
print(s5.str.casefold())

print("\nLowercase:")
print(s1.str.lower())
print(s2.str.lower())
print(s3.str.lower())
print(s4.str.lower())
print(s5.str.lower())

print("\nUppercase:")
print(s1.str.upper())
print(s2.str.upper())
print(s3.str.upper())
print(s4.str.upper())
print(s5.str.upper())

print("\nTitle Case:")
print(s1.str.title())
print(s2.str.title())
print(s3.str.title())
print(s4.str.title())
print(s5.str.title())

print("\nSwapcase:")
print(s1.str.swapcase())
print(s2.str.swapcase())
print(s3.str.swapcase())
print(s4.str.swapcase())
print(s5.str.swapcase())

# Replace occurrences of a word
print("\nReplace 'World' with 'Universe':")
print(s4.str.replace('World', 'Universe', regex=False))
print(s5.str.replace('Python', 'Code', regex=False))

