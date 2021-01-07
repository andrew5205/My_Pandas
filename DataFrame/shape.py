


# df.shape - Return a tuple representing the dimensionality of the DataFrame.

import pandas as pd


s = pd.Series({
    'a': 1,
    'b': 2,
    'c': 3
})
print(s)
# a    1
# b    2
# c    3
# dtype: int64

print(s.shape)           # (3,)



df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [4, 5, 6]
})

print(df)
#    a  b
# 0  1  4
# 1  2  5
# 2  3  6

print(df.shape)          # (3, 2)




























