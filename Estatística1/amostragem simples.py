import numpy as np 
import pandas as pd 

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\16.Prática em Python\dados\iris.csv")
base = pd.read_csv(path)
#mostra os 5 primeiros elementos
print(base.head())
#mostra a quantidade de linhas e colunas
print(base.shape)

#mudança da semente aleatória randômica para manter os resultados em várias execuções
np.random.seed(2345)
#150 amostras, de 0 a 1, com reposição, probabilidades equivalentes
amostra = np.random.choice(a = [0,1], size= 150, replace = True,
                           p = [0.7,0.3])
#verifica o atamanho da amostra
print(len(amostra))

#verifica o atamanho da amostra em 1
print(len(amostra[amostra ==1]))

#verifica o atamanho da amostra em 0
print(len(amostra[amostra ==0]))

base_final = base.loc[amostra==0]
print(base_final.shape)