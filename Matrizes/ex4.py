# Exercício 4
import numpy as np

salarios = np.array([
    [3000.0, 4500.0, 2800.0],
    [5200.0, 3800.0, 6000.0],
    [4100.0, 3300.0, 5500.0]
])

print("Matriz de salários original:")
print(salarios)

salarios_reajustados = salarios * 1.10

print("\nMatriz de salários reajustados (aumento de 10%):")
print(salarios_reajustados)
