import os
import unittest
import sys

sys.path.append(os.path.abspath("."))

from app.models.login import Login

class TestExeke(unittest.TestCase):
    
    def testeCriaTabelaEmpresa(self):
        lg = Login()

        usuario = {
            "email": "daniel_urba@hotmail.com",
            "senha" : "daniel123"
        }
        
        self.assertEqual("Login realizado com sucesso!", lg.login(usuario))

if __name__ == "__main__":
    unittest.main()