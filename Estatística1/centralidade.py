import numpy as np
from scipy import stats

jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]
print(np.mean(jogadores))
print(np.median(jogadores))

quartis = np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1 ])
print(quartis)

print(np.std(jogadores, ddof=1))

print(stats.describe(jogadores))
