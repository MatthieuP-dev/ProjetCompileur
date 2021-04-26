class Helper :

    def __init__(self):
        self.liste = []

    def replaceSpecialsChars(self, c):
        for i in self.liste :
            if self.detectTabulation(i):
                print(i)
    #permet de mettre sous forme de liste chaque ligne du fichier (je sais pas si ca va servir)
    def parserLine(self,code):
        res = ""
        for i in code:
            if(i=="\n"):
                self.liste.append(res)
                res = ""
            else:
                res = res + i
        self.liste.append(res)
        return code

    #permet de savoir si une ligne possede une tabulation ()
    def detectTabulation(self,line):
        res = 0
        for i in line :
            if i != " ":
                return False
            res+=1
        if res % 4 == 0 :
            return True