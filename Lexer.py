import re
class Token:
    NUMBER = 0
    IDENTIFIER = 1
    STRING = 2
    EOF = 3
    
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

    def isEof(self):
        return self.__type == Token.EOF

    def getValue(self):
        return self.__value





class Lexer:
    symbol = "([A-Z_a-z][A-Z_a-z0-9]*)|([1-9][0-9]*)|(==|>=|<=|>|<|\{|\})|{\".*\"}|(\s+)"
    def __init__(self, testStr):
        self.__regrex = re.compile(Lexer.symbol)
        self.__code = testStr
        self.__startPosition = 0

    def printResult(self):
        result = self.regrex.match(self.code)
        if result:
            str= result.group(4)
            print str
            print len(str)
            if len(str.strip()) == 0:
                print "spaces"
            else:
                print str
        else:
            print "fuck"

    



l = Lexer(" 1\"\"abc\"   { <9abc")
l.printResult()
        
