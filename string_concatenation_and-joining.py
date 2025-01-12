import pandas as pd

'''
String Concatenation and Joining Methods
1. Series.str.cat(): Concatenates strings in the Series or Index with an optional separator.
2. Series.str.join(): Joins the elements in lists contained in each string of the Series or Index using the specified separator.
'''

# Example 1: Using Series.str.cat() for concatenation
print("Example 1: Using str.cat()")
series1 = pd.Series(['Hello', 'Python', 'Data'])
series2 = pd.Series(['World', 'Programming', 'Science'])

# Concatenate strings in two Series with a space as the separator
result_cat = series1.str.cat(series2, sep=' ')
print("\nConcatenated Series (series1 and series2):")
print(result_cat)

# Concatenate all strings in a single Series with a comma as the separator
result_single_cat = series1.str.cat(sep=', ')
print("\nConcatenated Series (single series1):")
print(result_single_cat)

# Example 2: Using Series.str.join() for joining
print("\nExample 2: Using str.join()")
series_with_lists = pd.Series([['Hello', 'World'], ['Python', 'Programming'], ['Data', 'Science']])

# Join the elements in lists within the Series using a space as the separator
result_join = series_with_lists.str.join(' ')
print("\nJoined Series:")
print(result_join)

# Join with another separator, such as " - "
result_join_dash = series_with_lists.str.join(' - ')
print("\nJoined Series with ' - ' as separator:")
print(result_join_dash)
