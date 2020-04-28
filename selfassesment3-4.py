''' Soal dari Skill Academy Ruangguru
    Course: Programming Foundation for Data Science
    Unduh file dataset csv di: https://tinyurl.com/assessmentrnpy 
    Coding from Azka Muhammad Al Fisyahri (@azkamuhamco). Selesai pada Kamis, 2 April 2020'''

import pandas as pd
df = pd.read_csv("/home/azka/Dataset_superstore_simple.csv")

'3. Berapa banyak order yang menghasilkan profit negatif (rugi)?'
no_3 = df.groupby('order_id').agg( {"profit": "sum"}, )
no_3.query('profit < 0', inplace = True)
no_3 = no_3.reset_index()
no_3.count()

'''4. Antara 3 customer_id ini, mana yang total sales-nya paling banyak: JE-16165,
KH-16510, AD-10180?'''
no_4 = df.query(
    'customer_id == "JE-16165" | customer_id == "KH-16510" | customer_id== "AD-10180"', inplace = True)
no_4 = df.groupby('customer_id').agg( {"sales": "sum"}, )
no_4.sort_values("sales", axis = 0, ascending = False, inplace = True, na_position ='last') 
no_4 = no_4.reset_index()
no_4
