cadena = "Estamos en la clase de Complejidad Algoritmica"
find = "a"
indices = []
for i in range(len(cadena)):
    if(cadena[i].lower == find):
        indices.append(i)
print(indices)