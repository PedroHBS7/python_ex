# Exercício 20

def permutacoes(lista):
    if len(lista) == 0:
        return [[]]

    resultado = []

    for i in range(len(lista)):
        elemento = lista[i]
        restante = lista[:i] + lista[i + 1:]

        for perm in permutacoes(restante):
            resultado.append([elemento] + perm)

    return resultado


numeros = [1, 2, 3]

todas = permutacoes(numeros)

print("Lista:", numeros)
print(f"Total de permutações: {len(todas)}")
print("Permutações:")
for p in todas:
    print(p)
