# Exercício 2
import numpy as np

estoque_inicial = np.array([
    [100, 50, 80],
    [ 60, 90, 40],
    [ 75, 30, 55]
])

vendidos = np.array([
    [30, 20, 10],
    [15, 45, 25],
    [40, 10, 30]
])

estoque_final = estoque_inicial - vendidos

print("Estoque inicial:", estoque_inicial)
print(estoque_inicial)

print("\nProdutos vendidos:")
print(vendidos)

print("\nEstoque final:")
print(estoque_final)
