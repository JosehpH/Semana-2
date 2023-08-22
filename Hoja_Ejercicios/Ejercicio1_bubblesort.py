def bubbleSort(lista:list):
    n = len(lista)
    for i in range(n-1):
        for j in range(i+1,n):
            if(lista[i]>lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
arreglo = [5,6,1,2]
bubbleSort(arreglo)
print(arreglo)