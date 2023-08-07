import numpy as np 
import pandas as pd
from math import ceil

populacao = 150
amostra = 15

#arredonda número
k = ceil(populacao/amostra)
print(k)

#definição do valor randômico para incializar a amostra, iniciando em 1 até k+1
r = np.random.randint(low = 1, high = k+1, size =1)
print(r)

acumulador = r[0]
sorteados = []
for i in range(amostra):
    sorteados.append(acumulador)
    acumulador +=k
print(sorteados)

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\16.Prática em Python\dados\iris.csv")
base = pd.read_csv(path)
base_final = base.loc[sorteados]
print(base_final)