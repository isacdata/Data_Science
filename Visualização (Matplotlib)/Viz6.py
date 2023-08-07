import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\13.Prática em Python\dados\trees.csv")
base  = pd.read_csv(path)

print(base.head())

#vert = mostrar na vertical, showfliers = mostrar outliers, noth= cortar  no meio, patch = preencher box
plt.boxplot(base.Volume, vert = False, showfliers = False, notch = True, patch_artist = True)
plt.title('Árvores')
plt.xlabel('Volume')
plt.show()

plt.boxplot(base)
plt.title('Árvores')
plt.xlabel('Volume')
plt.show()

plt.boxplot(base.Volume, vert = False)
plt.boxplot(base.Height, vert = False)
plt.boxplot(base.Girth, vert = False)
plt.title('Árvores')
plt.xlabel('Volume')
plt.show()