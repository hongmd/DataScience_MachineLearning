'''
There are many ways to create a DataFrame in Pandas. Here are some of the most common methods:

1. From a dictionary of series: {"column_name": pd.Series(data, index=index)}
2. From a dictionary of lists or ndarrays: {"column_name": list_or_ndarray}
3. From a structured or record array: np.array([(data1), (data2)], dtype=[("col1", type1), ("col2", type2)])
4. From a list of dictionaries: [{"col1": val1, "col2": val2}, ...]
5. From a dictionary of tuples
6. From a list of namedtuples
7. From a list of dataclasses
8. Other constructors
'''

import pandas as pd
import numpy as np

#-------------------------------------------------------------------------------------------------------------#
#------------------------------------- 1. From a dictionary of series ----------------------------------------#
#-------------------------------------------------------------------------------------------------------------#

##################
## Step-by-step ##
##################

data_dict = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}

df = pd.DataFrame(data_dict)
print(df)
#    one  two
# a  1.0  1.0
# b  2.0  2.0
# c  3.0  3.0
# d  NaN  4.0
'''Here, the dictionary keys become the column names'''

#####################
## Shorter version ##
#####################

df = pd.DataFrame(
    data ={
        "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
        "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
    }
)

print(df)
#    one  two
# a  1.0  1.0
# b  2.0  2.0
# c  3.0  3.0
# d  NaN  4.0


#-------------------------------------------------------------------------------------------------------------#
#--------------------------------- 2. From a dictionary of lists or ndarrays ---------------------------------#
#-------------------------------------------------------------------------------------------------------------#

################
## from lists ##
################

df = pd.DataFrame(
    data = {
        "column_1": [1, 3, 5, 7],
        "column_2": [2.0, 4.0, 6.0, 8.0],
        "column_3": ["a", "b", "c", "d"],
    }
)

print(df)
#    column_1  column_2 column_3
# 0         1       2.0        a
# 1         3       4.0        b
# 2         5       6.0        c
# 3         7       8.0        d

###################
## from ndarrays ##
###################

df = pd.DataFrame(
    data = {
        "column_1": np.array([1.5, 3.2, 5.7, 6.8]),
        "column_2": np.array([2, 4.9, 2.3, 1.2]),
    }
)

print(df)
#    column_1  column_2
# 0       1.5       2.0
# 1       3.2       4.9
# 2       5.7       2.3
# 3       6.8       1.2

##################
## Advanced way ##
##################

df_score = pd.DataFrame(
    data = {
        "name": ["Alice"]*3 + ["Susan"]*3,
        "subject": ["Math", "Science", "English"]*2,
        "score": np.array([85, 90, 88, 92, 95, 89]),
    }
)

print(df_score)
#     name  subject  score
# 0  Alice     Math     85
# 1  Alice  Science     90
# 2  Alice  English     88
# 3  Susan     Math     92
# 4  Susan  Science     95
# 5  Susan  English     89


#-------------------------------------------------------------------------------------------------------------#
#--------------------------------- 3. From a structured or record array --------------------------------------#
#-------------------------------------------------------------------------------------------------------------#

# Create an empty structured record
record = np.zeros(
    shape = (2,), # 1D array with 2 elements
    dtype = [("A", "i4"), ("B", "f4"), ("C", "a10")] # Define the data types for each field "A", "B", "C"
)                                                    # "i4" means 4-byte integer, 
                                                     # "f4" means 4-byte float, 
                                                     # "a10" means string of length 10 (bytes
print(record)                          
# [(0, 0., b'') (0, 0., b'')]

# Fill the structured record with data
record[:] = [(1, 2.0, "Hello"), (2, 3.0, "World")]
print(record)
# [(1, 2., b'Hello') (2, 3., b'World')]

# Create DataFrame from the structured record
df = pd.DataFrame(record, index = ["first", "second"])
print(df)
#         A    B         C
# first   1  2.0  b'Hello'
# second  2  3.0  b'World'


#-------------------------------------------------------------------------------------------------------------#
#------------------------------------- 4. From a list of dictionaries ----------------------------------------#
#-------------------------------------------------------------------------------------------------------------#

##################
## Step-by-step ##
##################

list_of_dicts = [
    {"a": 1, "b": 2}, 
    {"a": 5, "b": 10, "c": 20}
]

df = pd.DataFrame(list_of_dicts, index = ["row_1", "row_2"])
print(df)
#        a   b     c
# row_1  1   2   NaN
# row_2  5  10  20.0


#####################
## Shorter version ##
#####################

df = pd.DataFrame(
    data = [
        {"a": 1.4, "b": 2.3}, 
        {"a": 5, "b": 10, "c": 20}
    ],
    index = ["row_1", "row_2"]
)

print(df)
#          a     b     c
# row_1  1.4   2.3   NaN
# row_2  5.0  10.0  20.0