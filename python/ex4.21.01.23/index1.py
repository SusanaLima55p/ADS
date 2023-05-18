def regressiva(x):
    if x >=0:
        print(x)
        regressiva(x - 1)


x = (eval(input('Digite um número: ')))
regressiva(x)