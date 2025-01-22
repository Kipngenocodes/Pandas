import pandas as pd

'''
1	lt(other[, axis, level])	Element-wise less than comparison.
2	gt(other[, axis, level])	Element-wise greater than comparison.
3	le(other[, axis, level])	Element-wise less than or equal comparison.
4	ge(other[, axis, level])	Element-wise greater than or equal comparison.
5	ne(other[, axis, level])	Element-wise not equal comparison.
6	eq(other[, axis, level])	Element-wise equal comparison.
'''
# Create a pandas series 
s = pd.Series([1, 2, 3, 4, 5])

# Output 
print(s)
print(s.lt(3)) 
print(s.gt(3))
print(s.le(3))
print(s.ge(3))
print(s.ne(3))  
print(s.eq(3))  

