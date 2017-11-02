#acá voy a realizar una prueba usando el modulo unittest

import unittest
import usuario

class UsuarioTest(unittest.TestCase):

    def testSaludarDeberiaDevolverHola(self):
        #AAA
        #ARRANGE
        saludoEsperado = "Hola"

        #ACT
        saludoRecibido = usuario.saludar()

        #ASSERT
        self.assertEqual(saludoEsperado, saludoRecibido)