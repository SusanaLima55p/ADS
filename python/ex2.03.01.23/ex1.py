#Entrada de dados, eval usado para tratar números
num1=eval(input('Entre com um múmero inteiro: '))
num2=eval(input('Entre com mais um número inteiro diferente do anterior: '))

#Comportamento inicial das variaveis
maior=num1

#Teste lógico para obter resposta
if maior < num2:
    maior=num2

#Exibição do resultado
print(f'O maior número que você digitou foi {maior}')