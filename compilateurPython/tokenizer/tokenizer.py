from . import helper
from . import constantToken
import re

class Token :

    def tokenizer(self,c):
        #line = re.split('}|{',l)
        h = helper.Helper()

        _tokens = h.replaceSpecialsChars(c)
        _tokens = re.split('{|}|        ',_tokens)
        
        #print(_tokens)
        tokens = []
        for i in range(0, len(_tokens)):
            t = _tokens[i]
            
           
            #si le token est une classe
            if constantToken.typeClass in t:
                tokens.append({"type": constantToken.typeClass})# faire ca dans parser.py

            else:
                #si le token est un main
                if constantToken.typeMain in t:
                    tokens.append({"type": constantToken.typeMain})# faire ca dans parser.py
                else:
                    #  si le token n'est pas un nombre
                    #print(t)
                    if constantToken.typeWord in t:
                        tokens.append({"type": constantToken.typeWord, "value": t})
                        #sinon c'est un nombre
                    if constantToken.typeNumber in t:
                        tokens.append({"type": constantToken.typeNumber, "value": t})
        if len(tokens) < 1:
            raise Exception(constant.errorNoTokenFound)

        return tokens
