# Exercício 17

matriz = [[1, 2], [3, 4], [5, 6]]

lista_plana = []

for sublista in matriz:
    for elemento in sublista:
        lista_plana.append(elemento)

print("Lista de listas:", matriz)
print("Lista achatada: ", lista_plana)
