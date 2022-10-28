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
