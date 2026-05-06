# Exercício 4
import numpy as np

matriz = np.array([
    [1, 2],
    [3, 4]
])

print("Matriz original:")
print(matriz)

temp = matriz[0].copy()
matriz[0] = matriz[1]
matriz[1] = temp

print("\nMatriz após troca das linhas:")
print(matriz)
