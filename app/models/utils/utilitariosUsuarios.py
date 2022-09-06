import sqlite3
from datetime import datetime
import bcrypt
import re

import utils

# password = "daniel123"
# password2 = "daniel123"

# senha = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
# print(senha)

# if bcrypt.checkpw(bytes(password2, 'utf-8'), senha):
#     print("Logado")
# else:
#     print("It Does not Match :(")

class UtilitariosUsuarios():

    def cadastrarUsuario(self, nome, senha, cpf, email, logradouro, numero, 
        complemento, bairro, cep, telefone, cidade, estado):

        self.criaTabelaUsuario()

        nome = nome.capitalize()

        senha = bcrypt.hashpw(bytes(senha, 'utf-8'), bcrypt.gensalt())

        if not self.validarCpf(cpf):
            return "Cpf inválido"
        
        if not utils.Utils.validarEmail(self.email):
            return "Email invalido"
        
        logradouro = logradouro.capitalize()

        if(len(numero) > 4):
            return "Numero da casa inválido"
        
        complemento = complemento.capitalize()

        bairro = bairro.capitalize()

        if not utils.Utils.validarCep(cep):
            return "Cep inválido"
        
        if len(telefone) > 11:
            return "Telefone inválido"
        
        cidade = cidade.capitalize()

        estado = estado.capitalize()

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO usuarios (nome, cpf, email, logradouro, numero, 
        complemento, bairro, cep, telefone, cidade, estado, criado_em)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (nome, senha, cpf, email, logradouro, numero, complemento, bairro, cep, telefone, cidade, estado, datetime.today().strftime('%d-%m-%Y')))

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
                complemento TEXT NOT NULL,
                bairro TEXT NOT NULL,
                cep TEXT NOT NULL,
                telefone TEXT NOT NULL,
                cidade TEXT NOT NULL,
                estado TEXT NOT NULL,
                criado_em DATE NOT NULL
            ); """)

        conn.close()

        return 'Tabela criada com sucesso.'

    def validarCpf(cpf):
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