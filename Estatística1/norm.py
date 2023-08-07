from scipy.stats import norm
#qual a probabilidade de tirar objeto é menor que 6 quilos com média 8 e desvio 2
print(norm.cdf(6, 8, 2))
#maior que
print(norm.sf(6, 8, 2))
print(1 - norm.cdf(6, 8, 2))

#qual a probabilidade de retirar um objeto menor que 6 e maior que 10
print(norm.cdf(6,8,2) + norm.sf(10,8,2))

#qual a probabilidade de retirar um objeto menor que 10 e maior que 8
print(norm.cdf(10,8,2)- norm.sf(8,8,2))