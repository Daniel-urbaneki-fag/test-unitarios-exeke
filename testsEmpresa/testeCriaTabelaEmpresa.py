import os
import unittest
import sys

sys.path.append(os.path.abspath("."))

from app.models.empresa import Empresa

class TestExeke(unittest.TestCase):
    
    def testeCriaTabelaEmpresa(self):
        e1 = Empresa()
        
        # cria tabela se não existe, se existir não da erro
        self.assertEqual("Tabela criada com sucesso.", e1.criarTabelaEmpresas())

if __name__ == "__main__":
    unittest.main()