
import pandas as pd

df = pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)


# structure also contains labeled axes (rows and columns)
# Can be thought of as a dict-like container for Series objects
# The primary pandas data structure


d = {'col1': [1, 2], 'col2': [3, 4], 'col3': [5, 6]}
df = pd.DataFrame(d)


# print(df)
# #    col1  col2  col3
# # 0     1     3     5
# # 1     2     4     6



# print(df._data)
# # BlockManager
# # Items: Index(['col1', 'col2', 'col3'], dtype='object')
# # Axis 1: RangeIndex(start=0, stop=2, step=1)
# # IntBlock: slice(0, 3, 1), 3 x 2, dtype: int64



# print(df.index)         # RangeIndex(start=0, stop=2, step=1)




# print(df.columns)           # Index(['col1', 'col2', 'col3'], dtype='object')



# print(df.dtypes)
# # col1    int64
# # col2    int64
# # col3    int64
# # dtype: object



# print(df.copy)              # True/ False



