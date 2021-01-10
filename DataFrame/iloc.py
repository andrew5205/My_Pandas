
# df.iloc[] - Purely integer-location based indexing for selection by position.
                # from 0 to length-1 of the axis
                
# a. Indexing just the rows
# b. Indexing both axes

import pandas as pd 

my_dict = [
    {'a': 1, 'b': 2, 'c': 3, 'd': 4},
    {'a': 100, 'b': 200, 'c': 300, 'd': 400},
    {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}
]

df = pd.DataFrame(my_dict)
# print(df)
# #       a     b     c     d
# # 0     1     2     3     4
# # 1   100   200   300   400
# # 2  1000  2000  3000  4000



# ***************************************************************************************************************
# a. Indexing just the rows

print(type(df.iloc[0]))         # <class 'pandas.core.series.Series'>
print(df.iloc[0])
# a    1
# b    2
# c    3
# d    4
# Name: 0, dtype: int64


# Note using [[]] returns a DataFrame.
print(type(df.iloc[[0]]))           # <class 'pandas.core.frame.DataFrame'>
print(df.iloc[[0]])
#    a  b  c  d
# 0  1  2  3  4


print(df.iloc[[0, 1]])
#      a    b    c    d
# 0    1    2    3    4
# 1  100  200  300  400


# slice object 
print(df.iloc[:3])
#       a     b     c     d
# 0     1     2     3     4
# 1   100   200   300   400
# 2  1000  2000  3000  4000


# With a boolean mask the same length as the index.
#     df.iloc[[  0,    1,    2]]
print(df.iloc[[True, False, True]])
#       a     b     c     d
# 0     1     2     3     4
# 2  1000  2000  3000  4000


# The x passed to the lambda is the DataFrame being sliced.
print(df.iloc[lambda x : x.index % 2 == 0])
#       a     b     c     d
# 0     1     2     3     4
# 2  1000  2000  3000  4000


# ***************************************************************************************************************
# b. Indexing both axes
# mix the indexer types for the index and columns. Use : to select the entire axis.

print(df.iloc[0,1])         # 2

print(df.iloc[[0,2], [1,3]])
#       b     d
# 0     2     4
# 2  2000  4000


print(df.iloc[1:3, 0:3])
#       a     b     c
# 1   100   200   300
# 2  1000  2000  3000



