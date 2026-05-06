# Exercício 15

lista = [1, 2, 3, 4, 5]
n = int(input("Digite o número de posições para rotacionar: "))

tamanho = len(lista)
n = n % tamanho  # evita rotações maiores que o tamanho da lista

rotacionada = lista[tamanho - n:] + lista[:tamanho - n]

print("Lista original:    ", lista)
print("Lista rotacionada: ", rotacionada)
