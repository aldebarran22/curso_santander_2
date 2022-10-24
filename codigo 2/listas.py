"""
Listas en Python: funciones, operadores, definición, acceso
"""

L = [1,2,4,5,61,1,1,9]
print(L, type(L))

L[0] = 400
print(L)

# Operadores: + *
L += [900]
print(L)
print(L * 2)

# in
if 900 in L:
    print('esta dentro')

# Bucle
for i in L:
    print(i, end=" ")
print()

# Bucle con indice + objeto
for pos, i in enumerate(L):
    print(pos, i)

# Funcion list
L = list('palabra')
print(L)

# Funciones: min, sum, max, len, del
L = [1,2,3,4,5,6,55]
print('Min',min(L))
print('Max',max(L))
print('Sum',sum(L))
print('Len',len(L))
print('Media: ',sum(L)/len(L))
del(L[0])
#del(L) Borra toda la lista (la variable)
print(L)

try:
    print(L[40])
except Exception as e:
    print(e.__class__.__name__,e)

try:
    for i in 7:
        print(L[i])

except Exception as e:
    print(e.__class__.__name__,e)

try:
    print(L(0))
except Exception as e:
    print(e.__class__.__name__,e)    

try:
    n = 10
    print(n[0])
except Exception as e:
    print(e.__class__.__name__,e)    

# Copia: OJO es una referencia a los mismos datos
L1 = [1,2,3,4,5]
L2 = L1
L1[0] = 1000
print('L1',L1, id(L1))
print('L2',L2, id(L2))
print()

# Copiando bien, pero los items tienen que ser inmutables!
L1 = [1,2,3,4,5]
L2 = L1.copy()
L1[0] = 1000
print('L1',L1, id(L1))
print('L2',L2, id(L2))
print()

# Prueba con objetos mutables
import copy
L1 = [[1,2,3],[4,5]]
L2 = copy.deepcopy(L1)
L1[0] = 1000
L1[1] += [900]
print('L1',L1, id(L1))
print('L2',L2, id(L2))
print(L1[1][0])

# Slicing: list, str, tuple: coleccion[ini:fin-1:salto]
L = [10,20,30,40,50]
print('Los 3 primeros:',L[0:3])
print('Los 3 primeros:',L[:3]) # Desde el principio de la lista
print('Los tres ultimos: ', L[-3:])
print('Quitar los extremos: ', L[1:-1])
print('La lista de 2 en 2:', L[::2])
print('Invertida: ', L[::-1])

s = "aaabobaaa"
print(s,'es palindromo',s==s[::-1])

path = "C:/mis documentos/word/cv.docx"
L = path.split('/')
print(L)
print(L[-1])
print(path.split("/")[-1])

# range(ini, fin-1, salto)
for i in range(10):
    print(i)

print('Cuenta atrás: ', list(range(10,-1,-1)))

L = [2,4,5,6,7,8]
for i in range(len(L)):
    print(L[i])

M = [[1,2,3], \
    [4,5,6], \
    [7,8,9]]

for fila in M:
    for i in fila:
        print(i, end='\t')
    print()        