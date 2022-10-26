"""
Ejemplo de herencia multiple:
dt = DateTime(2022,10,26,12,34,5)
print(dt) ==> 26/10/2022 12:34:05
"""

class TiempoError(Exception):

    def __init__(self, mensaje=""):
        Exception.__init__(self,mensaje)

class Time:

    def __init__(self,hh=0,mm=0,ss=0):
        
        if hh < 0 or hh > 23: raise TiempoError("Horas incorrectas")
        if mm < 0 or mm > 59: raise TiempoError("Minutos incorrectas")
        if ss < 0 or ss > 59: raise TiempoError("Segundos incorrectas")

        self.__hh = hh
        self.__MM = mm
        self.__ss = ss

    def __str__(self):        
        return '%02d:%02d:%02d' % (self.__hh,self.__MM,self.__ss)

class Date:

    def __init__(self, dd,mm,yy):
        self.__dd = dd
        self.__mm = mm
        self.__yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.__dd,self.__mm,self.__yy)

    def esBisiesto(self):
        anyo = self.__yy    
        if  (anyo % 4 == 0 and anyo % 100 != 0) or (anyo%100 == 0 and anyo % 400 == 0):
            return True    
        else:
            return False

 
class DateTime(Time,Date):

    def __init__(self,dd=1,mm=1,yy=1970,HH=0,MM=0,SS=0):
        Date.__init__(self, dd,mm,yy)
        Time.__init__(self,HH,MM,SS)

    def __str__(self):
        return Date.__str__(self)+" "+Time.__str__(self)

   
if __name__ == '__main__':
    try:
        dt = DateTime(yy=2020, SS=9, HH=25)
        print(dt)
    except TiempoError as e:
        print(e)
   
    t = Time(20,4,55)
    print(t)
    #print("hh:",t.__hh)
