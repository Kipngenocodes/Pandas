import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
Reindexing is a powerful and fundamental operation in Pandas that
allows you to align your data with a new set of labels. 
Whether you're working with rows or columns,
reindexing gives you control over how your data aligns with the labels you specify.
Reindexing in Pandas refers to the process of conforming your data to match a new
set of labels along a specified axis (rows or columns). This process can accomplish several tasks −
    Reordering: Reorder the existing data to match a new set of labels.
    Inserting Missing Values: If a label in the new set does not exist in the original data, 
    Pandas will insert a missing value (NaN) for that label.
    Filling Missing Data: You can specify how to fill in missing values that result from reindexing, 
    using various filling methods.
'''