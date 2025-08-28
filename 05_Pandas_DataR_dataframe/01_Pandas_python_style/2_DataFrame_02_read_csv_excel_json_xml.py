'''
Pandas offers many functions to read data from various file formats into DataFrames.

Flow of contents:
1. pd.read_csv() - Read CSV files
2. pd.read_excel() - Read Excel files
3. pd.read_json() - Read JSON files
4. pd.read_xml() - Read XML files
'''

import pandas as pd

#---------------------------------------------------------------------------------------------------------#
#----------------------------------------- 1. pd.read_csv() ----------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

'''
read_csv() is the most commonly used pandas I/O function, designed to read CSV files into DataFrames. 
It supports over 50 parameters for comprehensive data control.

File parameters:
+ filepath_or_buffer: Accepts file paths, URLs, or file-like objects
+ sep/delimiter: Field separator (default: ',')
+ encoding: Text encoding (utf-8, latin-1, etc.)
+ compression: Automatic detection ('infer') or specific formats ('gzip', 'bz2', 'zip')

Data Structure Control parameters:
+ header: Row number(s) for column names ('infer', int, list, None)
+ names: Custom column names list
+ index_col: Column(s) to use as row labels
+ usecols: Subset of columns to return

Data Type Management
+ dtype: Specify data types for columns
+ converters: Custom functions for value conversion
+ parse_dates: Parse date columns automatically
'''