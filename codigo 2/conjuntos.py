"""
Conjuntos en python
"""

# Quitar repetidos de una lista
L = [1,4,5,2,3,4,6,7,8,9]
c = set(L)
print(c, type(c))

L = list(set(L))
print(L)

# Definición
c2 = {1,4,3,5,6}
print(c2, type(c2))

print(5 in c2)
c2.add(88)
print(c2)
c2.remove(88)
print(c2)

L1 = [1,3,5,6,3,3,1,5,6,9]
L2 = [1,2,3,5,5,8,10]
c1 = set(L1)
c2 = set(L2)
print("Union: ", c1 | c2)
print("Inter: ", c1 & c2)

c1 = {1,2,3,4}
c2 = {4,3,6,7}
print(c1 - c2)
print(c2 - c1)
print(c1 ^ c2)






