

# df.itertuples(index=True, name=Pandas) - Iterate over DataFrame rows as namedtuples.


import pandas as pd 

df = pd.DataFrame({
    'num_legs': [4, 2],
    'num_wings': [0, 2],},
    index=['dog', 'hawk']
)


# print(df)
# #       num_legs  num_wings
# # dog          4          0
# # hawk         2          2


print(df.itertuples())          # <map object at 0x7fcf7b2d89a0>


for row in df.itertuples():
    print(row)
# Pandas(Index='dog', num_legs=4, num_wings=0)
# Pandas(Index='hawk', num_legs=2, num_wings=2)


for row in df.itertuples(index=False):
    print(row)
# Pandas(num_legs=4, num_wings=0)
# Pandas(num_legs=2, num_wings=2)



for row in df.itertuples(name='Animals'):
    print(row)
# Animals(Index='dog', num_legs=4, num_wings=0)
# Animals(Index='hawk', num_legs=2, num_wings=2)













