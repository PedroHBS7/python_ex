# Exercício 16

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

intersecao = []

for elemento in lista1:
    if elemento in lista2 and elemento not in intersecao:
        intersecao.append(elemento)

print("Lista 1:    ", lista1)
print("Lista 2:    ", lista2)
print("Interseção: ", intersecao)
