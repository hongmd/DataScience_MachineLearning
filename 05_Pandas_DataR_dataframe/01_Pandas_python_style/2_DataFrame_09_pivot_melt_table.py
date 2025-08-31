'''
Pivot, Melt and Cross-Table are powerful techniques allowing you to reshape

####################################

1. Pivot: long to wide
   + pd.pivot() || df.pivot()
   + pd.pivot_table() || df.pivot_table()

2. Melt: wide to long
   + pd.metl() || df.melt()
   + pd.wide_to_long()

3. Cross-Table
   + pd.crosstab()
'''

import pandas as pd
import numpy as np

#---------------------------------------------------------------------------------------------------------#
#----------------------------------------- 1. Pivot: long to wide ----------------------------------------#
#---------------------------------------------------------------------------------------------------------#

##############################
## Create example DataFrame ##
##############################

dates = pd.date_range('2024-01-01', periods=30) # 30 days
regions   = ['North', 'South', 'East', 'West']
products  = ['Widget', 'Gadget', 'Doohickey']

np.random.seed(42)
sales_df = pd.DataFrame(
    {
        'date'      : np.random.choice(dates, size=200),
        'region'    : np.random.choice(regions, size=200),
        'product'   : np.random.choice(products, size=200),
        'quantity'  : np.random.randint(1, 20, size=200),
        'unit_price': np.round(np.random.uniform(5, 50, size=200), 2)
    }
).assign(sales = lambda df: df.eval("quantity * unit_price")) # Add a column with the total sales amount

sales_df.head()
#         date region    product  quantity  unit_price   sales
# 0 2024-01-07   East     Gadget         5        6.19   30.95
# 1 2024-01-20  North     Widget        10       21.94  219.40
# 2 2024-01-29   East  Doohickey         5       41.47  207.35
# 3 2024-01-15   East     Widget         4       49.43  197.72
# 4 2024-01-11  North     Widget         2       11.77   23.54

#---------------------------------------------------------------------------------------------------------#
#------------------------------------------ 2. Melt: wide to long ----------------------------------------#
#---------------------------------------------------------------------------------------------------------#

##############################
## Create example DataFrame ##
##############################

n_patients = 8
patient_ids = [f"P{i:03d}" for i in range(1, n_patients+1)]

np.random.seed(42)
measurements_df = pd.DataFrame({
    'patient_id' : patient_ids,
    'age'        : np.random.randint(20, 80, size=n_patients),
    # Day‑specific columns (wide format)
    'BP_day1'    : np.random.randint(110, 150, size=n_patients), # BP = Blood Pressure
    'HR_day1'    : np.random.randint(60, 100, size=n_patients), # HR = Heart Rate
    'BP_day2'    : np.random.randint(110, 150, size=n_patients),
    'HR_day2'    : np.random.randint(60, 100, size=n_patients),
    'BP_day3'    : np.random.randint(110, 150, size=n_patients),
    'HR_day3'    : np.random.randint(60, 100, size=n_patients)
})

print(measurements_df)
#   patient_id  age  BP_day1  HR_day1  BP_day2  HR_day2  BP_day3  HR_day3
# 0       P001   58      128       62      142       62      134       67
# 1       P002   71      132       81      121       96      123       94
# 2       P003   48      120       61      131       66      118       73
# 3       P004   34      120       83      134       80      135       76
# 4       P005   62      133       89      136       68      111       95
# 5       P006   27      145       97      137       98      129       99
# 6       P007   40      149       61      125       77      137       63
# 7       P008   58      133       80      124       63      116       61


#---------------------------------------------------------------------------------------------------------#
#---------------------------------------------- 3. Cross-Table -------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

##############################
## Create example DataFrame ##
##############################

n_resp = 250

np.random.seed(42)
survey_df = pd.DataFrame({
    'respondent_id'   : range(1, n_resp+1),
    
    'gender'          : np.random.choice(['Male', 'Female', 'Other'], size=n_resp,
                                          p=[0.48, 0.48, 0.04]),

    'favorite_color'  : np.random.choice(['Red', 'Blue', 'Green', 'Yellow', 'Purple'],
                                          size=n_resp),

    'purchase_intent' : np.random.choice(['Definitely', 'Probably', 'Maybe', 'Unlikely', 'Never'], 
                                          size=n_resp,
                                         p=[0.15, 0.25, 0.30, 0.20, 0.10])
})

survey_df.head()
#    respondent_id  gender favorite_color purchase_intent
# 0              1    Male         Purple        Probably
# 1              2  Female         Purple        Unlikely
# 2              3  Female            Red           Never
# 3              4  Female          Green           Never
# 4              5    Male           Blue        Unlikely