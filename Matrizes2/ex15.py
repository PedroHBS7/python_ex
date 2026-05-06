# Exercício 15

def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)

def rotacionar_90_horario(matriz):
    n = len(matriz)

    resultado = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        resultado.append(linha)

    for i in range(n):
        for j in range(n):
            resultado[j][n - 1 - i] = matriz[i][j]

    return resultado

n = 4
matriz = [
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(f"Matriz original ({n}x{n}):")
exibir_matriz(matriz)

matriz_rotacionada = rotacionar_90_horario(matriz)

print(f"\nMatriz após rotação de 90° no sentido horário:")
exibir_matriz(matriz_rotacionada)
