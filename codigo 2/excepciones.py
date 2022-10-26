"""
Captura de excepciones en python
"""

def funcion1(L,i):
    print(L[i])


def prueba():
    L = list('hola que tal')
    funcion1(L, 40)   

def main():
    try:
        m = input('Teclea control+C')
        n = int("fr")
        prueba()

    except ValueError as e:
        print('Error de conversion:',e)

    except Exception as e:
        print(e.__class__.__name__, e)

    except:
        print("\nOtro error")

if __name__ == '__main__':
    main()        
