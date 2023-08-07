import pandas as pd
import seaborn as srn
import statistics as sts
import matplotlib.pyplot as plt

#importar dados
data = open(r'C:\Users\isacn\OneDrive\Área de Trabalho\Python Projects\tratamento de dados\Churn.csv')
dataset = pd.read_csv(data, sep=";")

#nome das colunas
dataset.columns = ['Id', 'Score', 'Estado', 'Gênero', 'Idade', 'Patrimonio', 'Saldo', 'Produtos', 'TemCartCredito', 'Ativo', 'Salario', 'Saiu']

#funções
#separa partes do código
def separa():
    print('\n=============================================================\n')

#quantos valores vazios
def NAN():
    print('Valores NAN:')
    print(dataset.isnull().sum())

#descrição das colunas
def describe(n):
    print('Descrição:')
    print(dataset[n].describe())

def mediana(a):
    print('Mediana:',sts.median(dataset[a]))

#substitui valores pela mediana
def substitui(i):
    mediana = sts.median(dataset[i])
    dataset[i].fillna(mediana, inplace=True)

#substitui pela moda
def moda(i):
    moda = sts.mode(dataset[i])
    dataset[i].fillna(moda, inplace=True)

#descreve elementos de uma coluna
def agrupa(b):
    print(dataset.groupby([b]).size())

#contagem de valores NAN
separa()
NAN()

separa()

describe('Salario')

separa()
mediana("Salario")

separa()
substitui('Salario')
NAN()

separa()
moda("Gênero")
NAN()
agrupa("Gênero")

separa()
#padronização e troca
dataset.loc[dataset['Gênero']=='M', 'Gênero'] = 'Masculino'
dataset.loc[dataset['Gênero'].isin(['Fem', 'F']), 'Gênero'] = 'Feminino'

agrupa('Gênero')

separa()

describe('Idade')

separa()

dataset.loc[(dataset['Idade']<0) | (dataset['Idade']>120), 'Idade'] = mediana('Idade')

describe('Idade')

separa()

#mostra dados duplicados pela id
print(dataset[dataset.duplicated(['Id'],keep=False)])

separa()
#retira dados duplicados
dataset.drop_duplicates(subset='Id', keep='first', inplace=True)
#busca por dados duplicados para garantir processo
print(dataset[dataset.duplicated(['Id'],keep=False)])

separa()

agrupa('Estado')
#trocar outros estados pela moda, fora do domínio preestabelecido
dataset.loc[dataset['Estado'].isin(['RP', 'SP', 'TD']), 'Estado'] = moda('Estado')

separa()
agrupa('Estado')

separa()
desv = sts.stdev(dataset['Salario'])
print(desv)

separa()
#localizamos conjunto que esta muito acima do desvio
print(dataset.loc[dataset['Salario']>= 2*desv, 'Salario'])
#trocamos pela mediana 
dataset.loc[dataset['Salario']>= 2*desv, 'Salario'] = mediana('Salario')

separa()
print(dataset.head())
print(dataset.shape)
