
# df.iat[] -  Access a single value for a row/column integer pair.

import pandas as pd 

df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    index = [0, 1, 2], columns= [0, 1, 2]
    )


print(df)
#    0  1  2
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9


print(df.iat[0,0])      # 1
print(df.iat[1,1])      # 5
print(df.iat[2,1])      # 8


# Set value at specified row/column pair
df.iat[2,0] = 500 
print(df)
#      0  1  2
# 0    1  2  3
# 1    4  5  6
# 2  500  8  9


# Get value within a series
print(df.loc[0].at[2])          # 3




