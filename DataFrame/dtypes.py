
import pandas as pd 



# df = pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)


df = pd.DataFrame({
    'float': [1.0],
    'int': 1,
    'datetime': [pd.Timestamp('20210104')],
    'string': ['foo']
})

print(df.dtypes)

# float              float64
# int                  int64
# datetime    datetime64[ns]
# string              object
# dtype: object




