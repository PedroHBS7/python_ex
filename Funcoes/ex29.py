# Exercício 29
def calculadora(a, b, operacao):
    if operacao == 'somar':
        return a + b
    elif operacao == 'subtrair':
        return a - b
    elif operacao == 'multiplicar':
        return a * b
    elif operacao == 'dividir':
        return a / b

print(calculadora(10, 5, 'somar'))
print(calculadora(10, 5, 'multiplicar'))
