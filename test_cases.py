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

    #(4) Verifica que la clave tenga longitud mayor que 7.
    def test_PasswordMin(self):
        valid = self.seguridad.registrarUsuario("angel?@gmail.com", "X7SJ", "X7SJ")
        self.assertEqual(valid, False)

    #(6) Verifica que la clave no tenga caracteres no alfanumericos.
    def test_PasswordAlphaNum(self):
        valid = self.seguridad.registrarUsuario("angel?@gmail.com", "X7SJus62h7AHv?", "X7SJus62h7AHv?")
        self.assertEqual(valid, False)

    #(8) Verifica que la clave tenga al menos una mayuscula.
    def test_PasswordKeyMax(self):
        valid = self.seguridad.registrarUsuario("angel@gmail.com", "x781dd3pru3hv", "x781dd3pru3hv")
        self.assertEqual(valid, False)

    #(10) Verifica que la clave tenga al menos un digito.
    def test_PasswordDigit(self):
        valid = self.seguridad.registrarUsuario("angel@gmail.com", "probandoPass", "probandoPass")
        self.assertEqual(valid, False)

    #(12) Verifica que se agrega el usuario al diccionario.
    def test_AddUser(self):
        diccionario = len(self.seguridad.users)
        valid = self.seguridad.registrarUsuario("angel@gmail.com", "X7SJus62h7AHv", "X7SJus62h7AHv")
        diccionarioAdd = len(self.seguridad.users)
        self.assertNotEqual(diccionario, diccionarioAdd)


 

if __name__ == '__main__':
    unittest.main()