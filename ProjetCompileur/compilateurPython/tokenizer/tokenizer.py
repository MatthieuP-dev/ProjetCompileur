from . import helper
from . import constant
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
            if constant.typeClass in t:
                tokens.append({"type": constant.typeClass})# faire ca dans parser.py

            else:
                #si le token est un main
                if constant.typeMain in t:
                    tokens.append({"type": constant.typeMain})# faire ca dans parser.py
                else:
                    #  si le token n'est pas un nombre
                    #print(t)
                    if constant.typeWord in t:
                        tokens.append({"type": constant.typeWord, "value": t})
                        #sinon c'est un nombre
                    if constant.typeNumber in t:
                        tokens.append({"type": constant.typeNumber, "value": t})
        if len(tokens) < 1:
            raise Exception(constant.errorNoTokenFound)
        return tokens
