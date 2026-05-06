# Exercício 13
import numpy as np

n = 5

matriz = np.array([
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

print("Matriz 5x5:")
print(matriz)

print("\nElementos da diagonal secundária:")
for i in range(n):
    j = (n - 1) - i
    print(f"  matriz[{i}][{j}] = {matriz[i][j]}")
