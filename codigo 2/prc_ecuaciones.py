"""
Resolver ecuaciones de 2º grado en python

"""
import math

print(math.sqrt(25))

a,b,c = 1,5,4 # Con solución
#a,b,c = 1,2,3 # Sin solución

raiz = b**2  - 4*a*c
if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2*a)
    x2 = (-b - math.sqrt(raiz)) / (2*a)

    print(x1,x2)
else:
    print('Sin solución')
