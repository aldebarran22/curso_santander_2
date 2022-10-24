"""
Operaciones con tuplas en python
"""

# Inicialización múltiple
a,b = 1,2
print(a,b)

# intercambio de vars.
a,b = b,a
print(a,b)

# Expansión de tuplas:
t = (1,5)
a = t[0]
b = t[1]
a,b = t

try:
    t2 = (1,2,3)
    a,b = t2
except Exception as e:
    print(e.__class__.__name__,e)

# Desempaquetar los dos primeros:
a,b,*resto = (1,2,3,4,5,6)
print(a,b,resto)    

a,b,*_ = (1,2,3,4,5,6)
print(a,b)

fich = "horario.docx"
t = fich.partition('.')
print(t)
f, _, ext = fich.partition('.')
print(f)
print(ext)

t = tuple("hola que tal")
print(t)
L = list(t)
print(L, id(L))
t2 = tuple(L)
print(t2, id(t2))

# método count
print('a se repite',t.count('a'),'veces')

# método index
print('posición de q', t.index('q'))

