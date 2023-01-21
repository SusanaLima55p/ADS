
def fatoracao(num):
    
    if (num == 0 or num == 1):
        return 1

    else:
        cont=1
        resultado=1
            
        while cont <= num:
            resultado *= cont
            cont+= 1
                      
        return resultado

num = (eval(input('Digite um número para saber o seu fatorial: ')))
fatorial = fatoracao(num)
print ('O fatorial do número que você digitou é: [{}]'.format(fatorial))    
