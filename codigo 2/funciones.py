"""
Ejemplo de funciones en python
"""

# Tipos anotados python 3.6:
def funcion(a:str, n:int) -> None:
    print(a.upper() * n)



# Que ocurre con la sobrecarga de funciones
def parametros(ob1,ob2,op1=1,op2=2,*args, **kwargs):
    print('Obligatorios: ',ob1,ob2)
    print('opcionales: ', op1,op2)
    print('args: ', args)
    print('kwargs: ', kwargs)
    print()

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
    parametros(1,2)
    parametros(1,2,3,4)
    parametros(1,2,op2=0)
    parametros(1,2,3,4,5,6,7,8)
    parametros(1,2,3,4,5,6,7,8,x=10,y=20,z=30)


    exit()

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

    # Con una lista:
    L = [1,2]
    print(suma(*L))

    # Definir una lista de tuplas de dos elementos y llamar 
    # a la función suma y dejar los resultados en otra lista
    L1 = [(1,1),(2,2),(3,3)]

    L2 = []

    for i in L1:
        L2.append(suma(*i))

    print(L2)




    