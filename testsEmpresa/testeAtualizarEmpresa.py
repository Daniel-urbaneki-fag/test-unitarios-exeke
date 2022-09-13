from copy import deepcopy
import os
import unittest
import sys

sys.path.append(os.path.abspath("."))

from app.models.empresa import Empresa

class TestExeke(unittest.TestCase):
    
    def testAtualizarEmpresa(self):

        e1 = Empresa("DANIEL SOFT", "26159125000152", "CALÇADOS", "45977685596", "esmeralda@hotmail.com", "85815025", "Avenida Brasil", "Pacaembu",
            "443", "Cascavel", "Paraná", "Matriz")
        # e1.cadastrarEmpresa()

        # dados de empresa em DICT Python, json
        empresa1 = {
            "alvo" : "DANIEL SOFT",
            "razaoSocial" : "daniel soft",
            "cnpj" : "",
            "nomeFantasia" : "conserto de pcs",
            "telefone" : "",
            "email" : "",
            "cep" : "",
            "logradouro" : "",
            "bairro" : "",
            "numero" : "",
            "cidade" : "Assis",
            "estado" : "",
            "tipo" : "",
}
        # Faz copia de objeto sem alterar o objeto a ser copiado
        empresa2 = deepcopy(empresa1)
        empresa2["email"] = "daniel#hotmail.com"

        empresa3 = deepcopy(empresa1)
        empresa3["cep"] = "832382138"

        empresa4 = deepcopy(empresa1)
        empresa4["cnpj"] = "26159225040152"

        # print(e1.lerTabelaEmpresa()[1])

        # Se existir empresa, e atualizado com sucesso
        self.assertEqual("Atualizado com sucesso.", e1.atualizarEmpresa(empresa1))
        
        # Caso não exista
        # self.assertEqual("Não existe empresa para a atualização !", e1.atualizarEmpresa(empresa1))

        #Dados do EMAIL incorreto

        self.assertEqual("Email invalido", e1.atualizarEmpresa(empresa2))
        
        #Dados do CEP invalido

        self.assertEqual("Cep inválido", e1.atualizarEmpresa(empresa3))

        #Dados cnpj invalido

        self.assertEqual("Cnpj invalido", e1.atualizarEmpresa(empresa4))

        print(e1.lerTabelaEmpresa()[1])


if __name__ == "__main__":
    unittest.main()