"""
Convertir un bloque de registros en CSV a una lista de diccionario
"""

csv = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas"""

L = csv.split("\n")
R = []
cabs = L[0].split(";")
for i in L[1:]:    
    datos = i.split(";")
    emp = dict(zip(cabs, datos))
    R += [emp]
print(R) 
print(R[4]['nombre'])   


csv2 = ""
csv2 += ";".join(R[0].keys())+"\n"
for dic in R:
    datos = ";".join(dic.values())+"\n"
    csv2 += datos
print()
print(csv2)
