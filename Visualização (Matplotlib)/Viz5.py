import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\13.Prática em Python\dados\trees.csv")
base  = pd.read_csv(path)

print(base.head())
'''
plt.scatter(base.Girth, base.Volume)
plt.show()
plt.scatter(base.Girth, base.Height)
plt.show()
plt.scatter(base.Height, base.Volume)
plt.show()
plt.hist(base.Volume)
plt.show()
'''
plt.figure(1)
plt.subplot(2,2,1)
plt.scatter(base.Girth, base.Volume)
plt.subplot(2,2,2)
plt.scatter(base.Girth, base.Height)
plt.subplot(2,2,3)
plt.scatter(base.Height, base.Volume, marker = '*')
plt.subplot(2,2,4)
plt.hist(base.Volume)
plt.show()