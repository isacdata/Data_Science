import pandas as pd
from sklearn.model_selection import train_test_split

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\16.Prática em Python\dados\iris.csv")
base = pd.read_csv(path)

print(base['class'].value_counts())

# iris.iloc[:, 0:4]: buscamos somente os atributos previsores, ou seja, os dados sobre pétala e sétala da planta
# iris.iloc[:, 4]: buscamos somente a classe, que é a espécie da planta (setosa, virginica ou versicolor)
# test_size: selecionamos 50% da base de dados, que serão copiados para as variáveis X e Y. Essa função retorna 4 valores,
# porém, vamos usar somente os 50% da base de dados e por isso colocamos "_" para os outros valores
# stratify: para retornar a amostra baseada na classe
X, _, y, _ = train_test_split(base.iloc[:, 0:4], base.iloc[:, 4], test_size=0.5, stratify = base.iloc[:,4]) 
print(y.value_counts())

path1 = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\16.Prática em Python\dados\infert.csv")
base1 = pd.read_csv(path1)

print(base1['education'].value_counts())

X1, _, y1, _ = train_test_split(base1.iloc[:, 2:9], base1.iloc[:, 1], test_size = 0.6, stratify = base1.iloc[:, 1])
print(y1.value_counts())

