import sys
import re

from dist.MyParserParser import MyParserParser
from dist.MyParserVisitor import MyParserVisitor


class SemanticAnalyzer(MyParserVisitor):
    def __init__(self):
        self.symbol_table = {}
        self.functions = {}

    def visitStatement(self, ctx: MyParserParser.StatementContext):
        # print(self.symbol_table)
        if ctx.ID() is not None:
            var_name = ctx.ID().getText()
            expr = ctx.expr().getText()
            if ctx.ID() not in self.symbol_table:
                # print(var_name, expr)
                if expr[0] == '"' and expr[-1] == '"':
                    self.symbol_table[var_name] = "string"
                elif expr[0] == '[' and expr[-1] == ']':
                    self.symbol_table[var_name] = "matrix"
                elif expr[0] == '<' and expr[-1] == '>':
                    self.symbol_table[var_name] = "vector"
                elif expr.isnumeric():
                    self.symbol_table[var_name] = "integer"
                elif re.search(r'[0-9]+.[0-9]+', expr):
                    self.symbol_table[var_name] = "decimal"
                elif expr[0] == '|' and expr[-1] == '|':
                    pass
                else:
                    for op in ["+", "-", "*"]:
                        expr_lst = expr.split(op)
                        if len(expr_lst) > 1:
                            break
                    # print(expr_lst)
                    if len(expr_lst) > 1:
                        if expr_lst[0] in self.symbol_table:
                            per_type = self.symbol_table[expr_lst[0]]
                            for i, per in enumerate(expr_lst):
                                if per in self.symbol_table or per.isnumeric() or re.search(r'[0-9]+.[0-9]+', per):
                                    if per in self.symbol_table and self.symbol_table[per] in ["decimal", "integer"]:
                                        continue
                                    elif self.symbol_table[per] == per_type:
                                        continue
                                    else:
                                        print(f"Некорректное выполнение операций. Проверьте типы данных.\n{expr}")
                                        sys.exit(1)
                                else:
                                    print(f"Переменная {per} не определена!")
                                    sys.exit(1)

                            self.symbol_table[var_name] = per_type
                        else:
                            if re.search("integer\((.)*\)", expr_lst[0]):
                                self.symbol_table[var_name] = 'integer'
                            elif re.search("decimal\((.)*\)", expr_lst[0]):
                                self.symbol_table[var_name] = 'decimal'
                            elif re.search("string\((.)*\)", expr_lst[0]):
                                self.symbol_table[var_name] = 'string'
                            else:
                                # print(expr)
                                print("Выражение начинается с неопределённого символа!")
                                self.symbol_table[var_name] = " "
                    else:
                        if re.search("\w(.)*\((.)*\)", expr):
                            pass
                        elif expr not in self.symbol_table:
                            print(f"Неверное объявление выражения '{expr}' ")
                            sys.exit(1)

        # проверяем, возвращается ли существующее значение
        if ctx.RETURN() is not None:
            expr = ctx.expr().getText()
            if expr is not None and ((expr in self.symbol_table) or (expr in ["0", "1"])):
                return expr
            else:
                print(f"Возвращаемая переменная не определена!")
                sys.exit(1)

        if ctx.if_stat() is not None:
            self.visitIf_stat(ctx.if_stat())

        if ctx.declaration() is not None:
            self.visitDeclaration(ctx.declaration())

    def visitDef_fun(self, ctx: MyParserParser.Def_funContext):
        if ctx.declaration() is not None:
            self.visitDeclaration(ctx.declaration())

    def visitDeclaration(self, ctx:MyParserParser.DeclarationContext):
        if ctx.ID() is not None:
            # print(ctx.ID().getText())
            fun_name = ctx.ID().getText()
            if fun_name in ['write', 'read']:
                pass
            elif fun_name not in self.functions:
                if ctx.expr() is not None:
                    expr = ctx.expr()
                    my_str = ""
                    for ex in expr:
                        my_str += ex.getText()
                    self.functions[fun_name] = my_str

            else:
                if ctx.expr() is not None:
                    expr = ctx.expr()
                    my_str = ""
                    for ex in expr:
                        my_str += ex.getText()
                    if my_str == self.functions[fun_name]:
                        pass
                    else:
                        print("Неверное объявление функции!")
                        sys.exit(1)
