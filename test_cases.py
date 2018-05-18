import unittest
from seguridad import Seguridad

class seguridadTestCase(unittest.TestCase):

    def setUp(self):
        self.seguridad = Seguridad()

    #Verifica que exista la clase self.seguridad.
    def test_seguridad(self):
        valid = self.seguridad
        self.assertNotEqual(valid, None)


 

if __name__ == '__main__':
    unittest.main()