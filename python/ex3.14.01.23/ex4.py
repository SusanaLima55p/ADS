def verinumdigi(numeros):
    contador = 1
    while contador <3:
        contador +=1
        print({contador})
        numeros += [(eval(input('Digite um número para o somatório: ')))]
    print('Seu conjunto é [{}]'.format(numeros)) 

def somatorio(numeros):
    resultado = numeros[0] + numeros[1] +numeros[2]
    print('A soma dos elementos do conjunto é [{}]'.format(resultado)) 



numeros = [(eval(input('Digite um número para o somatório: ')))]
verinumdigi(numeros)
somatorio(numeros)
print(type(numeros)) 
