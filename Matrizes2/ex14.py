# Exercício 14
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matriz A:")
print(A)

print("\nMatriz B:")
print(B)

# Verifica se a multiplicação é possível
if A.shape[1] == B.shape[0]:
    # Multiplicação de matrizes com np.dot (como ensinado na aula)
    C = np.dot(A, B)
    print("\nMatriz resultante da multiplicação (A x B):")
    print(C)
else:
    print("\nErro: número de colunas de A deve ser igual ao número de linhas de B!")
    print(f"  Colunas de A: {A.shape[1]} | Linhas de B: {B.shape[0]}")
