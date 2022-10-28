"""
Clase de pruebas con unittest
"""
import unittest
import cesar
import cesar2
from random import randint
import string

N = 1000
K = 8

class Pruebas(unittest.TestCase):

    def generarCadena(self):
        s = string.ascii_letters
        cadena = ""
        for i in range(N):
            n = randint(0,len(s)-1)
            cadena += s[n]
        return cadena


    def testEncriptarDesencriptar(self):
        """
        Encriptar una cadena y desecriptarla y comparar con el original
        """
        cad = self.generarCadena()
        enc1 = cesar.encriptar(cad, K)
        cad_1 = cesar.desencriptar(enc1, K)
        cad_2 = cesar.desencriptar2(enc1, K)
        self.assertEqual(cad_1, cad_2, "No coinciden las dos formas de desencriptar en cesar")


    def testLanzaExcepcion(self):
        cad = self.generarCadena()+"ÑÑÑññññ"
        self.assertRaises(ValueError, cesar.encriptar, cad,K)
       

    def testEncriptarCon2Alg(self):
        """
        Comparar dos cadenas encriptadas con cada uno de los algoritmos y comparar resultados
        """
        cad = self.generarCadena()

        for i in range(200):
            enc1 = cesar.encriptar(cad, i)
            enc2 = cesar2.encriptar(cad, i)

            self.assertEqual(enc1, enc2, "No coinciden la encriptación de ambos algoritmos con k = "+str(i))


if __name__ == '__main__':
    unittest.main()

