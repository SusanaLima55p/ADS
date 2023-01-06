#Entrada de dados, eval usado para tratar números
num1=eval(input('Entre com um número para ver se ele é par ou ímpar:  '))

#Teste lógico para obter resposta
if num1%2==0:
    resposta=(f'O número {num1} é par!!')
    
else:
    resposta=(f'O número {num1} é ímpar!!')

#Exibição do resultado
print(resposta)