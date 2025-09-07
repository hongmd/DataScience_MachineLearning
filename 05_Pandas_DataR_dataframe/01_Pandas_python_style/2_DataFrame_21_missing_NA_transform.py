'''
1. Detect missing values:
  + df.isna() or df.isnull(): Returns a DataFrame of the same shape as df, with True for missing values
  + df.isna().sum() or df.isnull().sum(): Returns the count of missing values in each column
  + df.info(): Provides a summary of the DataFrame, including non-null counts

2. Detect non-missing values:
  + df.notna() or df.notnull(): Returns a DataFrame of the same shape as df, with True for non-missing values
  + df.notna().sum() or df.notnull().sum(): Returns the count of non-missing values in each column

3. Drop missing values:
  + df.dropna(): Returns a DataFrame with rows containing any missing values removed
  + df.dropna(axis=...)
  + df.dropna(how=...)
  + df.dropna(thresh=...)
  + df.dropna(subset=...)

4. Fill missing values:
  + df.fillna(value): Returns a DataFrame with missing values filled with the specified value
  + df.fillna({dictionary}): Fill different columns with different values
  + df.fillna(df.mean()): Fill missing values with the mean of each column
  + df.fillna(method=..., limit=...): Fill missing values using a specified method (e.g., 'ffill', 'bfill')

5. Interpolate missing values:
  + df.interpolate(axis=...): linear interpolation
  + df.interpolate(method = "polynomial", order = n): polynomial interpolation of order n
  + df.interpolate(method = "spline", order = n): spline interpolation of order n
  + df.interpolate(method = "time"): time-based interpolation (requires a datetime index)
  + df.interpolate(method = "nearest"): nearest neighbor interpolation

6. Conditional filling: df['C'] = np.where(df['C'].isna(), df['A'] + df['B'], df['C'])

7. Group-based filling, transform
  + df_grouped = df.groupby('category').transform(lambda x: x.fillna(x.mean()))
'''

import pandas as pd
import numpy as np

df_mkt = (
    pd.read_csv(
        filepath_or_buffer = "05_Pandas_DataR_dataframe/data/marketing_data.csv",
        dtype = {"week": "category", "Year": "category"}
    )
    .pipe(
        lambda df: df.set_axis(
            df.columns.str.lower().str.strip().str.replace(r"[^a-zA-Z]", "_", regex = True), 
            axis = 1
        )
    )
)

print(df_mkt.info())
# RangeIndex: 156 entries, 0 to 155
# Data columns (total 26 columns):
#  #   Column                     Non-Null Count  Dtype   
# ---  ------                     --------------  -----   
#  0   week                       156 non-null    category
#  1   year                       156 non-null    category
#  2   market_share               156 non-null    float64 
#  3   av_price_per_kg            156 non-null    float64 
#  4   non_promo_price_per_kg     156 non-null    float64 
#  5   promo_vol_share            156 non-null    float64 
#  6   total_weigh                156 non-null    int64   
#  7   share_of_ean_weigh         156 non-null    float64 
#  8   avg_price_vs_plb           156 non-null    float64 
#  9   non_promo_price_vs_plb     156 non-null    float64 
#  10  promo_vol_sh_index_vs_plb  156 non-null    float64 
#  11  total_cm_shelf             156 non-null    float64 
#  12  shelf_share                156 non-null    float64 
#  13  top_of_mind                123 non-null    float64 
#  14  spontaneous                123 non-null    float64 
#  15  aided                      123 non-null    float64 
#  16  penetration                123 non-null    float64 
#  17  competitor                 111 non-null    float64 
#  18  grp_radio                  14 non-null     float64 
#  19  reach_radio                14 non-null     float64 
#  20  grp_tv                     52 non-null     float64 
#  21  reach_tv                   52 non-null     float64 
#  22  reach_cinema               18 non-null     float64 
#  23  grp_outdoor                1 non-null      float64 
#  24  grp_print                  22 non-null     float64 
#  25  share_of_spend             116 non-null    float64 
# dtypes: category(2), float64(23), int64(1)
# memory usage: 32.2 KB