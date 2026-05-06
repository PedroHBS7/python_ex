# Exercício 12
import numpy as np

matriz = np.array([
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
])

print("Matriz:")
print(matriz)

transposta = matriz.T

print("\nMatriz Transposta:")
print(transposta)

if np.array_equal(matriz, transposta):
    print("\nA matriz É SIMÉTRICA (igual à sua transposta).")
else:
    print("\nA matriz NÃO é simétrica.")
