import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statistics as sts

#separa partes do código
def separa():
    print('\n=============================================================\n')

path = open(r'C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\10.Prática em Python\dados\tempo.csv') 
dataset = pd.read_csv(path, sep=';')

print(dataset.head())
separa()
print(dataset.isnull().sum())
def moda(i):
    moda = sts.mode(dataset[i])
    dataset[i].fillna(moda, inplace=True)

def mediana(i):
    mediana = sts.median(dataset[i])
    dataset[i].fillna(mediana, inplace=True)

#dataset.loc[dataset["Umidade"], "Umidade"] = mediana('Umidade')
#dataset.loc[dataset["Vento"], "Vento"] = moda('Vento')

mediana('Umidade')
moda('Vento')

separa()
print(dataset.isnull().sum())
