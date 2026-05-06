# Exercício 8
import numpy as np

matriz = np.array([
    [85, 92, 78],
    [70, 88, 91],
    [62, 75, 80]
])

print("Matriz 3x3:")
print(matriz)

medias_por_linha = np.mean(matriz, axis=1)

print("\nMédia aritmética de cada linha:")
for i in range(len(medias_por_linha)):
    print(f"  Linha {i}: {medias_por_linha[i]:.2f}")
