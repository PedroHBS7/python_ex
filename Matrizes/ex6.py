# Exercício 6
import numpy as np

matriz = np.array([
    [0, 3, 7, 2],
    [5, 1, 4, 8],
    [9, 6, 0, 3],
    [2, 4, 1, 7]
])

print("Matriz original:")
print(matriz)

matriz = np.ones(matriz.shape, dtype=int)

print("\nMatriz final (todos os sensores ativos = 1):")
print(matriz)
