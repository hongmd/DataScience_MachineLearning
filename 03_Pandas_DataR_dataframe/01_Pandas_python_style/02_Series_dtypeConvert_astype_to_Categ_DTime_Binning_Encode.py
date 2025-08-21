'''
Converting and casting data types is a fundamental operation in pandas data manipulation.

Flow of contents:
1. .astype(): .astype("int64"), .astype("float64"), .astype("str"), .astype("category"), .astype("bool")
2. pd.to_numeric(): Safe Numeric Conversion
3. pd.Categorical(): Create Categorical Data
4. pd.to_datetime(): Convert to Datetime
5. pd.to_timedelta(): Convert to Timedelta
6. .infer_objects(): Infer Better Object Types
7. .convert_dtypes(): Convert to Best Possible Types
8. String conversion: .astype(str), .map(str), .apply(str), .apply(lambda x: str(x))
9. Binning and Discretization: pd.cut(), pd.qcut()
10. Categorical Encoding: pd.factorize(), pd.get_dummies()
'''

import pandas as pd

#-------------------------------------------------------------------------------------------------#
#---------------------------------------- 1. .astype() -------------------------------------------#
#-------------------------------------------------------------------------------------------------#

s_nums = pd.Series([1, 2, 3, 4, 5])
s_str_int = pd.Series(['1', '2', '3', '4', '5'])
s_str_float = pd.Series(['1.5', '2.3', '3.6', '4.2', '5.0'])
s_mixed = pd.Series([1, 'a', 3.0, '4.5', False])

####################
## .astype(int64) ##
####################

s_convert = s_str_int.astype('int64')
print(s_convert)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

s_convert = s_str_float.astype('int64') # ValueError: invalid literal for int() with base 10: '1.5'


######################
## .astype(float64) ##
######################

s_convert = s_nums.astype('float64')
print(s_convert)
# 0    1.0
# 1    2.0
# 2    3.0
# 3    4.0
# 4    5.0
# dtype: float64

s_convert = s_str_int.astype('float64')
print(s_convert)
# 0    1.0
# 1    2.0
# 2    3.0
# 3    4.0
# 4    5.0
# dtype: float64

s_convert = s_str_float.astype('float64')
print(s_convert)
# 0    1.5
# 1    2.3
# 2    3.6
# 3    4.2
# 4    5.0
# dtype: float64

s_convert = s_mixed.astype('float64')  # ValueError: could not convert string to float: 'a'


##################
## .astype(str) ##
##################

s_convert = s_nums.astype('str')
print(s_convert)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: object

s_convert = s_mixed.astype('str')
print(s_convert)
# 0        1
# 1        a
# 2      3.0
# 3      4.5
# 4    False
# dtype: object

print(s_convert[4])
# 'False'


#########################
## .astype('category') ##
#########################

s_gender = pd.Series(["M", "M", "F", "M", "LGBTQ", "F", "M", "F", "LGBTQ", "M"])

'''
How .astype('category') works:
- Converts the Series to a categorical type.
- Categories are stored as a separate array, which saves memory.
- Useful for columns with a limited number of unique values.
- Categories are ordered from A-Z or increasing order.
'''

s_convert = s_gender.astype('category')
print(s_convert)
# 0        M
# 1        M
# 2        F
# 3        M
# 4    LGBTQ
# 5        F
# 6        M
# 7        F
# 8    LGBTQ
# 9        M
# dtype: category
# Categories (3, object): ['F', 'LGBTQ', 'M']


###################
## .astype(bool) ##
###################

s_bool_demo = pd.Series([0, -1.1, 2, '', 'text', None, True, False])

'''
How .astype(bool) works:
- Numeric values: 0 is False, all other numbers are True.
- Strings: Empty strings are False, non-empty strings are True.
- Booleans: True remains True, False remains False.
- None/NaN: Treated as False.
'''

s_convert = s_bool_demo.astype('bool')
print(s_convert)
# 0    False
# 1     True
# 2     True
# 3    False
# 4     True
# 5    False
# 6     True
# 7    False
# dtype: bool


#-------------------------------------------------------------------------------------------------#
#---------------------------------------- 2. pd.to_numeric() -------------------------------------#
#-------------------------------------------------------------------------------------------------#

'''
pd.to_numeric() works like .astype("int64") or .astype("float64"), but it is safer.
It can handle errors more gracefully, allowing you to specify how to deal with invalid parsing.

It has parameters like errors='coerce' to convert invalid parsing to NaN, 
or errors='ignore' to return the original data without conversion.
(By default, errors='raise', which raises an error for invalid parsing.)
'''

s_str_float = pd.Series(['1.5', '2.3', '3.6', '4.2', '5.0'])
s_mixed = pd.Series([1, 'a', 3.0, '4.5', False])

# Try with valid numeric strings
s_convert = pd.to_numeric(s_str_float)
print(s_convert)
# 0    1.5
# 1    2.3
# 2    3.6
# 3    4.2
# 4    5.0
# dtype: float64

# Try with invalid mixed data (will raise an error)
s_convert = pd.to_numeric(s_mixed) # ValueError: Unable to parse string "a" at position 1

# Try with mixed data, but coerce errors to NaN
s_convert = pd.to_numeric(s_mixed, errors = 'coerce')
print(s_convert)
# 0    1.0
# 1    NaN
# 2    3.0
# 3    4.5
# 4    0.0 (The False is converted to 0.0)
# dtype: float64


#-------------------------------------------------------------------------------------------------#
#---------------------------------------- 3. pd.Categorical() ------------------------------------#
#-------------------------------------------------------------------------------------------------#

'''
pd.Categorical() is used to create categorical data from a Series.

It allows you to specify categories and their order, 
which can be useful for memory efficiency and performance 
when dealing with columns that have a limited number of unique values.

It's an improved version of .astype('category') that provides more control over the categories.

Note: missing values like NaN are not included in the categories by default.
'''

###########################
## string gender example ##
###########################

s_gender = pd.Series(["M", "M", "F", "M", "LGBTQ", "F", "M", "F", "LGBTQ", "M"])

#---------------
## With ordered = True
#---------------

s_gender_categ = pd.Categorical(
    values = s_gender,
    categories = ["LGBTQ", "F", "M"],  # Specify the order of categories
    ordered = True  # Set to True if you want to treat categories as ordered
)

print(s_gender_categ)
# ['M', 'M', 'F', 'M', 'LGBTQ', 'F', 'M', 'F', 'LGBTQ', 'M']
# Categories (3, object): ['LGBTQ' < 'F' < 'M']

#---------------
## With ordered = False
#---------------

s_gender_categ = pd.Categorical(s_gender_categ, ordered = False)
print(s_gender_categ)
# ['M', 'M', 'F', 'M', 'LGBTQ', 'F', 'M', 'F', 'LGBTQ', 'M']
# Categories (3, object): ['LGBTQ', 'F', 'M']