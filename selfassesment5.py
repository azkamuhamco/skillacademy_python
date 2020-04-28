''' Soal dari Skill Academy Ruangguru
    Course: Programming Foundation for Data Science
    Unduh file dataset csv di: https://tinyurl.com/assessmentrnpy 
    Coding from Azka Ramadhan (@mazkarindo). Selesai pada Kamis, 2 April 2020'''

import pandas as pd
df = pd.read_csv("/home/azka/Dataset_superstore_simple.csv")

'''5. Buatlah data frame bernama ‘yearly_sales’ yang berisi total sales, jumlah
customers, dan total profit tiap tahun. Tahun berapa profit tertinggi diperoleh?'''

df['year'] = pd.DatetimeIndex(df['order_date']).year
df_cust = df.groupby(["year"]).agg( {"customer_id": "nunique"}, )

df_sales = df.groupby(["year"]).agg( {"sales": "sum"}, )
df_profit = df.groupby(["year"]).agg( {"profit": "sum"}, )

df_merge = pd.merge(df_cust, df_sales, how="left", on="year")
yearly_sales = pd.merge(df_merge, df_profit, how="left", on="year")

yearly_sales.sort_values("profit", ascending = False, inplace = True)
yearly_sales = yearly_sales.reset_index()
yearly_sales
