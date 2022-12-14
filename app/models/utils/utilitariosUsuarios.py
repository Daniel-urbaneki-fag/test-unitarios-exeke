import sqlite3
from datetime import datetime
import bcrypt
import re

import utils

class UtilitariosUsuarios():

    def __init__(self):
        self.criaTabelaUsuario()

    def cadastrarUsuario(self, usuario):

        self.criaTabelaUsuario()

        usuario["nome"] = usuario["nome"].capitalize()

        usuario["senha"] = bcrypt.hashpw(bytes(usuario["senha"], 'utf-8'), bcrypt.gensalt())

        if not self.validarCpf(usuario["cpf"]):
            return "Cpf inválido"
        
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        
        for dados in cursor.execute(""" SELECT * FROM usuarios WHERE cpf=?; """, (usuario["cpf"],)):
            if(dados):
               return "O cpf já está cadastrado !"

        if not utils.Utils.validarEmail(usuario["email"]):
            return "Email invalido"
        
        usuario["logradouro"] = usuario["logradouro"].capitalize()

        if(len(usuario["numero"]) > 4):
            return "Numero da casa inválido"
        
        usuario["complemento"] = usuario["complemento"].capitalize()

        usuario["bairro"]  = usuario["bairro"].capitalize()

        if not utils.Utils.validarCep(usuario["cep"]):
            return "Cep inválido"
        
        if len(usuario["telefone"]) > 11:
            return "Telefone inválido"
        
        usuario["cidade"] = usuario["cidade"].capitalize()

        usuario["estado"] = usuario["estado"].capitalize()

        cursor.execute("""INSERT INTO usuarios (nome, senha, cpf, email, logradouro, numero, 
        complemento, bairro, cep, telefone, cidade, estado, criado_em)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (usuario["nome"], usuario["senha"], usuario["cpf"], usuario["email"], usuario["logradouro"], usuario["numero"], usuario["complemento"], usuario["bairro"], usuario["cep"], usuario["telefone"], usuario["cidade"], usuario["estado"], datetime.today().strftime('%d-%m-%Y')))

        conn.commit()
        conn.close()
        return "Usuário cadastrado com sucesso!"
    
    def atualizarUsuario(self, updateUsuario):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        for dados in cursor.execute(""" SELECT * FROM usuarios WHERE cpf=?; """, (updateUsuario['alvo'],)):
            if(dados):
                usuario = {
                    "nome" : dados[1],
                    "senha" : dados[2],
                    "cpf" : dados[3],
                    "email" : dados[4],
                    "logradouro" : dados[5],
                    "numero" : dados[6],
                    "complemento" : dados[7],
                    "bairro" : dados[8],
                    "cep" : dados[9],
                    "telefone" : dados[10],
                    "cidade" : dados[11],
                    "estado" : dados[12],
                }

                for chave, valor in updateUsuario.items():
                    if valor != "":
                        if chave == "nome" or chave == "logradouro" or chave == "complemento" or chave == "bairro" or chave == "cidade" or chave == "estado":
                            usuario[chave] = valor.capitalize()
                        if chave == "senha":
                            usuario[chave] =  bcrypt.hashpw(bytes(valor, 'utf-8'), bcrypt.gensalt())
                        if chave == "cpf":
                            if not self.validarCpf(valor):
                                return "Cpf inválido"
                            usuario[chave] = valor
                        if chave == "email":
                            if not utils.Utils.validarEmail(usuario["email"]):
                                return "Email invalido"
                            usuario[chave] = valor
                        if chave == "numero":
                            if(len(valor) > 4):
                                return "Numero da casa inválido"
                            usuario[chave] = valor
                        if chave == "cep":
                            if not utils.Utils.validarCep(usuario["cep"]):
                                return "Cep inválido"
                            usuario[chave] = valor
                        if chave == "telefone":
                            if(len(valor) > 11):
                                return "Telefone inválido"
                            usuario[chave] = valor

                cursor.execute(""" UPDATE usuarios SET 
                                nome = ?,
                                senha = ?,
                                cpf = ?,
                                email = ?,
                                logradouro = ?,
                                numero = ?,
                                complemento = ?,
                                bairro = ?,
                                cep = ?,
                                telefone = ?,
                                cidade = ?,
                                estado = ?
                                WHERE cpf=?
                                ;""",
                    (usuario["nome"], usuario["senha"], usuario["cpf"], usuario["email"],
                        usuario["logradouro"], usuario["numero"], usuario["complemento"], usuario["bairro"],
                        usuario["cep"], usuario["telefone"], usuario["cidade"], usuario["estado"],
                        updateUsuario['alvo']))

                conn.commit()
                
                conn.close()
            
                return "Atualizado com sucesso."

        return "Não existe usuario para a atualização !"
    
    def excluirUsuario(self, cpf):
        conn = sqlite3.connect('db.sqlite3')
        
        cursor = conn.cursor()

        for dados in cursor.execute(""" SELECT * FROM usuarios WHERE cpf=?; """, (cpf,)):
            if(dados):
                cursor.execute("DELETE FROM usuarios WHERE cpf=?;", (cpf,))

                conn.commit()
                
                conn.close()
            
                return "Dados EXCLUIDOS com sucesso."

        return "Não existe usuario para a exclusão !"
    
    def lerTabelaUsuarios(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        response = []

        for dados in cursor.execute(""" SELECT id, nome, email, telefone FROM usuarios;"""):
            dados = {"id" : dados[0], "nome" : dados[1], "email" : dados[2], "telefone" : dados[3]}
            response.append(dados)
        return ['Leitura de Usuarios.', response]

    def criaTabelaUsuario(self,):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                senha TEXT NOT NULL,
                cpf TEXT NOT NULL,
                email TEXT NOT NULL,
                logradouro TEXT NOT NULL,
                numero TEXT NOT NULL,
                complemento TEXT,
                bairro TEXT NOT NULL,
                cep TEXT NOT NULL,
                telefone TEXT NOT NULL,
                cidade TEXT NOT NULL,
                estado TEXT NOT NULL,
                criado_em DATE NOT NULL
            ); """)

        conn.close()

        return 'Tabela criada com sucesso.'

    def validarCpf(self, cpf):
        # Verifica a formatação do CPF
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            return False

        # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True