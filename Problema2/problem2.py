import pandas as pd

data = pd.read_csv('./CSVExtract.csv', sep=';', index_col = False, skipinitialspace=True)
result = data.sort_values(by=['nome', 'id'])

print(result.to_string(index=False))

"""
#Lista com nomes em ordem lexigráfica 
reg_list = result.values.tolist() 
for tuple in reg_list:
    print(tuple[1]) 
"""