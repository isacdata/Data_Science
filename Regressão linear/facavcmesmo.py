import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python Projects\Regressão linear\slr12.csv")
base  = pd.read_csv(path, sep  = ';')

print(base.shape)

print(base.head())

X = base.iloc[:, 0].values
Y = base.iloc[:, 1].values

X = X.reshape(-1,1)

modelo_ajustado = sm.ols(formula='FrqAnual ~ CusInic', data = base)
modelo_treinado = modelo_ajustado.fit()
print(modelo_treinado.summary())

modelo = LinearRegression()
modelo.fit(X,Y)
previsoes = modelo.predict(X)

plt.scatter(X, Y)
plt.plot(X, previsoes, color = 'red')
plt.show()

print(modelo.predict([[5]]))