import numpy as np
import pandas as pd
from numpy.random import randn

# np.random.seed(101) # gets the same set of random numbers

##### DATA FRAME #####
# df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'], ['W','X','Y','Z']) # 5 rows, 4 columns of a random number
# print(df)

# print(df['W'])
# print(type(df['W']))

# print(df[['W','Z']]) # have to use double brackets for multiple columns

# df['new'] = df['W'] + df['Y'] # adds a new column
# # print(df)

# df.drop('new', axis = 1) # axis has to equal 1 to get rid of an actual column. will still be in the actual df if i print it
# print(df)

# print(df.drop('new', axis = 1, inplace=True)) # actually gets rid of the column

# # print(df.drop('E')) # dont have to have axis equal to anything because axis equals 0 which is the row

# print(df.shape) # shows how many rows and columns

# print(df)

# print(df.loc['A']) # prints the row

# print(df.iloc[1]) # returns row based on the index (don't have to give the column name)

# print(df.loc['B','Y']) # returns 1 value because it's the row and column

# print(df.loc[['A', 'B'], ['W', 'Y']]) # multiple rows and columns

# print(df.loc[['A','B']]) # prints row a and b

# print(df.iloc[[1,2]]) # based on index

#### CONDITIONAL SELECTION ####

# print(df>0) # will print True or False in the df structure where condition is/isn't met

# print(df[df>0]) # will print numbers anywhere that a meets the condition

# print(df['W']>0) # can do it for specific columns too

## the df surronding the df['W'] condition is what makes you access the actual data frame's values
# print(df[df['W']>0]) # this will print the entire data frame where the row meets the conditions in column "W"

# print(df.loc['A'][df.loc['A']>0]) # prints row A where the columns meet the criteria

# print(df[df['W']>0]['X']) # prints only column X of the data frame where column W meets that criteria rather than the entire df.

# boolser = df['W']>0 # what we did earlier put into a series
# result = df[boolser] # saves the series condition as a full df to a var
# print(boolser, result) # will print the true/false values of the series and then the df
# print(result['W']) # equal to print(df[df['W']>0]['W'])

### 2 more conditions

# print(df[(df['W']>0) & (df['Y']>1)]) # telling it to go into data frame and return where they = true

# print(df[(df['W']>0) | (df['Y']>1)]) # telling it to go into data frame and return where one of them = true

# print(df.reset_index()) # will make the index (row) 0,1,2,3 (typical)

# print(df) # as you can see it doesn't reset in place

# df.reset_index(inplace=True) # if i run this it will reset and make df diff

# newind = 'CA NY WY OR CO'.split() # creates list

# print(newind)

# df['States'] = newind # add new column with this list as rows
# print(df)

# print(df.set_index('States')) # makes this the index

#### INDEX LEVELS ####

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside)) # creates a list of tuple pairs [('G1', 1),('G1', 2)...]
hier_index = pd.MultiIndex.from_tuples(hier_index) # will put everything on the first index of its tuple in one column and second as an under index

df = pd.DataFrame(randn(6,2), hier_index, ['A', 'B']) # multiple levels of an index G1 is first level and 1,2,3 as the second level. A and B are columns

# print(df.loc['G1']) # prints the df that is in the G1 level.

# print(df.loc['G1'].loc[1]) # accesses the index named 1 in G1

df.index.names = ['Groups', 'Num'] # names the rows

# print(df) 

# print(df, df.loc['G2'].loc[2]['B']) # returns the specific number

print(df.xs(1, level='Num')) # goes inside a multi level index easily where index name = Num and 1 is the row name so from both G1 and G2