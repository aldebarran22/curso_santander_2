"""
Implementación del P - C
"""

from threading import Thread, Lock, Semaphore
from random import randint
from time import sleep

BUFFER_SIZE = 15
NUM_ITEMS = 20

class Productor(Thread):
    
    def __init__(self, mutex, sem_huecos, sem_items, buffer,index_p, index_c):
        Thread.__init__(self)
        self.mutex = mutex
        self.sem_huecos = sem_huecos
        self.sem_items = sem_items
        self.buffer = buffer
        self.index_c = index_c
        self.index_p = index_p

    def run(self):
        for i in range(NUM_ITEMS):
            numero = randint(0,100)
            self.sem_huecos.acquire()
            self.mutex.acquire()
            self.buffer[self.index_p] = numero
            self.index_p = (self.index_p + 1) % BUFFER_SIZE
            print("PROD: ",numero,self.buffer)
            self.mutex.release()
            self.sem_items.release()  
            sleep(randint(0,1))

class Consumidor(Thread):
    
    def __init__(self, mutex, sem_huecos, sem_items, buffer,index_p, index_c):
        Thread.__init__(self)
        self.mutex = mutex
        self.sem_huecos = sem_huecos
        self.sem_items = sem_items
        self.buffer = buffer
        self.index_c = index_c
        self.index_p = index_p

    def run(self):
        for i in range(NUM_ITEMS):
            self.sem_items.acquire()
            self.mutex.acquire()
            numero = self.buffer[self.index_c] 
            self.buffer[self.index_c]  = 0
            print("CONS: ", numero, self.buffer)
            self.index_c = (self.index_c + 1) % BUFFER_SIZE
            self.mutex.release()
            self.sem_huecos.release()
            sleep(randint(2,3))

if __name__ == '__main__':
    index_p = index_c = 0
    mutex = Lock()
    sem_huecos = Semaphore(BUFFER_SIZE) 
    sem_items = Semaphore(0)
    buffer = [0] * BUFFER_SIZE

    p = Productor(mutex, sem_huecos, sem_items, buffer, index_p, index_c)
    p.start()

    c = Consumidor(mutex, sem_huecos, sem_items, buffer, index_p, index_c)
    c.start()

    p.join()
    c.join()


