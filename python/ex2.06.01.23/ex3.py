#Entrada de dados, eval usado para tratar números
notaaluno=eval(input('Entre com a nota do aluno:  '))


if notaaluno>=7:
    situacao=('foi aprovado!!')
elif notaaluno>=5:
    situacao=('está em recuperação!!')
else:
    situacao=('foi reprovado!!')

print(f'O aluno {situacao}')
