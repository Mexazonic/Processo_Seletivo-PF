import pandas as pd
import random


def main():

    dataset = pd.read_csv('./oscar_age_male.csv', sep=',', index_col = False, skipinitialspace=True)
    dataset.set_index("Index", inplace=True)
    cellphone = []
    mapping = {}    

    for i in range(len(dataset.index)):
        cellphone.append(random_phone_num_generator(mapping,dataset["Name"][i+1])) 
    
    dataset = dataset.assign(Cellphone = cellphone)

    new_dataset = dataset[['Name','Cellphone', 'Age']]
    new_dataset.index.names = ['id']
    new_dataset = new_dataset.rename(columns ={'Name':'nome', 'Cellphone':'telefone','Age':'idade'})
    new_dataset.to_csv(r'./CSVExtract.csv', sep=';')
    
    #print(new_dataset)

def random_phone_num_generator(mapping,name):

    if(name in mapping): #Filtrando/Mapeando redundância dos dados
        return mapping[name]  
    
    ddd = str(random.randint(10, 99))
    first = str(random.randint(1, 9999)).zfill(4)
    last = (str(random.randint(1, 9998)).zfill(4))

    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))

    mapping[name] = str(ddd) + str(first) + str(last)
    number = str(ddd) + str(first) + str(last)

    return number

if __name__ == '__main__':
    main()