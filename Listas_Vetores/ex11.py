# Exercício 11

lista_original = [3, 1, 2, 1, 4, 3, 5, 2]

lista_sem_duplicatas = []

for elemento in lista_original:
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)

print("Lista original:        ", lista_original)
print("Lista sem duplicatas:  ", lista_sem_duplicatas)
