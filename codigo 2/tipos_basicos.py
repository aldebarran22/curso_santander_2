"""
Tipos básicos en python: int, float, complex
"""

n = "22"
numero = int(n)
print(numero, type(numero))
resul = 34 + 7.88
print(resul, type(resul))
c = complex(34)
print(c, type(c))

numero = int(input("Numero: "))
print(numero, bin(numero), oct(numero), hex(numero))