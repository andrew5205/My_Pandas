
# iterrows() - Iterate over DataFrame rows as (index, Series) pairs.

import pandas as pd

df = pd.DataFrame({
    'species': ['bear', 'bear', 'marsupial'],
    'population': [1864, 22000, 80000]},
    index=['panda', 'polar', 'koala']
)

# print(df)
# #         species  population
# # panda       bear        1864
# # polar       bear       22000
# # koala  marsupial       80000

print(df.iterrows())            # <generator object DataFrame.iterrows at 0x7faead6df040>

for index, value in df.iterrows():
    print(index)
    # panda
    # polar
    # koala

# print out each element in a row
for index, value in df.iterrows():
    print(value)
    # species       bear
    # population    1864
    # Name: panda, dtype: object
    # species        bear
    # population    22000
    # Name: polar, dtype: object
    # species       marsupial
    # population        80000
    # Name: koala, dtype: object





















