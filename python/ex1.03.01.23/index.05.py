altura=eval(input('Entre com a sua altura: '))
peso=eval(input('Entre com o seu peso: '))

imc=peso/(altura**2)

print(f'Seu IMC é:','{:5.5}'.format(imc))
if imc<18.5:
    print('Você está a baixo do peso!!')
elif imc>=18.4 and imc <25:
    print('Você está no peso ideal')
elif imc>=25:
    print('Você está a cima do peso')

