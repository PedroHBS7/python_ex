# Exercício 12

numeros = [4, 7, 1, 9, 3, 6, 2, 8, 5]

maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("Lista:", numeros)
print("Maior:", maior)
print("Menor:", menor)
