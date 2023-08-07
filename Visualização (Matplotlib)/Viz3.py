#gráfico de dispersão

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\13.Prática em Python\dados\trees.csv")
base  = pd.read_csv(path)

#Girth = circunferência, color = cor dos elementos, facecolors = cor de fundo, marker = marcador

plt.scatter(base.Girth, base.Volume, color = 'blue', facecolors = 'none', marker = '*')
plt.title('Árvores')
plt.xlabel('Volume')
plt.ylabel('Circunferência')

plt.show()

#grafico em linha
plt.plot(base.Girth, base.Volume)
plt.title('Árvores')
plt.xlabel('Volume')
plt.ylabel('Circunferência')

plt.show()

#jitter afasta os dados, fit_reg = linha de tendencia
sns.regplot(data = base, x = 'Girth', y='Volume', x_jitter = 0.3, fit_reg = True)

plt.show()