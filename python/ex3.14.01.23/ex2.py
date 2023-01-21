def ehpar(n):
    r = (n%2==0)
    return r

def somapares(lista):
    soma=0
    for num in lista:
        if (ehpar(num)):
            soma=soma+num
    return soma

lista= [2,6,9,8,2,5,3]
soma = somapares(lista)
print('A soma dos números pares é: [{}]'.format(soma))

