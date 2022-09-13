import os
import unittest
import sys

sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("./app/models/utils"))

from app.models.utils.utilitariosUsuarios import UtilitariosUsuarios

class TestExeke(unittest.TestCase):
    
    def testeCriaTabelaEmpresa(self):
        utilsUsuario = UtilitariosUsuarios()

        usuario1 = {
            "nome" : "Daniel",
            "senha" : "daniel123",
            "cpf" : "101.853.769-40",
            "email" : "daniel_urba@hotmail.com",
            "logradouro" : "Assis brasil",
            "numero" : "48",
            "complemento" : "",
            "bairro" : "sao cristovão",
            "cep" : "85816030",
            "telefone" : "45999789334",
            "cidade" : "cascavel",
            "estado" : "pr",
        }
        
        self.assertEqual("Usuário cadastrado com sucesso!", utilsUsuario.cadastrarUsuario(usuario1))

if __name__ == "__main__":
    unittest.main()