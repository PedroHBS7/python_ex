# Exercício 9
import numpy as np

matriz = np.array([
    [ 5, 10, 15, 20],
    [25, 30, 35, 40],
    [45, 50, 55, 60],
    [65, 70, 75, 80]
])

print("Matriz 4x4:")
print(matriz)

soma_diagonal = 0
for i in range(len(matriz)):
    soma_diagonal += matriz[i][i]

print(f"\nElementos da diagonal principal: {[int(matriz[i][i]) for i in range(len(matriz))]}")
print(f"Soma da diagonal principal: {soma_diagonal}")
