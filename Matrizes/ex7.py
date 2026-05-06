# Exercício 7
import numpy as np

matriz = np.array([
    [10, 99, 30, 40, 50],
    [60, 70, 80, 90, 10],
    [20, 30, 40, 50, 99],
    [70, 80, 90, 10, 20],
    [30, 40, 50, 60, 70]
])

print("Matriz 5x5 antes da alteração:")
print(matriz)

matriz[0][1] = 15

matriz[2][4] = 45

print("\nMatriz 5x5 depois da alteração:")
print(matriz)
