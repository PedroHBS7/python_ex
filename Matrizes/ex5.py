# Exercício 5
import numpy as np

matriz = np.array([
    [42, 17, 85],
    [33, 61, 29],
    [74, 50, 13]
])

print("Matriz original:")
print(matriz)

matriz = np.zeros(matriz.shape, dtype=int)

print("\nMatriz final (zerada):")
print(matriz)
