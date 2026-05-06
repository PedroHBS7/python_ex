# Exercício 3
import numpy as np

ingredientes = np.array([
    [2, 1, 3],
    [1, 2, 1]
])

pedidos = np.array([
    [5, 2],
    [3, 4],
    [1, 6]
])

print("Matriz ingredientes (2x3):")
print(ingredientes)

print("\nMatriz pedidos (3x2):")
print(pedidos)

resultado = np.dot(ingredientes, pedidos)

print("\nMatriz resultado da multiplicação (2x2):")
print(resultado)
