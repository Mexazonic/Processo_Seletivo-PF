import pandas as pd
import os

columns = ["Film", "Genre"]
data = pd.read_csv('./movies.csv', usecols = columns)

flag = True
dict = {}
second_list = set()

for i in range(len(data)):
    dict[data.loc[i][0]] = data.loc[i][1]
  

while(flag):
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = input("Digite o nome do Filme: ")

    if (nome in dict):
        print("Encontrado!")
        second_list.add(dict[nome])
    
    next = input("Deseja Continuar?(S/N): ")
    flag = True if next.lower() == 's' else False 

os.system('cls' if os.name == 'nt' else 'clear')


if (len(second_list) > 0):
    print("=============Genders==============")
    print(*second_list, sep=', ')

else:
    print("No Genders")