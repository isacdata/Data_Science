import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\13.Prática em Python\dados\trees.csv")
base  = pd.read_csv(path)

sns.boxplot(base.Volume).set_title('Árvores')
plt.show()

sns.boxplot(base)
plt.show()