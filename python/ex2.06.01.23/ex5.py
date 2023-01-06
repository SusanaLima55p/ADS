listnum=[10,2,5,7,6,3]
n=len(listnum)
soma=0

for i in range(n):
    if(listnum[i]%2==0):
        soma=soma+listnum[i]

print(f'O somatório dos elementos da lisata é {soma}')

