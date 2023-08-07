import pandas as pd
import seaborn as srn
import statistics as sts
import matplotlib.pyplot as plt
#importar dados
data = open(r'C:\Users\isacn\OneDrive\Área de Trabalho\Python Projects\tratamento de dados\Churn.csv')
dataset = pd.read_csv(data, sep=";")

#nome das colunas
dataset.columns = ['id', 'Score', 'Estado', 'Gênero', 'Idade', 'Patrimonio', 'Saldo', 'Produtos', 'TemCartCredito', 'Ativo', 'Salario', 'Saiu']
#explorar categoria 
#estado 

'''for i in dataset.columns:
    agrupado = dataset.groupby([i]).size()
    agrupado.plot.bar(color='gray')
    plt.show()'''

#visualizar
#print(dataset.head(10))

#descreve situação de uma determinada coluna
print(dataset['Score'].describe())
srn.boxplot(dataset["Score"]).set_title("Score")
plt.show()

#Histograma
srn.distplot(dataset["Score"]).set_title("Score")
plt.show()

#descreve situação de uma determinada coluna
print(dataset['Saldo'].describe())
srn.boxplot(dataset["Saldo"]).set_title("Saldo")
plt.show()

#Histograma
srn.distplot(dataset["Saldo"]).set_title("Saldo")
plt.show()

