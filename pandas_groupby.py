import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print(df)

# Splitting data into groups 
df_grouped = df.groupby(['Team','Year'])
print(df_grouped)

# Pandas object can be split into any of their objects. There are multiple ways to split an object like −

'''
obj.groupby('key')
obj.groupby(['key1','key2'])
obj.groupby(key,axis=1)
'''
# View group
print (df.groupby('Team').groups)

