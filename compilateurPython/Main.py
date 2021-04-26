from tokenizer import tokenizer
file = open("test.py","r")
#print(file.read())
#for i in file.read():
#    print(i)

token = tokenizer.Token()
token.tokenizer(file.read())