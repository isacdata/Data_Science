import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

path = open(r'C:\Users\isacn\OneDrive\Área de Trabalho\Python Projects\Regressão logística\Eleicao.csv')
base = pd.read_csv(path, sep =';')

print(base.head())
#visualização de gráficos com base em duas variáveis
#plt.scatter(base.DESPESAS, base.SITUACAO)
#plt.show()
print(base.describe())

#correlação coeficientes
#print(np.corrcoef(base.DESPESAS, base.SITUACAO))

X = base.iloc[:, 2].values
X = X[:, np.newaxis]#transforma X para formato de matriz adicionando um novo eixo
Y = base.iloc[:, 1].values

modelo  = LogisticRegression()
modelo.fit(X,Y)

print(modelo.coef_)
print(modelo.intercept_)

plt.scatter(X,Y)
#plt.show()

#geração de novos dados para a função sigmoide
X_teste = np.linspace(10,3000,100)
print(X_teste)

#implementação da função sigmoide
def model (x):
    return 1/(1 + np.exp(-x))

#geração de previsões variável r, e visualização de resultados
r = model(X_teste*modelo.coef_ + modelo.intercept_).ravel()

plt.plot(X_teste, r, color ='red')
plt.show()

#nova base com novos candidatos
path1 = open(r'C:\Users\isacn\OneDrive\Área de Trabalho\Python Projects\Regressão logística\NovosCandidatos.csv')
base1 = pd.read_csv(path1, sep =';')

#etl para matriz
despesas = base1.iloc[:, 1].values
despesas = despesas.reshape(-1,1)

#previsões baseadas na base anterior
print(modelo.predict(despesas))