"""
Ejemplos de generadores en python
"""
def multiplos3List(ini, fin, salto=1):
    L = []
    for i in range(ini, fin, salto):
        if i % 3 == 0:
            print('List multiplo 3')
            L.append(i)
    return L

def multiplos3Gen(ini, fin, salto=1):
    
    for i in range(ini, fin, salto):
        if i % 3 == 0:
            print('Gen multiplo 3')
            # Sirve un multiplo de 3
            yield i

if __name__ == '__main__':
    print('Lista:')
    for i in multiplos3List(2,25):
        print(i)
        
    print('Generador:')
    for i in multiplos3Gen(2,25):
        print(i)

