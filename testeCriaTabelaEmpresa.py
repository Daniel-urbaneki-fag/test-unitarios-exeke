import unittest
from app.models.empresa import Empresa

class TestExeke(unittest.TestCase):
    
    def testeCriaTabelaEmpresa(self):
        e1 = Empresa()
        
        self.assertEqual("Tabela criada com sucesso.", e1.criarTabelaEmpresas())

if __name__ == "__main__":
    unittest.main()