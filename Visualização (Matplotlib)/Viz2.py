#historgramas

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\13.Prática em Python\dados\trees.csv")
base  = pd.read_csv(path)

plt.hist(base.iloc[:,1], bins = 6)

plt.show()

#hist = gerar histograma
#kde = gerar linha de densidade
#bins = número de colunas
#hist_kws = cor da borda

sns.kdeplot(base['Height'])

plt.show()

sns.histplot(base['Height'], kde = True)

plt.show()