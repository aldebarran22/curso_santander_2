class Empleado(object):
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
         
    def __getnombre(self):
        return self.__nombre
 
    def __getsalario(self):
        return self.__salario
   
    def __setnombre(self, nombre):
        self.__nombre = nombre
 
    def __setsalario(self, salario):
        self.__salario = salario
 
    def __delnombre(self):
        del self.__nombre
 
    def __delsalario(self):
        del self.__salario
     
    nombre = property(fget = __getnombre, fset = __setnombre, fdel = __delnombre, doc = "Soy la propiedad 'nombre'")
    salario = property(fget = __getsalario, doc = "Soy la propiedad 'salario'")
 
empleado1 = Empleado("Francisco José", 30000)
empleado1.nombre = "Rosa"  # Realiza una llamada al método "fset"
print(empleado1.nombre, empleado1.salario)  # Realiza una llamada al método "fget"

print(type(Empleado))

