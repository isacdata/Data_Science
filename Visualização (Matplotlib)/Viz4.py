import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\13.Prática em Python\dados\co2.csv")
base  = pd.read_csv(path)

print(base.head())

#define x e y no gráfico
x = base.conc
y = base.uptake

#retorna valores únicos do atributo treatment
unicos = list(set(base.Treatment))

print(unicos)

#percorre cada tipo de tratamento e cria um gráfico de dispersão
for i in range(len(unicos)):
    indice = base.Treatment == unicos[i]
    plt.scatter(x[indice], y[indice],label = unicos[i])
plt.legend(loc = 'lower right')
plt.xlabel('Conc')
plt.ylabel('Uptake')

plt.show()