import constantParser as constParser
import sys 

sys.path.append('../tokenizer')

import constantToken as constTokens

class parser:

    def parser(self, tokens):
        AST= []
        for i in range(0, len(tokens)):
            expression = None

            if(tokens[i].type == constTokens.typeWord and constParser.declarationVariable.indexOf(tokens[i].value)!=-1)
                expression= factory.create(constParser.expressionDeclaration, tokens, i)
                i = i+1
            elif tokens[i].type == constTokens.symboleEqual:
                    expression = factory.create(constParser.expressionAffectation, tokens, i)
                if expression.variableValue.type== constTokens.typeNumber :
                    i = i+1
                else
                    i = expression.variableValue.end
            elif (i<tokens.length-1 and tokens[i].type == constTokens.typeWord and tokens[i+1].type==constTokens.symbolePoint)
                expression = factory.create(constParser.expressionMethodCall, tokens, i)
                i= expression.end
                
                if(expression)
                    AST.append(expression)
                else:
                    AST.append(tokens[i])
        return AST
