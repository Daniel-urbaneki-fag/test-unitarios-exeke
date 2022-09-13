import os
import unittest
import sys

sys.path.append(os.path.abspath("."))

from app.models.empresa import Empresa

class TestExeke(unittest.TestCase):
    
    def testExcluirEmpresa(self):
        e1 = Empresa()

        # Caso exista a empresa SALDÃO
        # self.assertEqual("Dados EXCLUIDOS com sucesso.", e1.excluirEmpresa("SALDÃO"))

        # Não existindo a empresa informada
        self.assertEqual("Não existe empresa para a exclusão !", e1.excluirEmpresa("SALDÃO"))
        
        print(e1.lerTabelaEmpresa())

if __name__ == "__main__":
    unittest.main()