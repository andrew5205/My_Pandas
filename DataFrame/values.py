
# df.values - Only the values in the DataFrame will be returned, the axes labels will be removed.


import pandas as pd


df = pd.DataFrame({
    'age': [3, 29],
    'height': [99, 180],
    'weight': [30, 65]
})

# print(df)
# #    age  height  weight
# # 0    3      99      30
# # 1   29     180      65


print(df.values)
# [[  3  99  30]
#  [ 29 180  65]]




df2 = pd.DataFrame([
    ('a', 12, "how"),
    ('b', 25.0, 1),
    ('c', 'lion', None),
])

print(df2.values)
# [['a' 12 'how']
#  ['b' 25.0 1]
#  ['c' 'lion' None]]



