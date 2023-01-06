numitens=eval(input('Itens comprados: '))

compra=numitens*10
desconto=0

if numitens>=20:
    desconto=compra*20/100
elif numitens>=11:
    desconto=compra*10/100

compra=compra-desconto

print(f'Valor total {compra}!!')