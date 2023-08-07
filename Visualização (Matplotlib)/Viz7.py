import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\13.Prática em Python\dados\insect.csv")
base  = pd.read_csv(path)

print(base.head())

#vert = mostrar na vertical, showfliers = mostrar outliers, noth= cortar  no meio, patch = preencher box
agrupado = base.groupby(['spray'])['count'].sum()
print(agrupado)
agrupado.plot.bar(color='gray')
plt.show()
agrupado.plot.bar(color=['blue', 'yellow', 'red', 'green', 'pink', 'orange'])
plt.show()
agrupado.plot.pie()
plt.show()
agrupado.plot.pie(legend = True)
plt.show()