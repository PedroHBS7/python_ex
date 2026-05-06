# Exercício 19

numeros = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maior_soma = numeros[0]
soma_atual = numeros[0]

for i in range(1, len(numeros)):
    if soma_atual + numeros[i] > numeros[i]:
        soma_atual = soma_atual + numeros[i]
    else:
        soma_atual = numeros[i]

    if soma_atual > maior_soma:
        maior_soma = soma_atual

print("Lista:", numeros)
print("Maior soma contígua:", maior_soma)
