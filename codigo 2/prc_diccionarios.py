"""
1. Partiendo de una lista con repetidos convertirla en un diccionario que cuente las 
ocurrencias de cada elemento de la lista.
Calcular la moda
"""

L = [1,1,2,3,2,2,1,1,6]
# d = {1: 4, 2: 3, 3:1, 6:1}

d = {}
for i in L:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)        