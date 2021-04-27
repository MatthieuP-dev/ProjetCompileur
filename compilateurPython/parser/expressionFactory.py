import constantParser as consParser
import sys 

sys.path.append('../tokenizer')

import constantToken as consTokens

def variableDeclaration(tokens, start):
    if tokens[start+1].typpe != consTokens.typeWord:
        raise consParser.errorMissingWord
    variableName = tokens[start+1].value
    return {type : constParser.expressionDeclaration, variableName: variableName}

def variableAffectation(tokens, start):
    if tokens[start-1].type != consTokens.typeWord:
        raise consParser.errorMissingWord
    if tokens[start+1].type==consTokens.typeNumber:
        variableValue = tokens[start+1]
    else:
        if tokens[start+1].type==consTokens.symboleQuotationMark:
            variableValue= helper.searchString(tokens, start+1)
    
    return {type: consParser.expressionAffectation, variableName: variableName, variableValue: variableValue}



