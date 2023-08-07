import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\13.Prática em Python\dados\dados.csv")
base  = pd.read_csv(path, sep =';')
print(base.head())

sns.histplot(base.loc[base].weight, kde = True).set_title('horsebean')
plt.show()
