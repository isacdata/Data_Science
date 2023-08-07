import pandas as pd 
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from yellowbrick.regressor import ResidualsPlot

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python Projects\Regressão linear\cars.csv")
base  = pd.read_csv(path)

print(base.shape)
print(base.head())

base = base.drop(['Unnamed: 0'], axis  = 1)

print(base.head())

#X = variavel independente e Y = variavel dependente
X = base.iloc[:, 1].values
Y = base.iloc[:, 0].values

print(X)

correlacao  = np.corrcoef(X,Y)
print(correlacao)

#formato de matriz com uma coluna a mais 
X = X.reshape(-1,1)
#Criação de modelo e treinamento(fit é a execução do treinamento)
modelo  = LinearRegression()
modelo.fit(X,Y)

#viz dos coeficiente, onde a linha vai enconstar no y0
print(modelo.intercept_)

#inclinação, o quanto cresce por dist
print(modelo.coef_)

#graphs
plt.scatter(X,Y)
plt.plot(X, modelo.predict(X), color = 'red')
plt.show()

#previsão a com calculos para 22 ´pés
print(modelo.intercept_ + modelo.coef_*22)

#jeito smart
modelo.predict([[22]])

#graph 
visualizador  = ResidualsPlot(modelo)
visualizador.fit(X,Y)
print(visualizador.poof())