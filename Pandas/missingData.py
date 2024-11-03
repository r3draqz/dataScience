import numpy as np
import pandas as pd

d = {
    "A":[1,2,np.nan], 
    "B":[5,np.nan,np.nan],
    "C":[1,2,3]
    } # columns are a, b, c. rows are the indices.

df = pd.DataFrame(d)
print(df)

print(df.dropna()) # will drop any rows with a null value so the entirety of row 1 and 2
print(df.dropna(axis=1)) # drops columns with null value
print(df.dropna(thresh=2)) # will keep any rows with at least 2 non null values
df["A"].fillna(value=df["A"].mean(), inplace=True)
print(df)

