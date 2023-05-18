def fatorial(n):
    if n == 0 or n == 1:
         return 1
    else:
         return n*fatorial(n-1)


n = (eval(input('Digite um número: ')))
res = fatorial(n)
print(res)