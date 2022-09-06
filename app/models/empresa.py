import sqlite3
from datetime import datetime
from .utils.utils import Utils

class Empresa():

    def __init__(self, *args):

        self.criarTabelaEmpresas()

        if(len(args) == 12):
            self.razaoSocial = args[0]
            self.cnpj = args[1]
            self.nomeFantasia = args[2]
            self.telefone = args[3]
            self.email = args[4]
            self.cep = args[5]
            self.logradouro = args[6]
            self.bairro = args[7]
            self.numero = args[8]
            self.cidade = args[9]
            self.estado = args[10]
            self.tipo = args[11]

    def cadastrarEmpresa(self):
        self.razaoSocial = self.razaoSocial.upper()

        if(not Utils.validarCnpj(self.cnpj)):
            return "Cnpj invalido"

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        for dados in cursor.execute(""" SELECT * FROM empresas WHERE cnpj=?; """, (self.cnpj,)):
            if(dados):
               return "O cnpj já está cadastrado !"
        
        self.nomeFantasia = self.nomeFantasia.upper()

        if(len(self.telefone) > 11):
            return "Telefone inválido"
        
        if(not Utils.validarEmail(self.email)):
            return "Email invalido"
        
        if(not Utils.validarCep(self.cep)):
            return "Cep inválido"
        
        self.logradouro = self.logradouro.capitalize()

        self.bairro = self.bairro.capitalize()
        
        if(len(self.numero) > 4):
            return "Numero da casa inválido"
        
        self.cidade = self.cidade.capitalize()

        self.estado = self.estado.capitalize()

        self.tipo = self.tipo.upper()

        cursor.execute("""INSERT INTO empresas (razaoSocial, cnpj, nomeFantasia, telefone, email, cep, logradouro, 
        bairro, numero, cidade, estado, tipo, criado_em)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);
        """, (self.razaoSocial, self.cnpj, self.nomeFantasia, self.telefone, self.email, self.cep, self.logradouro, self.bairro, self.numero, self.cidade, self.estado, self.tipo, datetime.today().strftime('%d-%m-%Y')))

        conn.commit()
        conn.close()
        return "Dados inseridos com sucesso."
    
    def excluirEmpresa(self, razaoSocial):
        conn = sqlite3.connect('db.sqlite3')
        
        cursor = conn.cursor()

        for dados in cursor.execute(""" SELECT * FROM empresas WHERE razaoSocial=?; """, (razaoSocial,)):
            if(dados):
                cursor.execute("DELETE FROM empresas WHERE razaoSocial=?;", (razaoSocial,))

                conn.commit()
                
                conn.close()
            
                return "Dados EXCLUIDOS com sucesso."

        return "Não existe empresa para a exclusão !"
    
    def atualizarEmpresa(self, updateEmpresa):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        for dados in cursor.execute(""" SELECT * FROM empresas WHERE razaoSocial=?; """, (updateEmpresa['alvo'],)):
            if(dados):
                empresa = {
                    "razaoSocial" : dados[1],
                    "cnpj" : dados[2],
                    "nomeFantasia" : dados[3],
                    "telefone" : dados[4],
                    "email" : dados[5],
                    "cep" : dados[6],
                    "logradouro" : dados[7],
                    "bairro" : dados[8],
                    "numero" : dados[9],
                    "cidade" : dados[10],
                    "estado" : dados[11],
                    "tipo" : dados[12]
                }

                for chave, valor in updateEmpresa.items():
                    if valor != "":
                        if chave == "razaoSocial" or chave == "nomeFantasia" or chave == "tipo":
                            empresa[chave] = valor.upper()
                        if chave == "cnpj":
                            if(not Utils.validarCnpj(valor)):
                                return "Cnpj invalido"
                            empresa[chave] = valor
                        if chave == "telefone":
                            if(len(valor) > 11):
                                return "Telefone inválido"
                            empresa[chave] = valor
                        if chave == "email":
                            if(not Utils.validarEmail(valor)):
                                return "Email invalido"
                            empresa[chave] = valor
                        if chave == "cep":
                            if(not Utils.validarCep(valor)):
                                return "Cep inválido"
                            empresa[chave] = valor
                        if chave == "logradouro" or chave == "bairro" or chave == "cidade" or chave == "estado":
                            empresa[chave] = valor.capitalize()
                        if chave == "numero":
                            if(len(valor) > 4):
                                return "Numero da casa inválido"
                            empresa[chave] = valor

                cursor.execute(""" UPDATE empresas SET 
                                razaoSocial = ?,
                                cnpj = ?,
                                nomeFantasia = ?,
                                telefone = ?,
                                email = ?,
                                cep = ?,
                                logradouro = ?,
                                bairro = ?,
                                numero = ?,
                                cidade = ?,
                                estado = ?,
                                tipo = ?
                                WHERE razaoSocial=?
                                ;""",
                    (empresa["razaoSocial"], empresa["cnpj"], empresa["nomeFantasia"],
                        empresa["telefone"], empresa["email"], empresa["cep"], empresa["logradouro"],
                        empresa["bairro"], empresa["numero"], empresa["cidade"], empresa["estado"],
                        empresa["tipo"], updateEmpresa['alvo']))

                conn.commit()
                
                conn.close()
            
                return "Atualizado com sucesso."

        return "Não existe empresa para a atualização !"
    
    def lerTabelaEmpresa(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM empresas; """)

        lista = []

        for linha in cursor.fetchall():
            lista.append(linha)

        conn.close()

        return ['Leitura de Empresa.', lista]
    
    def criarTabelaEmpresas(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empresas (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                razaoSocial TEXT NOT NULL,
                cnpj TEXT NOT NULL,
                nomeFantasia TEXT NOT NULL,
                telefone TEXT NOT NULL,
                email TEXT NOT NULL,
                cep TEXT NOT NULL,
                logradouro TEXT NOT NULL,
                bairro TEXT NOT NULL,
                numero TEXT NOT NULL,
                cidade TEXT NOT NULL,
                estado TEXT NOT NULL,
                tipo TEXT NOT NULL,
                criado_em DATE NOT NULL
            ); """)

        conn.close()

        return 'Tabela criada com sucesso.'
