"""
Ejemplo de funciones en python
"""

# Que ocurre con la sobrecarga de funciones

def suma(a,b):
    """
    Sumar dos numeros
    """
    return a + b

def suma3(a,b,c):
    """
    Sumar tres numeros
    """
    return a+b+c

if __name__ == '__main__':
    # Forma posicional
    print(suma(1,2)) 

    # Forma nominal:
    print(suma(b=2,a=1))

    # Con una tupla:
    t = (1,2)
    print(suma(*t))

    # Con un dicc:
    d = {"b": 2,"a": 1}
    print(suma(**d))

    # Definir una lista de tuplas de dos elementos y llamar 
    # a la función suma y dejar los resultados en otra lista
    L1 = [(1,1),(2,2),(3,3)]

    L2 = []

    for i in L1:
        L2.append(suma(*i))

    print(L2)




    