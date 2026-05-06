# Exercício 1
import numpy as np

manha = np.array([
    [5.0, 2.0, 8.0],
    [0.0, 3.5, 1.0],
    [7.0, 4.0, 6.5]
])

tarde = np.array([
    [3.0, 1.5, 2.0],
    [4.0, 0.5, 3.0],
    [2.5, 5.0, 1.5]
])

total = manha + tarde

print("Matriz da manhã (mm):")
print(manha)

print("\nMatriz da tarde (mm):")
print(tarde)

print("\nMatriz total - chuva por dia e por região (mm):")
print(total)
