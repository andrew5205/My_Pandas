
# df.keys() - get info axis, => columns



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


print(df.keys())
# Index(['species', 'population'], dtype='object')








