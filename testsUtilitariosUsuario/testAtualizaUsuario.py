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
            "alvo" : "101.853.769-40",
            "nome" : "Daniel urbaneki",
            "senha" : "",
            "cpf" : "",
            "email" : "daniel_urba@hotmail.com",
            "logradouro" : "",
            "numero" : "",
            "complemento" : "",
            "bairro" : "",
            "cep" : "",
            "telefone" : "45999998888",
            "cidade" : "",
            "estado" : "",
        }
        
        self.assertEqual("Atualizado com sucesso.", utilsUsuario.atualizarUsuario(usuario1))

if __name__ == "__main__":
    unittest.main()