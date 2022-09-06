import unittest
from app.models.empresa import Empresa

class TestExeke(unittest.TestCase):
    
    def testLerEmpresas(self):
        e1 = Empresa()

        self.assertEqual("Leitura de Empresa.", e1.lerTabelaEmpresa()[0])
        
        print(e1.lerTabelaEmpresa()[1])

if __name__ == "__main__":
    unittest.main()