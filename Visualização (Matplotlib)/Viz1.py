#histograma simples

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\13.Prática em Python\dados\trees.csv")
base  = pd.read_csv(path)

#print(base.shape)
#print(base.head())

#histograma(base.iloc pega coluna de altura com 6 eixos)
h= np.histogram(base.iloc[:], bins=6)

#visualização do histograma
plt.hist(base.iloc[:,1], bins = 6)
plt.show()