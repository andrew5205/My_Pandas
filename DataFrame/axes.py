
# df.axes - Return a list representing the axes of the DataFrame.
#           It has the row axis labels and column axis labels as the only members. 
#           They are returned in that order.

import pandas as pd 

df = pd.DataFrame({
    'col1': [1, 2],
    'col2': [3, 4]
})

print(df)
#    col1  col2
# 0     1     3
# 1     2     4


print(df.axes)          # [RangeIndex(start=0, stop=2, step=1), Index(['col1', 'col2'], dtype='object')]






