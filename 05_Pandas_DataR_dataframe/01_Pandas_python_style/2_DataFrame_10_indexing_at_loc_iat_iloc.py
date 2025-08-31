'''
1. Indexing with df.at and df.loc:
   + df.at: Access a single value for a row/column label pair.
   + df.loc: Access a group of rows and columns by labels or a boolean array.

2. Indexing with df.iat and df.iloc:
   + df.iat: Access a single value for a row/column pair by integer position.
   + df.iloc: Access a group of rows and columns by integer position(s).
'''

import pandas as pd

df_emp = pd.read_csv("05_Pandas_DataR_dataframe/data/emp.csv")
print(df_emp)
#    id      name  salary  start_date        dept
# 0   1      Rick  623.30  2012-01-01          IT
# 1   2       Dan  515.20  2013-09-23  Operations
# 2   3  Michelle  611.00  2014-11-15          IT
# 3   4      Ryan  729.00  2014-05-11          HR
# 4   5      Gary  843.25  2015-03-27     Finance
# 5   6      Nina  578.00  2013-05-21          IT
# 6   7     Simon  632.80  2013-07-30  Operations
# 7   8      Guru  722.50  2014-06-17     Finance

########################################################

df_set_id = df_emp.set_index("id", drop = True, inplace = False)
print(df_set_id)
#         name  salary  start_date        dept
# id                                          
# 1       Rick  623.30  2012-01-01          IT
# 2        Dan  515.20  2013-09-23  Operations
# 3   Michelle  611.00  2014-11-15          IT
# 4       Ryan  729.00  2014-05-11          HR
# 5       Gary  843.25  2015-03-27     Finance
# 6       Nina  578.00  2013-05-21          IT
# 7      Simon  632.80  2013-07-30  Operations
# 8       Guru  722.50  2014-06-17     Finance

########################################################

df_indexed = df_emp.set_axis(
    labels = [f"row_{i}" for i in df_emp["id"]],
    axis = 0,
    copy = True
)
print(df_indexed)
#        id      name  salary  start_date        dept
# row_1   1      Rick  623.30  2012-01-01          IT
# row_2   2       Dan  515.20  2013-09-23  Operations
# row_3   3  Michelle  611.00  2014-11-15          IT
# row_4   4      Ryan  729.00  2014-05-11          HR
# row_5   5      Gary  843.25  2015-03-27     Finance
# row_6   6      Nina  578.00  2013-05-21          IT
# row_7   7     Simon  632.80  2013-07-30  Operations
# row_8   8      Guru  722.50  2014-06-17     Finance