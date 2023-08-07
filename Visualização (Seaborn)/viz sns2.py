import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

path = open(r"C:\Users\isacn\OneDrive\Área de Trabalho\Python\FormacaoCD\13.Prática em Python\dados\chicken.csv")
base  = pd.read_csv(path)

agrupado = base.groupby(['feed'])['weight'].sum()
print(agrupado)
'''
sns.histplot(base.loc[base['feed'] == 'horsebean'].weight, kde = True).set_title('horsebean')
plt.show()
sns.histplot(base.loc[base['feed'] == 'casein'].weight, kde = True).set_title('casein')
plt.show()
sns.histplot(base.loc[base['feed'] == 'linseed'].weight, kde = True).set_title('linseed')
plt.show()
sns.histplot(base.loc[base['feed'] == 'meatmeal'].weight, kde = True).set_title('meatmeal')
plt.show()
sns.histplot(base.loc[base['feed'] == 'soybean'].weight, kde = True).set_title('soybean')
plt.show()
sns.histplot(base.loc[base['feed'] == 'sunflower'].weight, kde = True).set_title('sunflower')
plt.show()
'''
plt.figure()
plt.subplot(3,2,1)
sns.histplot(base.loc[base['feed'] == 'horsebean'].weight, kde = True).set_title('horsebean')
plt.subplot(3,2,2)
sns.histplot(base.loc[base['feed'] == 'casein'].weight, kde = True).set_title('casein')
plt.subplot(3,2,3)
sns.histplot(base.loc[base['feed'] == 'linseed'].weight, kde = True).set_title('linseed')
plt.subplot(3,2,4)
sns.histplot(base.loc[base['feed'] == 'meatmeal'].weight, kde = True).set_title('meatmeal')
plt.subplot(3,2,5)
sns.histplot(base.loc[base['feed'] == 'soybean'].weight, kde = True).set_title('soybean')
plt.subplot(3,2,6)
sns.histplot(base.loc[base['feed'] == 'sunflower'].weight, kde = True).set_title('sunflower')
#ajusta posições evitando sobreposição
plt.tight_layout()
plt.show()

