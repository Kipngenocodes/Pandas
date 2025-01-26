import pandas as pd

'''
Pandas allows you to reorder or reset the categories in your categorical data
using .cat.reorder_categories() and .cat.set_categories() methods.
reorder_categories(): This method is used to reorder the existing categories with the specified new_categaries.
set_categories(): This method allows you to define a new set of categories,
which may involve adding new categories or removing existing ones.
'''

# Create a Series with categorical data
s = pd.Series(['a', 'b', 'c', 'a', 'b', 'c'], dtype='category')
print("Original Series:")
print(s)

# Reorder categories using reorder_categories
s_reordered = s.cat.reorder_categories(["b", "a", "c"], ordered=True)
print("\nSeries with Reordered Categories:")
print(s_reordered)

# Set new categories using set_categories
s_new_categories = s.cat.set_categories(["d", "b", "a", "c"], ordered=True)
print("\nNew Categories Set:")
print(s_new_categories)

# Sorting Categorical Data
# The .sort_values() method can be used to sort the values in a Series or DataFrame.
# When sorting categorical data, the .sort_values() method will sort the categories in the order they
# appear in the .cat.categories attribute.
# If you want to sort the categories in a different order, you can use the .cat.reorder_categories() 
# method to reorder the categories before sorting.

# Sort the categorical series without any predefined order (lexical sorting)
print("\nLexical Sorting:")
print(s.sort_values())

# Define a custom order for the categories
s = s.cat.set_categories(['b', 'a', 'c'], ordered=True)

# Sort the categorical series with the defined order
print("\nSorted with Defined Category Order:")
print(s.sort_values())

# Create a DataFrame with categorical columns
df = pd.DataFrame({
    'A': ['a', 'b', 'c', 'a', 'b', 'c'],
    'B': ['x', 'y', 'z', 'x', 'y', 'z'],
    'C': ['1', '2', '3', '1', '2', '3'],
    'D': ['a', 'b', 'c', 'a', 'b', 'c']
})

# Convert columns to categorical with custom categories and order
df['A'] = df['A'].astype('category').cat.set_categories(['b', 'a', 'c'], ordered=True)
df['B'] = df['B'].astype('category').cat.set_categories(['y', 'x', 'z'], ordered=True)
df['C'] = df['C'].astype('category').cat.set_categories(['2', '1', '3'], ordered=True)
df['D'] = df['D'].astype('category').cat.set_categories(['b', 'a', 'c'], ordered=True)

# Sort by multiple columns
sorted_df = df.sort_values(by=["A", "B"])
print("\nSorted DataFrame:")
print(sorted_df)