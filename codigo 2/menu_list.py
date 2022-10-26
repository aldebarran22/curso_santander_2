"""
Menú dinámico con una lista de función
"""

def suma(a,b):
    return a+b

def minimo(a,b):
    return min(a,b)

def resta(a,b):
    return a-b

def salir(*args):
    exit() 

def menu(L, a,b):
    while True:
        print('Menu principal:')      
        for i, f in enumerate(L):
            print(i+1, f.__name__)
        op = int(input("Opcion: "))

        print(L[op-1](a,b))
        print()

if __name__ == '__main__':
    L = [suma, resta, minimo, salir]    
    #menu(L, 5,7)

    f = suma
    print(type(f))
    print(f(8,3))

    s = "{}({},{})".format('resta',4,5)
    print(s)
    print(eval(s))

    f2 = lambda a,b : a if a < b else b
    print(f2(88,44))