# Exercício 3
import numpy as np

matriz = np.array([
    [10, 25, 33, 47],
    [52, 61, 78, 84],
    [91, 15, 23, 36],
    [44, 55, 66, 77]
])

print("Matriz 4x4:")
print(matriz)

numero = int(input("\nDigite um número para buscar na matriz: "))

if numero in matriz:
    print(f"\nO número {numero} FOI ENCONTRADO na matriz.")
else:
    print(f"\nO número {numero} NÃO foi encontrado na matriz.")
