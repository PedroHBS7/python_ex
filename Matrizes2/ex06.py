# Exercício 6
import numpy as np

matriz = np.array([
    [ 2, 15, 8, 33],
    [10, 21, 4, 17],
    [13, 6, 19, 12]
])

print("Matriz 3x4:")
print(matriz)


contagem = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] % 2 == 0:
            contagem += 1

print(f"\nQuantidade de números pares na matriz: {contagem}")
