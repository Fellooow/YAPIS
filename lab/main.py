from antlr4 import *
from grammaLexer import grammaLexer
from grammaParser import grammaParser
from MyErrorListener import MyErrorListener
from MyVisitor import MyVisitor


def main():
    input_stream = FileStream('test.txt', encoding='utf8')
    lexer = grammaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammaParser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())

    tree = parser.program()
    visitor = MyVisitor()
    output = visitor.visit(tree)
    # print('main',visitor.main_dict)


if __name__ == '__main__':
    main()