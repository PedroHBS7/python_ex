# Exercício 10
import numpy as np

m = int(input("Digite o número de linhas (M): "))
n = int(input("Digite o número de colunas (N): "))

matriz = []

for i in range(m):
    linha = []
    for j in range(n):
        elemento = float(input(f"Digite o elemento para a posição ({i},{j}): "))
        linha.append(elemento)
    matriz.append(linha)

matriz_np = np.array(matriz)

print(f"\nMatriz original ({m}x{n}):")
print(matriz_np)

matriz_transposta = matriz_np.T

print(f"\nMatriz transposta ({n}x{m}):")
print(matriz_transposta)
