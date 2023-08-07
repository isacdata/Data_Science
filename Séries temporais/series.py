import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
#registro de converters para matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

path = open(r'C:\Users\isacn\OneDrive\Área de Trabalho\Python Projects\Séries temporais\dados\AirPassengers.csv')
base = pd.read_csv(path)

def separa():
    print('\n===================================================================\n')

print(base.head())
separa()
#visualização do tipo de dados dos atributos
print(base.dtypes)
separa()

#conversão de atributos que estão no formato de string para o formato de data: ANO - MÊS

dateparse = lambda dates: datetime.strptime(dates, '%Y-%m')
print(base)
base = pd.read_csv(path, parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse)
print(base)
separa()