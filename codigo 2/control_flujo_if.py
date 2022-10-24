"""
Control de flujo if
"""

n = 10

# Comprobar si n está dentro de un rango: 5 - 15
if n >= 5 and n <= 15:
    print('Esta en el rango')

if 5 <= n <= 15:
    print('Esta en el rango')

# Comparar dos variables
a = 3
b = 8
if a < b:
    print("a < b")
elif a > b:
    print("a > b")

    if a + 2 > b:
        print("a+2 > b")
        
else:
    print("a == b")    

