

import pandas as pd 


# df.info() - print concise summary of DataFrame
# pd.DataFrame.info(verbose=None, buf=None, max_cols=None, memory_usage=None, show_counts=None, null_counts=None)


int_values = [1, 2, 3, 4, 5]
text_values = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
float_values = [0.0, 0.25, 0.5, 0.75, 1.0]

df = pd.DataFrame({ "int_col": int_values, 
                    "text_col": text_values, 
                    "float_col": float_values
                })

print(df)
#    int_col text_col  float_col
# 0        1    alpha       0.00
# 1        2     beta       0.25
# 2        3    gamma       0.50
# 3        4    delta       0.75
# 4        5  epsilon       1.00



print(df.info(verbose=True))              # with per-column info

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 3 columns):
#  #   Column     Non-Null Count  Dtype  
# ---  ------     --------------  -----  
#  0   int_col    5 non-null      int64  
#  1   text_col   5 non-null      object 
#  2   float_col  5 non-null      float64
# dtypes: float64(1), int64(1), object(1)
# memory usage: 248.0+ bytes
# None


print(df.info(verbose=False))               # no per-column info 

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Columns: 3 entries, int_col to float_col
# dtypes: float64(1), int64(1), object(1)
# memory usage: 248.0+ bytes
# None



# print(df.info(max_cols=1))

# print(df.info(show_counts=True))





