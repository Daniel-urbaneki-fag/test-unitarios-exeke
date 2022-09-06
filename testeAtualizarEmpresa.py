import unittest
from app.models.empresa import Empresa

class TestExeke(unittest.TestCase):
    
    def testAtualizarEmpresa(self):

        e1 = Empresa()

        empresa = {
            "alvo" : "DANIEL LTDA",
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

        print(e1.lerTabelaEmpresa()[1])
        self.assertEqual("Atualizado com sucesso.", e1.atualizarEmpresa(empresa))
        print(e1.lerTabelaEmpresa()[1])


if __name__ == "__main__":
    unittest.main()