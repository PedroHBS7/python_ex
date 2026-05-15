# Exercício 15
def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

mostrar_dados(nome="Ana", idade=20, cidade="Curitiba")
