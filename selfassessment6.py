''' Soal dari Skill Academy Ruangguru
    Course: Programming Foundation for Data Science
    Unduh file dataset csv di: https://tinyurl.com/assessmentrnpy 
    Coding from Azka Ramadhan (@mazkarindo). Selesai pada Kamis, 2 April 2020'''   
    
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

df = pd.read_csv("/home/azka/Dataset_superstore_simple.csv", parse_dates=["order_date"])

'''Buatlah scatterplot antara sales dan profit untuk data di tahun 2014-2015 saja,
bedakan warnanya antara tahun 2014 dan tahun 2015. Beri judul ‘Sales vs Profit 2014-2015’!'''

df.query('order_date >= "2014-01-01" & order_date < "2016-01-01"', inplace = True)
df["Tahun"] = df.order_date.dt.strftime("%Y")

df1=pd.pivot_table(df, index=['order_date', 'Tahun'],values=['sales','profit'],aggfunc=np.sum)
df1=df1.reset_index()

no_6 = px.scatter(df1, x="sales", y="profit", trendline="ols", color="Tahun", 
                   title="Sales vs Profit 2014-2015")
no_6.show()
