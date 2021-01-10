
# df.insert() - Insert column into DataFrame at specified location.
# only for column

import pandas as pd 

df = pd.DataFrame([])

# print(df)
# # Empty DataFrame
# # Columns: []
# # Index: []

df.insert(loc=0, column='col1', value=[23], allow_duplicates=True)
# print(df)
# #    col1
# # 0    23
# print(df.head())
# #    col1
# # 0    23


df1 = pd.DataFrame({
    'a': [1, 2],
    'b': [3, 4],
    'c': [5, 6]
})
# print(df1)
# #    a  b  c
# # 0  1  3  5
# # 1  2  4  6


df1.insert(loc=1, column='g', value=[10,20])
# print(df1)
# #    a   g  b  c
# # 0  1  10  3  5
# # 1  2  20  4  6








