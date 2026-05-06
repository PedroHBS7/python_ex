# Exercício 5
import numpy as np

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Matriz original:")
print(matriz)


k = float(input("\nDigite o número escalar: "))

matriz_resultado = k * matriz

print(f"\nMatriz resultante da multiplicação por escalar ({k}):")
print(matriz_resultado)
