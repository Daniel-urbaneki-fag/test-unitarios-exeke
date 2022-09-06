import unittest
from app.models.empresa import Empresa

class TestExeke(unittest.TestCase):
    
    def testCriarEmpresa(self):
        #Dados da empresa corretos / Cnpj já cadastrado
        e1 = Empresa("SALDÃO", "26159125000152", "CALÇADOS", "45977685596", "esmeralda@hotmail.com", "85815025", "Avenida Brasil", "Pacaembu",
            "443", "Cascavel", "Paraná", "Matriz")

        #Dados do EMAIL incorreto
        e2 = Empresa("SALDÃO", "26159125000152", "CALÇADOS", "45977685596", "esmeralda.hotmail.com", "85815025", "Avenida Brasil", "Pacaembu",
            "443", "Cascavel", "Paraná", "Matriz")

        #Dados do CEP invalido
        e3 = Empresa("SALDÃO", "26159125000152", "CALÇADOS", "45977685596", "esmeralda@hotmail.com", "8581502", "Avenida Brasil", "Pacaembu",
            "443", "Cascavel", "Paraná", "Matriz")
      
        # Verifica o cnpj que ja está inserido no banco de dados
        self.assertEqual("O cnpj já está cadastrado !", e1.cadastrarEmpresa())

        # Exclusão da empresa para tratar erros seguintes
        e1.excluirEmpresa('SALDÃO')

        # Se espera que o email seja inválido
        self.assertEqual("Email invalido", e2.cadastrarEmpresa())

        # Se espera que o cep seja inválido
        self.assertEqual("Cep inválido", e3.cadastrarEmpresa())

        # Inseri os dados corretamentes no banco de dados
        self.assertEqual("Dados inseridos com sucesso.", e1.cadastrarEmpresa())

if __name__ == "__main__":
    unittest.main()