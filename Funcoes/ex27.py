# Exercício 27
def media(lista):
    """
    Retorna a média dos valores de uma lista.

    Parâmetros:
        lista (list): lista de números

    Retorno:
        float: média dos valores
    """
    return sum(lista) / len(lista)

print(media([10, 20, 30]))
