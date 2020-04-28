''' Soal dari Skill Academy Ruangguru
    Course: Programming Foundation for Data Science
    Unduh file dataset csv di: https://tinyurl.com/assessmentrnpy 
    Coding from Azka Muhammad Al Fisyahri (@azkamuhamco). Selesai pada Kamis, 2 April 2020'''

import pandas as pd
df = pd.read_csv("/home/azka/Dataset_superstore_simple.csv")

'1. Carilah customer_id yang memiliki sales paling besar!'
no_1 = df.groupby(["customer_id"]).agg({ 	"sales": "sum", })
no_1.sort_values("sales", axis = 0, ascending = False, inplace = True, na_position ='last')
no_1 = no_1.reset_index()
no_1

'''2. Sub-category apa saja yang ada di dalam category Office Supplies,
dan masing-masing berapa banyak total profitnya?'''
no_2 = df.query('category == "Office Supplies"', inplace = True)
no_2 = df.groupby(["sub_category"]).agg({ 	"profit": "sum", })
no_2.sort_values("sub_category", axis = 0, ascending = True, inplace = True, na_position ='last')
no_2 = no_2.reset_index()
no_2
