
def encontrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if (elem < minimo):
            minimo = elem
    return minimo

listat = [3,6,9,2,1]
menor = encontrar_minimo(listat)
print ('O menor elemento da lista é: [{}]'.format(menor))