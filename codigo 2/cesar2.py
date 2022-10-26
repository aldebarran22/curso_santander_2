"""
Implementación del algoritmo de encriptado Cesar
"""

import string

alf = " "+string.ascii_letters+string.punctuation+"Ññ"+string.digits

def textoANumeros(texto):
    return [alf.find(i) for i in texto]
    
def numerosATexto(numeros):   
    return "".join([alf[n] for n in numeros])

def encriptar(mensaje, k=5):
    """
    Encriptado con el algoritmo de Cesar
    """
    # 1) Pasar el mensaje a numeros
    L = textoANumeros(mensaje)

    # 2) Sumar k a cada número teniendo en cuenta lo del módulo
    L2 = [(i+k) % len(alf) for i in L]   

    # 3) Volver a pasar a texto los números
    return numerosATexto(L2)

def desencriptar(mensaje_enc, k=5):
    return encriptar(mensaje_enc, -k)

def desencriptar2(mensaje_enc, k=5):   
    L = textoANumeros(mensaje_enc)
    L2 = [(i-k) if (i-k) >= 0 else (i-k+len(alf)) for i in L]    
    return numerosATexto(L2)


if __name__ == '__main__':
    mensaje = "hola que tal. Mi telefono es 699056050"    
    print(mensaje)

    mensaje_enc = encriptar(mensaje)
    print(mensaje_enc)

    print(desencriptar2(mensaje_enc))

    