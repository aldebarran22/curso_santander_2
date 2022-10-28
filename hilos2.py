"""
Hilos: condición de carrera y mecanismos de sincronización: Lock
"""

from threading import Thread, Lock

iteraciones = 1000000
contador = 0
contador2 = 0

class Sumador(Thread):

    def __init__(self):
        Thread.__init__(self, name="sumador")

    def run(self):
        global contador
        for i in range(iteraciones):
            contador += 1       

class Sumador2(Thread):

    def __init__(self, mutex):
        Thread.__init__(self, name="sumador2")
        self.mutex = mutex

    def run(self):
        global contador2
        for i in range(iteraciones):
            self.mutex.acquire()
            # Esta operación se realiza en exclusión mutua
            contador2 += 1
            self.mutex.release()


class Restador(Thread):

    def __init__(self):
        Thread.__init__(self, name="restador")

    def run(self):
        global contador
        for i in range(iteraciones):
            contador -= 1       

class Restador2(Thread):

    def __init__(self,mutex):
        Thread.__init__(self, name="restador2")
        self.mutex = mutex

    def run(self):
        global contador2
        for i in range(iteraciones):
            with self.mutex:
                contador2 -= 1     

if __name__ == '__main__':
    mutex = Lock()

    sumador = Sumador()
    restador = Restador()
    sumador2 = Sumador2(mutex)
    restador2 = Restador2(mutex)

    sumador.start()
    restador.start() 
    sumador2.start()
    restador2.start()

    sumador2.join()
    restador2.join()
    sumador.join()
    restador.join()

    print("Contador sin Lock:", contador)
    print("Contador2 con Lock:", contador2)