# Exercício 25
def contagem(n):
    if n == 0:
        print(0)
        return
    print(n)
    contagem(n - 1)

contagem(5)
