import sqlite3
import bcrypt

from .utils.message import message

class Login():

    def login(self, usuario):

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        
        for dados in cursor.execute(""" SELECT senha FROM usuarios WHERE email=?; """, (usuario["email"],)):
            if(dados):
                if bcrypt.checkpw(usuario["senha"].encode('utf8'), dados[0]):
                    return message("Login realizado com sucesso!", (40/255, 167/255, 67/255, 1))
                else:
                    return message("Senha inválida !", (220/255, 53/255, 69/255, 1))
        return message("Email/Usuario não existe!", (220/255, 53/255, 69/255, 1))