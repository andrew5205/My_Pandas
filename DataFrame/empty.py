
# df.empty - indicate if DataFrame is empty or not 

import pandas as pd 

df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [4, 5, 6]
})

# print(df.empty)         # False

df1 = pd.DataFrame({
    'a': [],
    'b': []
})

print(df1.empty)            # True



