
# df.tail() - Return the last n rows.

import pandas as pd 

df = pd.DataFrame({
    'animal': ['alligator', 'bee', 'falcon', 'lion', 'monkey', 'parrot', 'shark', 'whale', 'zebra']
})


# print(df)
# #       animal
# # 0  alligator
# # 1        bee
# # 2     falcon
# # 3       lion
# # 4     monkey
# # 5     parrot
# # 6      shark
# # 7      whale
# # 8      zebra


print(df.tail(3))
#  animal
# 6  shark
# 7  whale
# 8  zebra



print(df.tail(-3))
#    animal
# 3    lion
# 4  monkey
# 5  parrot
# 6   shark
# 7   whale
# 8   zebra














