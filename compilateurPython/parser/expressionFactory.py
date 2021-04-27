


function variableDeclaration(tokens, start){
    if(tokens[start+1].type != constTokens.typeWord) throw constParser.errorMissingWord;
    let variableName= tokens[start+1].value;
    return {type: constParser.expressionDeclaration, variableName: variableName};
}

def variableDeclaration(tokens, start):
    