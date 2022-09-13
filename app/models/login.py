import sqlite3
import bcrypt

class Login():

    def login(self, usuario):

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        # password = "daniel123"
        # password2 = "daniel123"

        # senha = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
        # print(senha)

        # if bcrypt.checkpw(bytes(password2, 'utf-8'), senha):
        #     print("Logado")
        # else:
        #     print("It Does not Match :(")
        
        for dados in cursor.execute(""" SELECT senha FROM usuarios WHERE email=?; """, (usuario["email"],)):
            if(dados):
                if bcrypt.checkpw(usuario["senha"].encode('utf8'), dados[0]):
                    return "Login realizado com sucesso!"
                else:
                    return "Senha inválida !"
        
        return "Email/Usuario não existe!"