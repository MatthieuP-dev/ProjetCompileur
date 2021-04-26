from . import helper
from . import constant
class Token :

    def tokenizer(self,code):
        h = helper.Helper()
        token = h.parserLine(code);
        h.replaceSpecialsChars(code)
        #return code
        #print("test")