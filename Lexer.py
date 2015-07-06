import re
class Token:
    NUMBER = "NUMBER"
    STRING = "STRING"
    PUNCT = "PUNCT"
    EMPTY = "EMPTY"
    EOF = "EOF"
    
    def __init__(self, lineNumber, value, type):
        self.__lineNumber = lineNumber
        self.__value = value
        self.__type = type

    def isIdentifier(self):
        return self.__type == Token.IDENTIFIER

    def isNumber(self):
        return self.__type == Token.NUMBER

    def isString(self):
        return self.__type == Token.STRING

    def isEmpty(self):
        return self.__type == Token.EMPTY

    def isEof(self):
        return self.__type == Token.EOF

    def getValue(self):
        return self.__value

    def getType(self):
        return self.__type





class Lexer:
    symbolRegrex = "([A-Z_a-z][A-Z_a-z0-9]*)|([1-9][0-9]*)|(==|>=|<=|=|\+|\-|>|<|\{|\})|{\".*\"}|(\s+)"
    def __init__(self, testStr):
        self.__regrex = re.compile(Lexer.symbolRegrex)
        self.__code = testStr
        self.__startPosition = 0
        self.__iter = 0

    def getToken(self):
        if not self.__iter:
            self.__iter = self.__regrex.finditer(self.__code)
            if not self.__iter:
                return Token(0,0,Token.EOF)
        try:
            result = self.__iter.next()
            if result:
                if result.group(4):
                    return Token(0, 0, Token.EMPTY)
                elif result.group(1):
                    return Token(0, result.group(0), Token.STRING)
                elif result.group(2):
                    return Token(0, result.group(0), Token.NUMBER)
                elif result.group(3):
                    return Token(0, result.group(0), Token.PUNCT)
                else:
                    return Token(0,0,Token.EOF)
        except StopIteration:
            return Token(0,0,Token.EOF)
        

def main():
    code = '''
while i < 10 {
    sum = sum + i
    i = i + 1
}
sum
'''
    l = Lexer(code)
    while True:
        token = l.getToken()
        if token.isEof():
            return
        if token.isEmpty():
            continue

        print token.getType(), token.getValue()
        
main()
