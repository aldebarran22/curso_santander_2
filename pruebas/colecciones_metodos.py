# -*- coding: utf-8 -*-

"""LISTAS

L = []

L = [1,2,3,4,5,6,8]

for i in L:
    print i,

print ""
print L[0]

L[0] = 88

print L

print range(10)

for x in range(8):
    print x
    
L = [1,2,3,4,5]

# saltando de dos en dos:
print "L[::2]", L[::2]

# acceder al primer elemento de la lista de dos formas:
print L[0],L[-5]

#quitar el último elemento de la lista
print L[:-1]

print L[:-2]

print L,L[:]

# quitar los dos primeros elementos
print L[2:], L[2]


"""

"""TUPLAS

t = (1,2)
print type(t)

t2 = (1)
print type(t2)

t3 = (1,)
print type(t3)

t = (1,2,3,4,5,6)
for i in t:
    print i,
"""

""" diccionarios:"""

print("\nDICCIONARIOS:")
d = {"uno":1,"dos":2}

print(d)
print(d["uno"])

if "uno" in d:
    print("clave uno existe")
else:
    print("NO existe")

for k in d.keys():
    print(k,d[k])
    
print(d.items())

if "tres" in d.keys():
	print("existe clave tres")
else:
	print("NO existe clave tres")

print(d.values())
print(d.get("tres","no hay"))
d["tres"]=3
print(d)
print("borrar tres:",d.pop("tres"))


# cadenas:
s = "hola que tal"
print("n = ", s.count("a"))
print(s.find("a"))
print(s.rfind("a"))
print(s.find("w"))
print(s.index("a"))
print(s.rindex("a"))

L=["1","2","3"]
print(" - ".join(L))

print(s.partition(" "))
print(s.replace("a","x"))
print(s.split(" "))
print(s.lower())
print(s.upper())
print(s.capitalize())
print((s+" ").strip())

# Listas:
print(len([1,2,3,4,5]))
print([1,2,3,4,5][0])

for i in range(10):
	print(i,end=",")
	
if [2,3,4]==[2,3,4]:
	print("si")	
	
a = [1,2,3]
b = a
if a is b:
	print("si is")	
	
a[0]=1000
print(b)
del(a[1])
print(b)
#print(cmp(1,3))

if 1000 in a:
	print("in si")
	
print(list('cadena'))	

a.append(2000)
print(a, len(a),a.count(1000))
c=[1,2,3]
a.extend(c)
print(a)
a.insert(1,3000)
print(a)
a.pop()
print(a)
a.remove(2000)
print(a)
a.reverse()
print(a)

	
	















