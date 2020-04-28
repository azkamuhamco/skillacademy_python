''' Soal dari Skill Academy Ruangguru
    Course: Programming Foundation for Data Science
    Unduh file dataset csv di: https://tinyurl.com/assessmentrnpy 
    Coding from Azka Muhammad Al Fisyahri (@azkamuhamco). Selesai pada Kamis, 2 April 2020'''   
    
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

df = pd.read_csv("/home/azka/Dataset_superstore_simple.csv", parse_dates=["order_date"])

'''Buatlah barchart yang berisi total profit dari 10 customer dengan total sales
tertinggi di tahun 2015!'''

df.query('order_date >= "2015-01-01" & order_date < "2016-01-01"', inplace = True)
df1=pd.pivot_table(df, index=['customer_id'],values=['profit', 'sales'],aggfunc=np.sum)
df1.sort_values("sales", axis = 0, ascending = False, inplace = True, na_position ='last')

df2=df1.reset_index().head(n=10)
df2.sort_values("customer_id", axis = 0, ascending = True, inplace = True, na_position ='last')

fig = px.bar(df2, x='customer_id', y='profit')
fig.show()
