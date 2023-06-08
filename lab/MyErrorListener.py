from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("Syntax error: line %d:%d %s" % (line, column, msg) + "\n")