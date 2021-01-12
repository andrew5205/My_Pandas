
# pop() - Return item and drop from frame. Raise KeyError if not found

import pandas as pd

df = pd.DataFrame([
    ('falcon', 'bird', 389.0),
    ('parrot', 'bird', 24.0),
    ('lion', 'mammal', 80.5),
    ('monkey', 'mammal', 100)],
    columns=['name', 'class', 'speed']
)

print(df)
#      name   class  speed
# 0  falcon    bird  389.0
# 1  parrot    bird   24.0
# 2    lion  mammal   80.5
# 3  monkey  mammal  100.0


print(df.pop('class'))
# 0      bird
# 1      bird
# 2    mammal
# 3    mammal
# Name: class, dtype: object


print(df)
#     name  speed
# 0  falcon  389.0
# 1  parrot   24.0
# 2    lion   80.5
# 3  monkey  100.0










