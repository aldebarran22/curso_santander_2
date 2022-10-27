"""
Convertir un bloque de registros en CSV a una lista de diccionario
"""

def csvToFix(path,pathD, dicc, sep_col=','):

    def getCadenaFormato(dicc):
        cad = ""
        for tipo, tam in dicc.values():
            cad += "%"+ str(tam) + tipo
        return cad

    fich = None
    fich2 = None
    try:
        fich = open(path, "r")
        fich2 = open(pathD, "w")
        valores = list(dicc.values())
        cab = None

        for linea in fich:    
            linea = linea.rstrip()

            if not cab:
                fich2.write(linea+"\n")
                cab = True
                continue

            campos = linea.split(sep_col)
            for pos, t in enumerate(valores):
                tipo, tam = t
                if tipo == 'd':
                    campos[pos] = int(campos[pos])

                if tipo == 'f':
                    campos[pos] = float(campos[pos])

            tupla = tuple(campos)
            cadenaFormato = getCadenaFormato(dicc)
            print(cadenaFormato, tupla)
            fich2.write( (cadenaFormato % tupla) +"\n")            

    except Exception as e:
        raise e

    finally:
        if fich: fich.close()     
        if fich2: fich2.close()       

def csvToJson(path,sep_col=',',conCabs=True,cabeceras=None):
    fich = None
    try:
        cabs = cabeceras if conCabs == False else None
        R = []
        fich = open(path, "r")

        for linea in fich:
            linea = linea.rstrip()
            if conCabs:
                if not cabs:
                    cabs = linea.split(sep_col)
                    continue

            # Procesar la linea:
            campos = linea.split(sep_col)
            dicc = dict(zip(cabs, campos))
            R.append(dicc)
        return R

    except IOError as e:
        raise e

    finally:
        if fich: fich.close()

def jsonToCsv(R, sep_lin="\n", sep_col=','):
    csv2 = ""
    csv2 += sep_col.join(R[0].keys())+sep_lin
    for dic in R:
        datos = sep_col.join(dic.values())+sep_lin
        csv2 += datos
    return csv2

def testConCabeceras():
    fichero = "Empresas.txt"
    R = csvToJson(f"../ficheros/{fichero}",sep_col=';')
    for i in R:
        print(i)
    print()

def testSinCabeceras():
    fichero = "yob1880.txt"
    t = ("Nombre",'Sexo','Cuenta')
    R = csvToJson(f"../ficheros/{fichero}",conCabs=False, cabeceras=t)
    for i in R:
        print(i)
    print()

def testCSVToFix():
    fichero = "Pedidos.txt"
    fichero2 = "Pedidos.dat"
    cab = "idpedido;cliente;idempleado;idempresa;importe;pais"
    tam = (5,-5,3,3,8,-30)
    tipos = ('d','s','d','d','f','s')
    tuplas = tuple(zip(tipos,tam))
    d = dict(zip(cab.split(';'), tuplas))
    csvToFix(f"../ficheros/{fichero}", f"../ficheros/{fichero2}",dicc=d, sep_col=';')

if __name__ == "__main__":
    testCSVToFix()


"""
    cab = "idpedido;cliente;idempleado;idempresa;importe;pais"
    tam = (5,5,3,3,8,30)
    tipos = ('d','s','d','d','f','s')
    tuplas = tuple(zip(tipos,tam))
    d = dict(zip(cab.split(';'), tuplas))
    print(d)
   

    nombre = "nombre producto"
    precio = 5634.6
    numero = 34

    s = "%s %d %f" % (nombre, numero, precio)
    print(s)
    print()

    s = "%20s\t%05d %.2f" % (nombre, numero, precio)
    print(s)

    s = "%-20s%05d%8.2f" % (nombre, numero, precio)
    print(s)
"""




