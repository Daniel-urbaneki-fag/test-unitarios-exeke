import os
import unittest
import sys

sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("./app/models/utils"))

from app.models.utils.utilitariosUsuarios import UtilitariosUsuarios

class TestExeke(unittest.TestCase):
    
    def testeCriaTabelaEmpresa(self):
        utilsUsuario = UtilitariosUsuarios()
        
        self.assertEqual("Dados EXCLUIDOS com sucesso.", utilsUsuario.excluirUsuario("101.853.769-40"))

if __name__ == "__main__":
    unittest.main()