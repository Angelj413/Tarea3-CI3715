import unittest
from seguridad import Seguridad

class seguridadTestCase(unittest.TestCase):

    def setUp(self):
        self.seguridad = Seguridad()

    #Verifica que exista la clase self.seguridad.
    def test_seguridad(self):
        valid = self.seguridad
        self.assertNotEqual(valid, None)

    #Verifica que el id de correo sea valido segun el estandar RFC 822.
    def test_EmailValid(self):
        valid = self.seguridad.registrarUsuario("angel?@gmail.com", "X7SJus62h7AHv", "X7SJus62h7AHv")
        self.assertEqual(valid, False)
        
    #Verifica que la clave tenga longitud menor que 17.
    def test_PasswordMax(self):
        valid = self.seguridad.registrarUsuario("angel?@gmail.com", "X7SJus62h7AHvxxxx", "X7SJus62h7AHvxxxx")
        self.assertEqual(valid, False)
 

if __name__ == '__main__':
    unittest.main()