
# df.items() - Iterate over (column name, Series) pairs.
#                return asDataFrame in memory,  object - (col, val)

import pandas as pd

df = pd.DataFrame({
    'species': ['bear', 'bear', 'marsupial'],
    'population': [1864, 22000, 80000]},
    index=['panda', 'polar', 'koala']
)

print(df)
#         species  population
# panda       bear        1864
# polar       bear       22000
# koala  marsupial       80000


print(df.items())           # <generator object DataFrame.items at 0x7fda2225ec10>

for i, val in df.items():
    print(i)
    print(val)
# species
# panda         bear
# polar         bear
# koala    marsupial
# Name: species, dtype: object
# population
# panda     1864
# polar    22000
# koala    80000
# Name: population, dtype: int64


for col, val in df.items():
    print(col)
# species
# population


for col, val in df.items():
    print(val)
# panda         bear
# polar         bear
# koala    marsupial
# Name: species, dtype: object
# panda     1864
# polar    22000
# koala    80000
# Name: population, dtype: int64











