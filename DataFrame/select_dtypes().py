

import pandas as pd

df = pd.DataFrame({
    'a': [1, 2] * 3,
    'b': [True, False] *3,
    'c': [1.0, 2.5] *3
})


print(df)
#   a      b    c
# 0  1   True  1.0
# 1  2  False  2.5
# 2  1   True  1.0
# 3  2  False  2.5
# 4  1   True  1.0
# 5  2  False  2.5


print(df.select_dtypes(include='bool'))
#       b
# 0   True
# 1  False
# 2   True
# 3  False
# 4   True
# 5  False



print(df.select_dtypes(include='float64'))
#      c
# 0  1.0
# 1  2.5
# 2  1.0
# 3  2.5
# 4  1.0
# 5  2.5


print(df.select_dtypes(include='int64'))
#    a
# 0  1
# 1  2
# 2  1
# 3  2
# 4  1
# 5  2










