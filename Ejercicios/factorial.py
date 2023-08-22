def fac1(n):
    factorial = 1
    while(n>1):
        factorial *= n 
        n-=1
    return factorial

def fac2(n):
    if(n==0):
        return 1
    else:
        return n*fac2(n-1)

def actualizarLista(n:list,number:int):
    number += 10
    n.append(5)
    
lista = []
number = 0
print(lista,number)
actualizarLista(lista,number)
print(lista,number)

    