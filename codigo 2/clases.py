"""
Implementación de un DAO a la clase Pedido
"""

import sqlite3 as dbapi
from os.path import isfile

path = "../BD/empresa3.db"

class Pedido:

    def __init__(self, idpedido=0, idcliente='', importe=0, pais="", empresa=None, empleado=None):
        self.idpedido = idpedido
        self.idcliente = idcliente
        self.empleado = empleado
        self.importe = importe
        self.pais = pais
        self.empresa = empresa

    def __str__(self):
        return str(self.idpedido)+ " " + self.idcliente + " " +  str(self.empresa) + " " + \
            str(self.empleado) + " " + str(self.importe) + " " + self.pais 

    def __repr__(self):
        return str(self)

    def getTupleCreate(self):
        return (self.idpedido, self.idcliente, self.importe, self.pais, self.empleado.id, self.empresa.id)

    def getTupleUpdate(self):
        return (self.idcliente, self.importe, self.pais, self.empleado.id, self.empresa.id, self.idpedido)

class Empresa:

    def __init__(self,id=0, nombre=''):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return str(self.id)+ " " + self.nombre

    def __repr__(self):
        return str(self)

class Empleado:

    def __init__(self,id=0, nombre='',cargo=''):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo

    def __str__(self):
        return str(self.id)+ " " + self.nombre + " " + self.cargo

    def __repr__(self):
        return str(self)


class PedidoBD:

    def __init__(self, pathBD):
        if not isfile(pathBD):
            raise ValueError("No se encuentra el fichero: "+pathBD)

        self.con = dbapi.connect(pathBD)

    def __getSQL(self):
        sql = """select p.idpedido, p.idcliente, 
            p.importe, p.pais, emp.id as idemp,emp.nombre,emp.cargo, 
            e.id as ide, e.nombre from pedidos p
            inner join empresasenvios e on p.idempresaenvio=e.id
            inner join empleados emp on p.idempleado=emp.id"""         
        return sql

    def read(self, idpedido):
        cur = None
        try:
            sql = self.__getSQL() 
            sql += " where idpedido=?"
            cur = self.con.cursor() 
            cur.execute(sql, (idpedido,))

            t = cur.fetchone()
            if t == None:
                raise ValueError(f"El idpedido: {str(idpedido)} no existe")
            else:
                return self.__getPedido(t)  
               
        except Exception as e:
            raise e

        finally:
            if cur: cur.close()

    def __getPedido(self,t):
        tEmpresa = t[-2:]
        tEmpleado = t[-5:-2]
        empresa = Empresa(*tEmpresa)
        empleado = Empleado(*tEmpleado)
        tPedido = t[:4] + (empresa, empleado)
        return Pedido(*tPedido)

    def select(self, pais=None):
        cur = None
        try:
            sql = self.__getSQL()
            pedidos = list()
            cur = self.con.cursor()

            if pais:
                sql += " where pais=?"
                cur.execute(sql, (pais,))
            else:
                cur.execute(sql)

            for t in cur.fetchall():
                pedido = self.__getPedido(t)               
                pedidos.append(pedido)
                
            return pedidos

        except Exception as e:
            raise e

        finally:
            if cur: cur.close()

    def __update(self, sql, tupla):
        cur = None
        try:
            cur = self.con.cursor()
            cur.execute(sql, tupla)
            self.con.commit()
            return True

        except Exception as e:
            self.con.rollback()
            raise e

        finally:
            if cur: cur.close()

    def create(self, pedido):
        sql = "insert into pedidos(idpedido,idcliente,importe,pais,idempleado,idempresaenvio) values(?,?,?,?,?,?)"        
        tupla = pedido.getTupleCreate()
        self.__update(sql, tupla)

    def delete(self, idpedido):
        sql = "delete from pedidos where idpedido=?"
        tupla = (idpedido,)
        self.__update(sql, tupla)

    def update(self, pedido):
        sql = "update pedidos set idcliente=?, importe=?, pais=?, idempleado=?,idempresaenvio=? where idpedido=?"
        tupla = pedido.getTupleUpdate()
        self.__update(sql, tupla)

    def __del__(self):
        if hasattr(self, "con"): 
            if self.con:
                self.con.close()

if __name__ == '__main__':
    try:
        bd = PedidoBD(path)
        L = bd.select("Suiza")
        for p in L:
            print(p)

        ped2 = Pedido(10247, 'ALFKI',23.45,"Suiza",Empresa(1), Empleado(1))
        bd.create(ped2)

    except Exception as e:
        print(e)



