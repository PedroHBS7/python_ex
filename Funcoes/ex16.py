# Exercício 16
def com_args(*args):
    print(args)

def com_kwargs(**kwargs):
    print(kwargs)

com_args(1, 2, 3)
com_kwargs(nome="Ana", idade=20)
