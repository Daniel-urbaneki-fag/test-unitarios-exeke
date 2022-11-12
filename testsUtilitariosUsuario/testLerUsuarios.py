import os
import unittest
import sys

sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("./app/models/utils"))

from app.models.utils.utilitariosUsuarios import UtilitariosUsuarios

class TestExeke(unittest.TestCase):
    
    def testLerEmpresas(self):
        e1 = UtilitariosUsuarios()

        self.assertEqual("Leitura de Usuarios.", e1.lerTabelaUsuarios()[0])
        
        print(e1.lerTabelaUsuarios()[1])


if __name__ == "__main__":
    unittest.main()