"""
Implementación del algoritmo de encriptado Cesar
"""

import string

alf = " "+string.ascii_letters+string.punctuation+"Ññ"+string.digits

def textoANumeros(texto):
    L = []
    for i in texto:
        L.append(alf.find(i))
    return L

def numerosATexto(numeros):
    s = ""
    for n in numeros:
        s += alf[n]
    return s

def encriptar(mensaje, k=5):
    """
    Encriptado con el algoritmo de Cesar
    """
    # 1) Pasar el mensaje a numeros
    L = textoANumeros(mensaje)

    # 2) Sumar k a cada número teniendo en cuenta lo del módulo
    L2 = []
    for i in L:
        L2.append((i+k) % len(alf))

    # 3) Volver a pasar a texto los números
    return numerosATexto(L2)

def desencriptar(mensaje_enc, k=5):
    return encriptar(mensaje_enc, -k)

def desencriptar2(mensaje_enc, k=5):   
    L = textoANumeros(mensaje_enc)
    L2 = [] 
    for i in L:
        L2.append((i-k) if (i-k) >= 0 else (i-k+len(alf)) )
    return numerosATexto(L2)


if __name__ == '__main__':
    mensaje = "hola que tal. Mi telefono es 699056050"    
    print(mensaje)

    mensaje_enc = encriptar(mensaje)
    print(mensaje_enc)

    print(desencriptar2(mensaje_enc))

    print(type(encriptar))
    print(encriptar.__name__)
    print(encriptar.__doc__)
