from tokenizer import tokenizer
from tokenizer import helper
import re
#file = open("Test.java","r")

with open('Test.java') as file:
    token = tokenizer.Token()
    print(token.tokenizer(file.read()))
