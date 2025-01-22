import pandas as pd

# Create a MultiIndex object
index = pd.MultiIndex.from_tuples(
    [('A', 'one'), ('A', 'two'), ('A', 'three'),
     ('B', 'one'), ('B', 'two'), ('B', 'three')],
    names=["level0", "level1"]
)

# Create a DataFrame
data = [[1, 3], [7, 8], [9, 10], [11, 12], [13, 14], [15, 90]]  # 6 rows to match index
Dataframeone = pd.DataFrame(data, index=index, columns=['A', 'B'])

print("Original DataFrame:")
print(Dataframeone)

# Sorting the MultiIndex by level0 and level1
Dataframeone = Dataframeone.sort_index()
print("\nDataFrame after sorting MultiIndex:")
print(Dataframeone)
