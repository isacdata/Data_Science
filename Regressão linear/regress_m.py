import pandas as pd 
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python Projects\Regressão linear\mt_cars.csv")
base  = pd.read_csv(path)

print(base.shape)
print(base.head())

base = base.drop(['Unnamed: 0'], axis  = 1)

print(base.head())

#criação de X e Y
X = base.iloc[:, 2].values
Y = base.iloc[:, 0].values

correlacao = np.corrcoef(X, Y)
print(correlacao)

#mudança do formato de X
X = X.reshape(-1,1)

modelo  = LinearRegression()
modelo.fit(X, Y)

#print(modelo.intercept_)

#print(modelo.coef_)

#R2
#print(modelo.score(X, Y))

previsoes = modelo.predict(X)
print(previsoes)

#criação do modelo usando stats
#r ajustado r2
modelo_ajustado = sm.ols(formula = 'mpg ~ disp', data = base)
modelo_treinado = modelo_ajustado.fit()
print(modelo_treinado.summary())

plt.scatter(X, Y)
plt.plot(X, previsoes, color ='red')
plt.show()

print(modelo.predict([[200]]))


#regressão múltipla
X1 = base.iloc[:, 1:4].values
Y1 = base.iloc[:, 0].values

modelo2 = LinearRegression()
modelo2.fit(X1,Y1)

print(modelo2.score(X1,Y1))
modelo_ajustado2 = sm.ols(formula = 'mpg ~ cyl + disp + hp', data = base)
modelo_treinado2 = modelo_ajustado2.fit()
print(modelo_treinado2.summary())

#previsão de um novo registro
novo = np.array([4,200,100])
novo = novo.reshape(1,-1)
print(modelo2.predict(novo))


