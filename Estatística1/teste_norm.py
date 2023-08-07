from scipy import stats
from scipy.stats import norm, skewnorm
import matplotlib.pyplot as plt

#gera 1000 dados aletatórios em uma distribuição normal
dados = norm.rvs(size = 1000)
plt.hist(dados, bins= 20)
plt.title('Dados')
plt.show()

#gráfico para verificar se o gráfico tem distribuição normal
fig, ax = plt.subplots()
stats.probplot(dados, fit = True, plot = ax)
plt.show()

#teste de shapiro
#segundo elemento é a hipotese nula
print(stats.shapiro(dados))

#dados enviezados
dados2 = skewnorm.rvs(4, size = 1000)
#gera 1000 dados aletatórios em uma distribuição normal
plt.hist(dados2, bins= 20)
plt.title('Dados')
plt.show()

#gráfico para verificar se o gráfico tem distribuição normal
fig, ax = plt.subplots()
stats.probplot(dados2, fit = True, plot = ax)
plt.show()

#teste de shapiro
#segundo elemento é a hipotese nula
print(stats.shapiro(dados2))