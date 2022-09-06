from itertools import cycle
import re

LENGTH_CNPJ = 14

REGEX= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class Utils():

    def validarCnpj(cnpj: str) -> bool:
            if len(cnpj) != LENGTH_CNPJ:
                return False

            if cnpj in (c * LENGTH_CNPJ for c in "1234567890"):
                return False

            cnpj_r = cnpj[::-1]
            for i in range(2, 0, -1):
                cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
                dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
                if cnpj_r[i - 1:i] != str(dv % 10):
                    return False

            return True
        
    def validarEmail(email):  
    
        if(re.search(REGEX,email)):  
            return True
            
        else:  
            return False
        
    def validarCep(cep):
        if len(cep) == 8:
            return True
        else:
            return False