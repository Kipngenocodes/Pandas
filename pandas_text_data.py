import pandas as pd
import numpy as np

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
1	Series.str.capitalize() :Transforms the first character of each string in the Series or
    Index to uppercase and the rest to lowercase.
2  Series.str.casefold() :Converts each string to lowercase in a more aggressive manner
    suitable for case-insensitive comparisons.
3	Series.str.lower() :Converts all characters in each string of the Series or Index to lowercase.
4	Series.str.upper() : Converts all characters in each string of the Series or Index to uppercase.
5	Series.str.title() :Converts each string to titlecase, where the first character
    of each word is capitalized and the rest are lowercase.
6	Series.str.swapcase(): Swaps case – converts uppercase characters to lowercase and vice versa.
7	Series.str.replace() :Replaces occurrences of a pattern or regular expression 
    in each string with another string.
'''

# create three series
s1 = pd.Series(['hello', 'world', 'python'])
s2 = pd.Series(['Hello', 'World', 'Python'])
s3 = pd.Series(['HELLO', 'WORLD', 'PYTHON'])
s4 = pd.Series(['Hello World', 'World Python', 'Python Hello'])
s5 = pd.Series(['Hello World', 'World Python', 'Python Hello'])

# converting  the first character of each string in the Series or Index to uppercase and the rest to lowercase.
print(s1.str.capitalize())  # Output: 0    Hello 1    World 2
print(s2.str.capitalize())  # Output: 0    Hello 1    World 2
print(s3.str.capitalize())  # Output: 0    Hello 1    World 2
print(s4.str.capitalize())  # Output: 0    Hello World 1    World Python
print(s5.str.capitalize())  # Output: 0    Hello World 1    World Python
print("\n")
# converting each string to lowercase in a more aggressive manner suitable for case-insensitive comparisons.
print(s1.str.casefold())  # Output: 0    hello 1    world 2    python
print(s2.str.casefold())  # Output: 0    hello 1    world
print(s3.str.casefold())  # Output: 0    hello 1    world
print(s4.str.casefold())  # Output: 0    hello world 1    world
print(s5.str.casefold())  # Output: 0    hello world 1    world
print("\n")
# converting all characters in each string of the Series or Index to lowercase.
print(s1.str.lower())  # Output: 0    hello 1    world 2
print(s2.str.lower())  # Output: 0    hello 1    world 2
print(s3.str.lower())  # Output: 0    hello 1    world 2
print(s4.str.lower())  # Output: 0    hello world 1    world python
print(s5.str.lower())  # Output: 0    hello world 1    world python
print("\n")
# converting all characters in each string of the Series or Index to uppercase.
print(s1.str.upper())  # Output: 0    HELLO 1    WORLD
print(s2.str.upper())  # Output: 0    HELLO 1    WORLD
print(s3.str.upper())  # Output: 0    HELLO 1    WORLD
print(s4.str.upper())  # Output: 0    HELLO WORLD 1    WORLD
print(s5.str.upper())  # Output: 0    HELLO WORLD 1    WORLD
print("\n")
# converting each string to titlecase, where the first character of each word is capitalized and the rest
# are lowercase.
print(s1.str.title())  # Output: 0    Hello 1    World 2
print(s2.str.title())  # Output: 0    Hello 1    World 2
print(s3.str.title())  # Output: 0    Hello 1    World 2
print(s4.str.title())  # Output: 0    Hello World 1    World Python
print(s5.str.title())  # Output: 0    Hello World 1    World Python
print("\n")
# Swaps case – converts uppercase characters to lowercase and vice versa.
print(s1.str.swapcase())  # Output: 0    hELLO 1
print(s2.str.swapcase())  # Output: 0    hELLO 1
print(s3.str.swapcase())  # Output: 0    hELLO 1
print(s4.str.swapcase())
print('\n')
# Replaces occurrences of a pattern or regular expression in each string with another string.
print(s1.str.replace())  # Output: 0    hELLO 1
print(s2.str.replace())  # Output: 0    hELLO 1
print(s3.str.replace())  # Output: 0    hELLO 1
print(s4.str.replace())
