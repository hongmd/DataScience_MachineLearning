'''
Boolean Filtering or Boolean Indexing is a powerful technique in Pandas 
that allows you to filter data based on specific conditions. 

###############################

Flow of contents:

1. Single Condition Examples:
   + Logic Operators: >, <, >=, <=, .between(), ==, !=
   + .isin()
   + String Boolean: .str.contains(), .str.startswith(), .str.endswith(), ....
   + DateTime Boolean: .dt.is_month_start, .dt.is_month_end, ...

2. Negation of Condition: ~ (tilde) operator

3. Combine Multiple Conditions:
   + & (and),
   + | (or)
'''

import pandas as pd
import numpy as np

np.random.seed(42)
s1_nums = pd.Series(np.random.uniform(10, 20, 10)).round(2)

np.random.seed(24)
s2_nums = pd.Series(np.random.uniform(10, 20, 10)).round(2)

print(s1_nums)
# 0    13.75
# 1    19.51
# 2    17.32
# 3    15.99
# 4    11.56
# 5    11.56
# 6    10.58
# 7    18.66
# 8    16.01
# 9    17.08
# dtype: float64

print(s2_nums)
# 0    13.21
# 1    13.66
# 2    17.10
# 3    19.00
# 4    15.34
# 5    12.47
# 6    16.72
# 7    15.62
# 8    15.43
# 9    18.93
# dtype: float64


#----------------------------------------------------------------------------------------------------------------#
#----------------------------------------- 1. Single Condition Examples -----------------------------------------#
#----------------------------------------------------------------------------------------------------------------#

#######################################################
## Logic Operators: >, <, >=, <=, .between(), ==, != ##
#######################################################

#-------------
## > (greater than)
#-------------

print(s1_nums > 15)
# 0    False
# 1     True
# 2     True
# 3     True
# 4    False
# 5    False
# 6    False
# 7     True
# 8     True
# 9     True
# dtype: bool

print(s1_nums[s1_nums > 15]) # Retuns values greater than 15 (True)
# 1    19.51
# 2    17.32
# 3    15.99
# 7    18.66
# 8    16.01
# 9    17.08
# dtype: float64

print(s2_nums[s2_nums > s1_nums]) # Retuns values greater than corresponding values (same index) in s1_nums
# 3    19.00 (> 15.99)
# 4    15.34 (> 11.56)
# 5    12.47 (> 11.56)
# 6    16.72 (> 10.58)
# 9    18.93 (> 17.08)
# dtype: float64

#-------------
## < (less than)
#-------------

print(s1_nums[s1_nums < 13]) # Retuns values less than 13 (True)
# 4    11.56
# 5    11.56
# 6    10.58
# dtype: float64

print(s2_nums[s2_nums < s1_nums]) # Retuns values less than corresponding values (same index) in s1_nums
# 0    13.21
# 1    13.66
# 2    17.10
# 7    15.62
# 8    15.43
# dtype: float64

#-------------
## >= (greater than or equal to)
#-------------

print(s1_nums[s1_nums >= 15.99]) # Retuns values greater than or equal to 15.99 (True)
# 1    19.51
# 2    17.32
# 3    15.99
# 7    18.66
# 8    16.01
# 9    17.08
# dtype: float64

print(s2_nums[s2_nums >= s1_nums]) # Retuns values greater than or equal to corresponding values (same index) in s1_nums
# 3    19.00
# 4    15.34
# 5    12.47
# 6    16.72
# 9    18.93
# dtype: float64

#-------------
## <= (less than or equal to)
#-------------

print(s1_nums[s1_nums <= 11.56]) # Retuns values less than or equal to 13 (True)
# 4    11.56
# 5    11.56
# 6    10.58
# dtype: float64

print(s2_nums[s2_nums <= s1_nums]) # Retuns values less than or equal to corresponding values (same index) in s1_nums
# 0    13.21
# 1    13.66
# 2    17.10
# 7    15.62
# 8    15.43
# dtype: float64

#-------------
## .between()
#-------------
'''
inclusive = "both" (default): [left, right] or left <= x <= right
inclusive = "neither": (left, right) or left < x < right
inclusive = "left": [left, right) or left <= x < right
inclusive = "right": (left, right] or left < x <= right
'''

print(s1_nums[s1_nums.between(10, 15.99)]) # Retuns values between 10 and 15.99 (both inclusive)
# 0    13.75
# 3    15.99
# 4    11.56
# 5    11.56
# 6    10.58
# dtype: float64

print(s1_nums[s1_nums.between(10, 15.99, inclusive = "left")]) # Retuns values between 15.99 (left inclusive)
# 0    13.75
# 4    11.56
# 5    11.56
# 6    10.58
# dtype: float64
'''The value 15.99 is excluded because the right endpoint is not inclusive.'''

#-------------
## == (equal to)
#-------------

print(s1_nums[s1_nums == 11.56]) # Retuns values equal to 11.56 (True)
# 4    11.56
# 5    11.56
# dtype: float64

print(s2_nums[s2_nums == s1_nums]) # Retuns values equal to corresponding values (same index) in s1_nums
# Series([], dtype: float64)

#-------------
## != (not equal to)
#-------------

print(s1_nums[s1_nums != 11.56]) # Retuns values not equal to 11.56 (True)
# 0    13.75
# 1    19.51
# 2    17.32
# 3    15.99
# 6    10.58
# 7    18.66
# 8    16.01
# 9    17.08
# dtype: float64

print(s2_nums[s2_nums != s1_nums]) # Retuns values not equal to corresponding values (same index) in s1_nums
# 0    13.21
# 1    13.66
# 2    17.10
# 3    19.00
# 4    15.34
# 5    12.47
# 6    16.72
# 7    15.62
# 8    15.43
# 9    18.93
# dtype: float64
'''All values are returned because none of the values in s2_nums are equal to the corresponding values in s1_nums.'''
