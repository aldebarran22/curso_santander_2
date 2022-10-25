"""
Convertir un bloque de registros en CSV a una lista de diccionario
"""

txt_csv = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas"""

txt2 = """id,tno,email,dir
1,600998877,a@gmail.com,direccion1
2,640918827,b@gmail.com,direccion2"""

txt3 = """Mary,F,7065
Anna,F,2604
Emma,F,2003
Elizabeth,F,1939
Minnie,F,1746
Margaret,F,1578
Ida,F,1472"""

def csvToJson(csv,sep_lin='\n',sep_col=',',conCabs=True,cabeceras=None):
    L = csv.split(sep_lin)
    R = []

    if conCabs:
        cabs = L[0].split(sep_col)
        ini = 1
    else:
        cabs = cabeceras
        ini = 0

    for i in L[ini:]:    
        datos = i.split(sep_col)
        emp = dict(zip(cabs, datos))
        R += [emp]
    return R


def jsonToCsv(R, sep_lin="\n", sep_col=','):
    csv2 = ""
    csv2 += sep_col.join(R[0].keys())+sep_lin
    for dic in R:
        datos = sep_col.join(dic.values())+sep_lin
        csv2 += datos
    return csv2


if __name__ == "__main__":
    R = csvToJson(txt_csv,sep_col=';')
    print(R)
    print()

    csv1 = jsonToCsv(R, sep_col=';')
    print(csv1)
    print()
    
    R2 = csvToJson(txt3, conCabs=False, cabeceras=['Nombre','Sexo','Cuenta'])
    print(R2)
    print()

    """
    csv2 = jsonToCsv(R2)
    print(csv2)
    print()
    """