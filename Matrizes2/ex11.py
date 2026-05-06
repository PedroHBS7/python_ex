# Exercício 11
import numpy as np

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Matriz 3x3:")
print(matriz)


soma_colunas = []
for j in range(len(matriz[0])):
    soma_col = 0
    for i in range(len(matriz)):
        soma_col += matriz[i][j]
    soma_colunas.append(soma_col)

soma_colunas = np.array(soma_colunas)

print(f"\nArray com a soma de cada coluna: {soma_colunas}")
print(f"  Soma da coluna 0: {soma_colunas[0]}")
print(f"  Soma da coluna 1: {soma_colunas[1]}")
print(f"  Soma da coluna 2: {soma_colunas[2]}")
