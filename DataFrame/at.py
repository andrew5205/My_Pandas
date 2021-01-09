
# df.at[] -  Access a single value for a row/column label pair.

import pandas as pd 

df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    index = ['a', 'b', 'c'], columns= ['col1', 'col2', 'col3']
    )


print(df)
#    col1  col2  col3
# a     1     2     3
# b     4     5     6
# c     7     8     9


# Get value at specified row/column pair
print(df.at['c','col2'])        # 8


# Set value at specified row/column pair
df.at['a', 'col1'] = 999
print(df)
#    col1  col2  col3
# a   999     2     3
# b     4     5     6
# c     7     8     9


# Get value within a Series
print(df.loc['b'].at['col3'])           # 6




