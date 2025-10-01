'''
1. pivot_wider: dr.pivot_wider()
   + basig usage
   + dr.pivot_wider(values_fill = 0)
   + dr.pivot_wider(values_from = [many_cols], names_sep = "_")
   + dr.pivot_wider(values_fn = ...)
   
2. pivot_longer: dr.pivot_longer()

3. crosstab: dr.table()
'''

import datar.all as dr
from datar import f
import pandas as pd
import numpy as np

# Suppress all warnings
import warnings
warnings.filterwarnings("ignore")


#---------------------------------------------------------------------------------------------------------#
#------------------------------------------ 1. dr.pivot_wider() ------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

########################
## Create sample data ##
########################

'''
The dr.pivot_wider() converts unique values from one column into multiple columns in the DataFrame.
=> Results in a wider DataFrame than the original.

NOTE: if the chosen "index" column has duplicates => RAISE ERROR
'''

dates = pd.date_range('2024-01-01', periods=30) # 30 days
regions   = ['North', 'South', 'East', 'West']
products  = ['Widget', 'Gadget', 'Doohickey']

np.random.seed(42)
df_sales = pd.DataFrame(
    {   'ID'        : range(1, 201),
        'date'      : np.random.choice(dates, size=200),
        'region'    : np.random.choice(regions, size=200),
        'product'   : np.random.choice(products, size=200),
        'quantity'  : np.random.randint(1, 20, size=200),
        'unit_price': np.round(np.random.uniform(5, 50, size=200), 2)
    }
).assign(sales = lambda df: df.eval("quantity * unit_price")) # Add a column with the total sales amount

df_sales.head()
#    ID       date region    product  quantity  unit_price   sales
# 0   1 2024-01-07   East     Gadget         5        6.19   30.95
# 1   2 2024-01-20  North     Widget        10       21.94  219.40
# 2   3 2024-01-29   East  Doohickey         5       41.47  207.35
# 3   4 2024-01-15   East     Widget         4       49.43  197.72
# 4   5 2024-01-11  North     Widget         2       11.77   23.54

##################################
## dr.pivot_wider() basic usage ##
##################################

print(
    df_sales 
    >> dr.pivot_wider(
        names_from = f.region, 
        values_from = f.sales
        )
    >> dr.slice_head(n = 5)
)
#        ID             date    product  quantity  unit_price      East     North     South      West
#   <int64> <datetime64[ns]>   <object>   <int64>   <float64> <float64> <float64> <float64> <float64>
# 0       1       2024-01-07     Gadget         5        6.19     30.95       NaN       NaN       NaN
# 1       2       2024-01-20     Widget        10       21.94       NaN    219.40       NaN       NaN
# 2       3       2024-01-29  Doohickey         5       41.47    207.35       NaN       NaN       NaN
# 3       4       2024-01-15     Widget         4       49.43    197.72       NaN       NaN       NaN
# 4       5       2024-01-11     Widget         2       11.77       NaN     23.54       NaN       NaN

#####################################
## dr.pivot_wider(values_fill = 0) ##
#####################################

print(
    df_sales  
    >> dr.pivot_wider(
            names_from = f.region, 
            values_from = f.sales,
            values_fill = 0 # Fill NaN with 0
        )
    >> dr.slice_head(n = 5)
)
#        ID             date    product  quantity  unit_price      East     North     South      West
#   <int64> <datetime64[ns]>   <object>   <int64>   <float64> <float64> <float64> <float64> <float64>
# 0       1       2024-01-07     Gadget         5        6.19     30.95      0.00       0.0       0.0
# 1       2       2024-01-20     Widget        10       21.94      0.00    219.40       0.0       0.0
# 2       3       2024-01-29  Doohickey         5       41.47    207.35      0.00       0.0       0.0
# 3       4       2024-01-15     Widget         4       49.43    197.72      0.00       0.0       0.0
# 4       5       2024-01-11     Widget         2       11.77      0.00     23.54       0.0       0.0

################################################################
## dr.pivot_wider(values_from = [many_cols], names_sep = "_") ##
################################################################

print(
    df_sales  
    >> dr.pivot_wider(
            names_from = f.region, 
            values_from = [f.sales, f.quantity], # Pivot multiple columns
            names_sep = "_", # Separator between the new column names
            values_fill = 0 # Fill NaN with 0
        )
    >> dr.slice_head(n = 5)
)
#        ID             date    product  unit_price       sales_East  sales_North  sales_South  sales_West
#   <int64> <datetime64[ns]>   <object>   <float64>  ...   <float64>    <float64>    <float64>   <float64>
# 0       1       2024-01-07     Gadget        6.19  ...       30.95         0.00          0.0         0.0
# 1       2       2024-01-20     Widget       21.94  ...        0.00       219.40          0.0         0.0
# 2       3       2024-01-29  Doohickey       41.47  ...      207.35         0.00          0.0         0.0
# 3       4       2024-01-15     Widget       49.43  ...      197.72         0.00          0.0         0.0
# 4       5       2024-01-11     Widget       11.77  ...        0.00        23.54          0.0         0.0

#####################################
## dr.pivot_wider(values_fn = ...) ##
#####################################
'''
values_fn: function to aggregate values 
           if there are multiple entries for the same index/column combination.
           (e.g., sum, mean, len, etc.)
'''

print(
    df_sales
    >> dr.select(f.product, f.region, f.sales) # Select only relevant columns
    >> dr.pivot_wider(
            names_from = f.product, 
            values_from = f.sales,
            values_fill = 0, # Fill NaN with 0
            values_fn = np.mean # Aggregate by sum if there are duplicates
        )
)
#     region   Doohickey      Gadget      Widget
#   <object>   <float64>   <float64>   <float64>
# 0     East  179.994000  283.253750  237.328889
# 1    North  248.782857  290.524737  239.141429
# 2    South  284.672000  183.286000  244.672500
# 3     West  256.096111  209.636957  409.786818