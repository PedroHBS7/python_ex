# Exercício 30
def processar_dados(*args, **kwargs):
    for valor in args:
        print(valor)
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

processar_dados(1, 2, 3, nome="Ana", cidade="Curitiba")
