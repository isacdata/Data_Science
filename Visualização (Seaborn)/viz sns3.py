import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\13.Prática em Python\dados\co2.csv")
base  = pd.read_csv(path)
print(base.head())

#gráfico de dispersão utilizando conc uptake e agrupamento pelo type
sns.scatterplot(x = base.conc, y = base.uptake, hue = base.Type)
plt.show()

q = base.loc[base['Type']=='Quebec']
m = base.loc[base['Type']=='Mississippi']

plt.figure()
plt.subplot(1,2,1)
sns.scatterplot(x = q.conc, y = q.uptake, hue = base.Type).set_title('Quebec')
plt.subplot(1,2,2)
sns.scatterplot(x = m.conc, y = m.uptake, hue = base.Type).set_title('Mississippi')

plt.show()

ch = base.loc[base['Treatment']=='chilled']
nc = base.loc[base['Treatment']=='nonchilled']

plt.figure()
plt.subplot(1,2,1)
sns.scatterplot(x = ch.conc, y = ch.uptake, hue = base.Type).set_title('Chilled')
plt.subplot(1,2,2)
sns.scatterplot(x = nc.conc, y = nc.uptake, hue = base.Type).set_title('Nonchilled')

plt.show()

path2 = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\13.Prática em Python\dados\esoph.csv")
base2  = pd.read_csv(path2)
print(base2.head())

sns.catplot(x = 'alcgp', y='ncontrols', data = base2, jitter = False)
plt.show()

sns.catplot(x = 'alcgp', y='ncontrols', data = base2, jitter = True)
plt.show()

sns.catplot(x = 'alcgp', y='ncontrols', data = base2, col = 'tobgp')
plt.tight_layout()
plt.show()

