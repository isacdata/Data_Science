import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\13.Prática em Python\dados\orchard.csv")
base  = pd.read_csv(path)
print(base.head())

#criação de gráfico 3d passando 3 atributos
figura = plt.figure()
#configura 1 dimensão em cada lado
eixo = figura.add_subplot(1,1,1, projection = '3d')
#define scatter
eixo.scatter(base.decrease, base.rowpos, base.colpos)
eixo.set_xlabel('decrease')
eixo.set_ylabel('rowpos')
eixo.set_zlabel('colpos')

plt.show()






