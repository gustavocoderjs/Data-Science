

import numpy as np

dados = [10, 20, 30, 40, 50, 60, 70, 80, 90]

q1 = np.percentile(dados, 25)
q2 = np.percentile(dados, 50)  # Mediana
q3 = np.percentile(dados, 75)

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)

q1 = np.quantile(dados, 0.25)
q2 = np.quantile(dados, 0.50)
q3 = np.quantile(dados, 0.75)


print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
