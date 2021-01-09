
# df.head - Return the first n rows. 
            # default n = 5

import pandas as pd 

df = pd.DataFrame({
    'animal': ['alligator', 'bee', 'falcon', 'lion', 'monkey', 'parrot', 'shark', 'whale', 'zebra'],
    'food': ['a', 'b', 'f', 'l', 'm', 'p', 's', 'w', 'z']
})


# default n = 5
print(df.head())
#       animal food
# 0  alligator    a
# 1        bee    b
# 2     falcon    f
# 3       lion    l
# 4     monkey    m


print(df.head(3))
#       animal food
# 0  alligator    a
# 1        bee    b
# 2     falcon    f

# negative n can be looked as total -n
print(df.head(-3))
#       animal food
# 0  alligator    a
# 1        bee    b
# 2     falcon    f
# 3       lion    l
# 4     monkey    m
# 5     parrot    p




