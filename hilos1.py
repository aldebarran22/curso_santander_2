"""
Implementación de hilos:
Hilo1: lanza número aleatorio
Hilo2: imprime n mensajes
"""

from threading import Thread
from time import sleep
from random import randint

class Hilo1(Thread):

    def __init__(self, n):
        Thread.__init__(self, name="Aleatorios")
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.name, randint(0,10))
            sleep(randint(0,2))

        print('Aleatorio termina')

class Hilo2(Thread):

    def __init__(self, n):
        Thread.__init__(self)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.name, "Mensaje",(i+1))            
            sleep(randint(1,2))

        print(self.name,' termina')


def test1():
    hilo1 = Hilo1(15)
    hilo2 = Hilo2(10)

    hilo1.start()
    hilo2.start()

    hilo1.join()
    hilo2.join()

def test2():
    L = [Hilo2(randint(5,10)) for _ in range(10)]
    for hilo in L:
        hilo.start()

    for hilo in L:
        hilo.join()


if __name__ == '__main__':
    test2()
    print('Thread main termina')




