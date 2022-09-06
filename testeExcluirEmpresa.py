import unittest
from app.models.empresa import Empresa

class TestExeke(unittest.TestCase):
    
    def testExcluirEmpresa(self):
        e1 = Empresa()
        
        self.assertEqual("Dados EXCLUIDOS com sucesso.", e1.excluirEmpresa("SALDÃO"))
        
        print(e1.lerTabelaEmpresa())

if __name__ == "__main__":
    unittest.main()