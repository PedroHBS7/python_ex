# Exercício 7
import numpy as np

matriz = np.random.randint(0, 100, size=(4, 4))

print("Matriz preenchida com números aleatórios:")
print(matriz)

maior = np.max(matriz)

print(f"\nO maior elemento da matriz é: {maior}")
