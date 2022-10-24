"""
Diccionarios en Python, creación, acceso, operador, bucles
"""

d = {"uno":1, "dos":2, "tres":3}
print(d, type(d))
d['cuatro'] = 4
print(d)

# Operador in: OJO, VA POR LAS CLAVES!
print("cinco" in d)
print("tres" in d)
print(2 in d) # Buscar por las claves
print(2 in d.values()) # Buscar por valores

# Bucle:
for k,v in d.items():
    print(k, v)

print('Claves: ', d.keys())

# Como invertir un diccionario: {1:"uno",2:"dos",3:"tres"}

col1 = ["Francia","Alemania","Italia","Suiza","Belgica"]
col2 = [56000, 123000,4500, 400]
d = dict(zip(col1, col2))
print(d)

d2 = dict(zip(col2, col1))
print(d2)

d3 = dict()
for i in range(min(len(col1),len(col2))):
    d3[col1[i]] = col2[i]
print(d3)
d3.clear()
print(d3)

try:
    print(d3["Cuba"])
except Exception as e:
    print(e.__class__.__name__, e)

try:
    # Ojo la clave no es inmutable!
    d = {[1,2]:'uno', [3,4]:'dos'}
except Exception as e:
    print(e.__class__.__name__, e)    
