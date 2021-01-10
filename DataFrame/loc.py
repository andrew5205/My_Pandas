
# df.loc[] - Access a group of rows and columns by label(s) or a boolean array.

import pandas as pd

df = pd.DataFrame(
    [[1,2], [4,5], [7,8]],
    index= ['cobra', 'viper', 'sidewinder'],
    columns=['max_speed', 'sheild']
)


# print(df)
# #             max_speed  sheild
# # cobra               1       2
# # viper               4       5
# # sidewinder          7       8



# Single label. Note this returns the row as a Series.
print(df.loc['viper'])
# max_speed    4
# sheild       5
# Name: viper, dtype: int64


# List of labels. Note using [[]] returns a DataFrame.
print(df.loc[['viper','sidewinder']])
#             max_speed  sheild
# viper               4       5
# sidewinder          7       8


print(df.loc['viper', 'max_speed'])         # 4


# slicing 
# df.loc[row1:row2, col1:col2]
print(df.loc['cobra': 'viper', 'max_speed'])
# cobra    1
# viper    4
# Name: max_speed, dtype: int64


print(df.loc['cobra': 'viper', 'max_speed':'sheild'])
#        max_speed  sheild
# cobra          1       2
# viper          4       5


# Alignable bool series
print(df.loc[pd.Series([False, True,False], index=['viper', 'sidewinder', 'cobra'])])
#             max_speed  sheild
# sidewinder          7       8


# index - same as df.reindex
print(df.loc[pd.Index(['cobra', 'viper'], name='foo')])
#        max_speed  sheild
# foo                     
# cobra          1       2
# viper          4       5


# Conditional return bool condition
print(df.loc[df['sheild'] > 5])
#             max_speed  sheild
# sidewinder          7       8

# 
print(df.loc[lambda df: df['sheild'] == 8])
#             max_speed  sheild
# sidewinder          7       8


# Condition return with specific labels
print(df.loc[df['sheild'] > 5, ['max_speed']])
#             max_speed
# sidewinder          7


# ***************************************************************************************************************
# SET VALUES

df.loc[['viper', 'sidewinder'], ['shield']] = 1000
print(df)
#             max_speed  sheild  shield
# cobra               1       2     NaN
# viper               4       5  1000.0
# sidewinder          7       8  1000.0


# set value for entire row
df.loc['cobra'] =0
print(df)
#             max_speed  sheild
# cobra               0       0
# viper               4       5
# sidewinder          7       8


# set value for entire column
df.loc[:, 'sheild'] = 555
print(df)
#             max_speed  sheild
# cobra               1     555
# viper               4     555
# sidewinder          7     555



# ***************************************************************************************************************
# Getting values on a DataFrame with an index that has integer labels

df_index_change = pd.DataFrame(
    [[1,2], [3,4], [5,6]],
    index=[100, 200, 300],
    columns=['max_speed', 'sheild']
)
# print(df_index_change)
# #     max_speed  sheild
# # 11          1       2
# # 12          3       4
# # 13          5       6


#  both the start and stop of the slice are included
print(df_index_change.loc[100:300])
#      max_speed  sheild
# 100          1       2
# 200          3       4
# 300          5       6


# # ***************************************************************************************************************
# Multiple Index

tuples = [
    ('cobra', 'mark i'),
    ('cobra', 'mark ii'),
    ('sidewinder', 'mark i'),
    ('sidewinder', 'mark ii'),
    ('viper', 'mark ii'),
    ('viper', 'mark iii')
]

index = pd.MultiIndex.from_tuples(tuples)

values = [
    [12,2], [0,4], [10,20], [1,4], [7,1], [16,36]
]

df = pd.DataFrame(values, columns=['max_speed', 'shield'], index=index)
print(df)
#                     max_speed  shield
# cobra      mark i           12       2
#            mark ii           0       4
# sidewinder mark i           10      20
#            mark ii           1       4
# viper      mark ii           7       1
#            mark iii         16      36


print(df.loc['cobra'])
#          max_speed  shield
# mark i          12       2
# mark ii          0       4



print(df.loc['cobra', 'mark i'])
# max_speed    12
# shield        2
# Name: (cobra, mark i), dtype: int64


# Note using [[]] returns a DataFrame.
# (index, colum)
print(df.loc[[('cobra', 'mark ii')]])
#                max_speed  shield
# cobra mark ii          0       4


print(df.loc[('cobra', 'mark i'), 'shield'])                # 2


# Slice from index tuple to single label
print(df.loc[('cobra', 'mark i'): 'viper'])
#                     max_speed  shield
# cobra      mark i           12       2
#            mark ii           0       4
# sidewinder mark i           10      20
#            mark ii           1       4
# viper      mark ii           7       1
#            mark iii         16      36


# Slice from index tuple to index tuple
print(df.loc[('cobra', 'mark i'): ('viper', 'mark ii')])
#                    max_speed  shield
# cobra      mark i          12       2
#            mark ii          0       4
# sidewinder mark i          10      20
#            mark ii          1       4
# viper      mark ii          7       1


