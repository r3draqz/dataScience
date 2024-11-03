import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Company": ["GOOG", "GOOG", "MSFT", "MSFT", "FB", "FB"],
    "Person": ["Sam", "Charlie", "Amy", "Vanessa", "Carl", "Sarah"],
    "Sales": [200,120,340,124,243,350]
})

print(df)

byComp = df.groupby('Company')
print(byComp["Sales"].mean())
print(byComp.apply(lambda x: x.select_dtypes(include="number").mean())) # same as above. saying for every group (x), select only the columns that are numeric.

print(byComp["Sales"].sum().loc['FB'])

print(byComp.count()) # counts how many values in each group

print(df.groupby("Company").describe()) # gives all of them

