"""
Expresiones regulares en Python
"""
import re, string

def test(patron, L):
    return [re.match(patron, i)!=None for i in L]

# Validación de DNIs:
patron = r"\d{1,8}[A-Z]$"
print("patron:", patron)
L = ["AA","67990443F","233443SS","12345678G","12345678G44","1B"]
print(L)
print(test(patron, L))

# Palabras que terminan en punto y tienen 3 letras:
patron = r"...\.$"
print("patron:", patron)
L = ["abc","ddf.","...","asv..","aaa.a"]
print(L)
print(test(patron, L))

# Matriculas europeas: 4 dígitos + 3 letras consonates
s = "[" + "".join([i for i in string.ascii_uppercase if i not in "AEIOU"]) + "]"
print(s)
patron = r"\d{4}"+s+"{3}$"
print("patron:", patron)
L = ["1234SSf","1234TTY66","1234TTR","RRT3445","WWS","1234"]
print(L)
print(test(patron, L))

# Validación de códigos:
patron = r"COD_|S/N_[AEIOU]{3}_[1-9][0-9]{5}$"
print("patron:", patron)
L = ["COD_AEE_800959","S/N_UOO_958474","SN_UOO_958474","S/N_U4O_958474","S/N_UOO_958T74"]
print(L)
print(test(patron, L))


# Grupos:
patron = r"(COD|S/N)_([AEIOU]{3})_([1-9][0-9]{5})$"
obj = re.match(patron, "COD_AEE_800959")
if obj:
    print(obj)
    print(obj.groups())


# Validar cuenta bancaria e imprimir: entidad, sucursal, DC y número:
patron = r"([0-9]{4})([0-9]{4})([0-9]{2})([0-9]{10})$"
obj = re.match(patron, "30006000450123456789")
if obj:
    print(obj)
    print(obj.groups())


