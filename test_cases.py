import unittest
from seguridad import Seguridad

class seguridadTestCase(unittest.TestCase):

    def setUp(self):
        self.seguridad = Seguridad()

    #(1) Verifica que exista la clase self.seguridad.
    def test_seguridad(self):
        valid = self.seguridad
        self.assertNotEqual(valid, None)

    #(2) Verifica que exista el metodo registrarUsuario.
    def test_registrar(self):
        valid = self.seguridad.registrarUsuario("angel@gmail.com", "X7SJus62h7AHv", "X7SJus62h7AHv")
        self.assertNotEqual(valid, None)


 

if __name__ == '__main__':
    unittest.main()