# Exercício 18

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i = i + 1
        else:
            resultado.append(direita[j])
            j = j + 1

    while i < len(esquerda):
        resultado.append(esquerda[i])
        i = i + 1

    while j < len(direita):
        resultado.append(direita[j])
        j = j + 1

    return resultado


numeros = [38, 27, 43, 3, 9, 82, 10]

print("Lista original: ", numeros)
print("Lista ordenada: ", merge_sort(numeros))
