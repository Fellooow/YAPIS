from antlr4 import *
import re
from grammaVisitor import grammaVisitor
from grammaParser import grammaParser

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def print_msg(self):
        print(self.msg)
class MyVisitor(grammaVisitor):

    main_dict = {}
    sub_dict = {}

    def visitIn_crit(self, ctx:grammaParser.In_critContext):
        if ctx.LESS() != None:
            if isinstance(self.visitExpr(ctx.expr(0)), int) and isinstance(self.visitExpr(ctx.expr(1)), int):
                if self.visitExpr(ctx.expr(0)) < self.visitExpr(ctx.expr(1)):
                    return True
                else:
                    return False
            elif isinstance(self.visitExpr(ctx.expr(0)), str) and isinstance(self.visitExpr(ctx.expr(1)), str):
                if len(self.visitExpr(ctx.expr(0))) < len(self.visitExpr(ctx.expr(1))):
                    return True
                else:
                    return False
            elif isinstance(self.visitExpr(ctx.expr(0)), str) and isinstance(self.visitExpr(ctx.expr(1)), int):
                if len(self.visitExpr(ctx.expr(0))) < self.visitExpr(ctx.expr(1)):
                    return True
                else:
                    return False
            elif isinstance(self.visitExpr(ctx.expr(0)), int) and isinstance(self.visitExpr(ctx.expr(1)), str):
                if self.visitExpr(ctx.expr(0)) < len(self.visitExpr(ctx.expr(1))):
                    return True
                else:
                    return False
            else:
                raise MyError ("неверный тип переменных")
        if ctx.MORRE() != None:
            if isinstance(self.visitExpr(ctx.expr(0)), int) and isinstance(self.visitExpr(ctx.expr(1)), int):
                if self.visitExpr(ctx.expr(0)) == self.visitExpr(ctx.expr(1)):
                    return True
                else:
                    return False
            if isinstance(self.visitExpr(ctx.expr(0)), str) and isinstance(self.visitExpr(ctx.expr(1)), str):
                if len(self.visitExpr(ctx.expr(0))) == len(self.visitExpr(ctx.expr(1))):
                    return True
                else:
                    return False
            if isinstance(self.visitExpr(ctx.expr(0)), str) and isinstance(self.visitExpr(ctx.expr(1)), int):
                if len(self.visitExpr(ctx.expr(0))) == self.visitExpr(ctx.expr(1)):
                    return True
                else:
                    return False
            if isinstance(self.visitExpr(ctx.expr(0)), int) and isinstance(self.visitExpr(ctx.expr(1)), str):
                if len(self.visitExpr(ctx.expr(0))) == len(self.visitExpr(ctx.expr(1))):
                    return True
                else:
                    return False
            else:
                raise MyError("неверный тип переменных")
        if ctx.COMPR() != None:
            if isinstance(self.visitExpr(ctx.expr(0)), int) and isinstance(self.visitExpr(ctx.expr(1)), int):
                if self.visitExpr(ctx.expr(0)) > self.visitExpr(ctx.expr(1)):
                    return True
                else:
                    return False
            if isinstance(self.visitExpr(ctx.expr(0)), str) and isinstance(self.visitExpr(ctx.expr(1)), str):
                if len(self.visitExpr(ctx.expr(0))) > len(self.visitExpr(ctx.expr(1))):
                    return True
                else:
                    return False
            if isinstance(self.visitExpr(ctx.expr(0)), str) and isinstance(self.visitExpr(ctx.expr(1)), int):
                if len(self.visitExpr(ctx.expr(0))) > self.visitExpr(ctx.expr(1)):
                    return True
                else:
                    return False
            if isinstance(self.visitExpr(ctx.expr(0)), int) and isinstance(self.visitExpr(ctx.expr(1)), str):
                if len(self.visitExpr(ctx.expr(0))) > len(self.visitExpr(ctx.expr(1))):
                    return True
                else:
                    return False
            else:
                raise MyError("неверный тип переменных")

    def visitIf_st(self, ctx: grammaParser.If_stContext):
        if ctx.in_crit() != None:
            if self.visitIn_crit(ctx.in_crit()):
                for stat in ctx.stat():
                    self.visitStat(stat)
            if not self.visitIn_crit(ctx.in_crit()) and ctx.ELSE() != None:
                self.visitStat(ctx.in_else())
        else:
            raise MyError("неверный if ()")
    '''
        def visitIf_st(self, ctx:grammaParser.If_stContext):
        if self.visitIn_crit(ctx.in_crit()):
            self.visitStat(ctx.stat())
        if not self.visitIn_crit(ctx.in_crit()) and ctx.ELSE() != None:
            self.visitStat(ctx.in_else())
    def visitWhile_st(self, ctx:grammaParser.While_stContext):
        print(ctx.getText())
        if ctx.in_crit() != None:
            print(ctx.in_crit().getText())
            if ctx.in_crit().LESS != None:
                if isinstance(self.visitExpr(ctx.in_crit().expr(0)), int) and isinstance(self.visitExpr(ctx.in_crit().expr(1)), int):
                    tmp = self.visitExpr(ctx.in_crit().expr(0))
                    while tmp < self.visitExpr(ctx.in_crit().expr(1)):
                        for i in range(len(ctx.stat())):
                            self.visitStat(ctx.stat(i))
                        tmp += 1
    '''

    def visitLong_stat(self, ctx:grammaParser.Long_statContext):
        if len(ctx.expr()) == len(ctx.ID()):
            for i in range(len(ctx.expr())):
                if self.main_dict.get(ctx.ID(i).getText()) != None:
                    raise MyError("переменная '" + ctx.ID(i).getText() + "' уже есть")
                if ctx.expr(i) != None:
                    expr = self.visitExpr(ctx.expr(i))
                    self.main_dict[ctx.ID(i).getText()] = {'value': self.visitExpr(ctx.expr(i)),
                                                          'type': type(self.visitExpr(ctx.expr(i)))}
        elif len(ctx.expr()) != len(ctx.ID()):
            raise MyError("неверная заппись: " + ctx.getText())

    def visitShort_stat(self, ctx: grammaParser.Short_statContext):
       # if self.main_dict.get(ctx.ID().getText()) != None:
         #   print(ctx.expr().getText())
        #    raise MyError("переменная'" + ctx.ID().getText() + "' уже объявлена")
        if ctx.expr() != None:
            self.main_dict[ctx.ID().getText()] = {'value' : self.visitExpr(ctx.expr()), 'type' : type(self.visitExpr(ctx.expr()))}
    def visitExpr(self, ctx:grammaParser.ExprContext):
        if ctx.ID() != None:
            if ctx.ID().getText() not in self.main_dict.keys():
                raise MyError("переменная '" + ctx.ID().getText() + "' не объявлена")
            return self.main_dict[ctx.ID().getText()]['value']
        elif ctx.INT() != None:
            return int(ctx.INT().getText())
        elif ctx.CHAR() != None:
            return chr(ctx.CHAR().getText())
        elif ctx.STR() != None:
            return str(ctx.STR().getText()[1:-1])
        elif ctx.PLUS() != None:
            if isinstance(self.visitExpr(ctx.expr(0)), int) and isinstance(self.visitExpr(ctx.expr(1)), int):
                return self.visitExpr(ctx.expr(0)) + self.visitExpr((ctx.expr(1)))
            elif isinstance(self.visitExpr(ctx.expr(0)), str) and isinstance(self.visitExpr(ctx.expr(1)), str):
                return self.visitExpr(ctx.expr(0)) + self.visitExpr((ctx.expr(1)))
            elif type(self.visitExpr(ctx.expr(0))) != type(self.visitExpr(ctx.expr(1))):
                raise MyError("переменные должны быть одного типа: " + ctx.getText())
        elif ctx.DIFFER() != None:
            if isinstance(self.visitExpr(ctx.expr(0)), int) and isinstance(self.visitExpr(ctx.expr(1)), int):
                return self.visitExpr(ctx.expr(0)) - self.visitExpr((ctx.expr(1)))
            if isinstance(self.visitExpr(ctx.expr(0)), str) and isinstance(self.visitExpr(ctx.expr(1)), int):
                return len(self.visitExpr(ctx.expr(0))) - self.visitExpr((ctx.expr(1)))
            if isinstance(self.visitExpr(ctx.expr(0)), int) and isinstance(self.visitExpr(ctx.expr(1)), str):
                return self.visitExpr(ctx.expr(0)) - len(self.visitExpr((ctx.expr(1))))
            if isinstance(self.visitExpr(ctx.expr(0)), str) and isinstance(self.visitExpr(ctx.expr(1)), str):
                return len(self.visitExpr(ctx.expr(0))) - len(self.visitExpr((ctx.expr(1))))
            else:
                raise MyError("неверный тип переменных: " + ctx.getText())

        elif ctx.MULTI() != None:
            if isinstance(self.visitExpr(ctx.expr(0)), int) or isinstance(self.visitExpr(ctx.expr(1)), int):
                return self.visitExpr(ctx.expr(0)) * self.visitExpr((ctx.expr(1)))
            else:
                raise MyError("str * str: " + ctx.getText())

        elif ctx.QUONTIENT() != None:
            if isinstance(self.visitExpr(ctx.expr(0)), int) and isinstance(self.visitExpr(ctx.expr(1)), int):
                return self.visitExpr(ctx.expr(0)) // self.visitExpr((ctx.expr(1)))
            if isinstance(self.visitExpr(ctx.expr(0)), str) and isinstance(self.visitExpr(ctx.expr(1)), int):
                return len(self.visitExpr(ctx.expr(0))) // self.visitExpr((ctx.expr(1)))
            if isinstance(self.visitExpr(ctx.expr(0)), int) and isinstance(self.visitExpr(ctx.expr(1)), str):
                return self.visitExpr(ctx.expr(0)) // len(self.visitExpr((ctx.expr(1))))
            if isinstance(self.visitExpr(ctx.expr(0)), str) and isinstance(self.visitExpr(ctx.expr(1)), str):
                return len(self.visitExpr(ctx.expr(0))) // len(self.visitExpr((ctx.expr(1))))
            else:
                raise MyError("неверный тип переменных: " + ctx.getText())

    def visitSpr_arg(self, ctx:grammaParser.Spr_argContext):
        if ctx.ID() != None:
            if ctx.ID().getText() not in self.main_dict.keys():
                raise MyError("переменная '" + ctx.ID().getText() + "' не объявлена")
            return self.main_dict[ctx.ID().getText()]['value']
        elif ctx.INT() != None:
            return int(ctx.INT().getText())
        elif ctx.STR() != None:
            return str(ctx.STR().getText())[1:-1]
        elif ctx.CHAR() != None:
            return chr(ctx.CHAR().getText())
        else:
            raise MyError("неподдерживаемые тип данных")


    def visitSub_pr_get(self, ctx:grammaParser.Sub_pr_getContext):
        #if self.main_dict.get(ctx.ID(0).getText()) != None:
         #   raise MyError("переменная '" + ctx.ID().getText() + "' уже объявлена")
        if ctx.ID(1).getText() == "pr_substr":
            if len(ctx.spr_arg()) == 2 and isinstance(self.visitExpr(ctx.spr_arg(0)), str) and isinstance(self.visitExpr(ctx.spr_arg(1)), str):
                if self.visitExpr(ctx.spr_arg(0)) in self.visitExpr(ctx.spr_arg(1)):
                    self.main_dict[ctx.ID(0).getText()] = {'value':self.visitExpr(ctx.spr_arg(0)), 'type': type(self.visitExpr(ctx.spr_arg(0)))}
                else:
                    self.main_dict[ctx.ID(0).getText()] = {'value': None,
                                                           'type': None}
            else:
                raise MyError("неверные аргументы для функции" + ctx.ID(2).getText())

        elif ctx.ID(1).getText() == "pr_slise":
            if len(ctx.spr_arg()) == 3 and isinstance(self.visitExpr(ctx.spr_arg(0)), str) and isinstance(self.visitExpr(ctx.spr_arg(1)), int) and isinstance(self.visitExpr(ctx.spr_arg(2)), int) and self.visitExpr(ctx.spr_arg(1)) < self.visitExpr(ctx.spr_arg(2)):
                if self.visitExpr(ctx.spr_arg(1)) >= 0 and self.visitExpr(ctx.spr_arg(1)) <=  len(self.visitExpr(ctx.spr_arg(0))):
                    if self.visitExpr(ctx.spr_arg(2)) >= 0 and self.visitExpr(ctx.spr_arg(2)) <= len(
                            self.visitExpr(ctx.spr_arg(0))):
                        self.main_dict[ctx.ID(0).getText()] = {'value':self.visitExpr(ctx.spr_arg(0))[self.visitExpr(ctx.spr_arg(1)):self.visitExpr(ctx.spr_arg(2))], 'type': type(self.visitExpr(ctx.spr_arg(0)))}
                    else:
                        raise MyError("втрой аргумент вышел за рамки" + ctx.spr_arg(1).getText())
                else:
                    raise MyError("первый аргумент вышел за рамки" + ctx.spr_arg(1).getText())
            else:
                raise MyError("неверные аргументы для функции" + ctx.ID(2).getText())

        elif ctx.ID(1).getText() == "pr_replace":
            if len(ctx.spr_arg()) == 3 and isinstance(self.visitExpr(ctx.spr_arg(0)), str) and isinstance(
                self.visitExpr(ctx.spr_arg(1)), str) and isinstance(self.visitExpr(ctx.spr_arg(2)), str):
                if len( self.visitExpr(ctx.spr_arg(1))) < len(self.visitExpr(ctx.spr_arg(0))) and len( self.visitExpr(ctx.spr_arg(2))) < len(self.visitExpr(ctx.spr_arg(0))):
                    if self.visitExpr(ctx.spr_arg(1)) in self.visitExpr(ctx.spr_arg(0)):
                        p = re.compile(self.visitExpr(ctx.spr_arg(1)))
                        self.main_dict[ctx.ID(0).getText()] = {'value': p.sub(self.visitExpr(ctx.spr_arg(2)),self.visitExpr(ctx.spr_arg(0))),
                                                               'type': type(self.visitExpr(ctx.spr_arg(0)))}
                    else:
                        raise Myerror("Error")
                else:
                    raise MyError("размер подстроки не может быть больше строки" )
            else:
                raise MyError("неверные аргументы для функции")

        elif ctx.ID(1).getText() == "pr_size":
            if len(ctx.spr_arg()) == 1:
                if isinstance(self.visitExpr(ctx.spr_arg(0)), str):
                    self.main_dict[ctx.ID(0).getText()] = {
                        'value': len(self.visitExpr(ctx.spr_arg(0))),
                        'type': type(len(self.visitExpr(ctx.spr_arg(0))))}
                else:
                    raise MyError("аргумент обязан быть строкой" + ctx.ID(2).getText())
            else:
                raise MyError("необходим лишь 1 аргумент" + ctx.ID(2).getText())

        elif ctx.ID(1).getText() == "pr_ind":
            if len(ctx.spr_arg()) == 2 and isinstance(self.visitExpr(ctx.spr_arg(0)), str) and isinstance(
                self.visitExpr(ctx.spr_arg(1)), int):
                if self.visitExpr(ctx.spr_arg(1)) < len(self.visitExpr(ctx.spr_arg(0))) and self.visitExpr(ctx.spr_arg(1)) >= 0:
                    self.main_dict[ctx.ID(0).getText()] = {'value': self.visitExpr(ctx.spr_arg(0))[self.visitExpr(ctx.spr_arg(1))],
                                                               'type': type(self.visitExpr(ctx.spr_arg(0)))}
                else:
                    raise MyError("индекс за рамками размера строки" )
            else:
                raise MyError("неверные аргументы для функции")
        else:
            d = {}
            in_sub = {}
            for i in range(len(ctx.spr_arg())):
                if  self.visitExpr(ctx.spr_arg(i)) == None:
                    raise MyError("аргумент без значения")
                d[i] = {'value': self.visitExpr(ctx.spr_arg(i)),'type': type(self.visitExpr(ctx.spr_arg(i)))}
            #print(self.sub_dict.keys())
            if ctx.ID(1).getText() not in self.sub_dict.keys():
                in_sub[ctx.ID(0).getText()] = d
                #print(self.sub_dict)
                self.sub_dict[ctx.ID(1).getText()] = in_sub
            else:
                self.sub_dict[ctx.ID(1).getText()][ctx.ID(0).getText()] = d
            self.main_dict[ctx.ID(0).getText()] = {'value':None,'type': None}
            #print(self.sub_dict)

    def visitSub_programm(self, ctx:grammaParser.Sub_programmContext):
        tmp = {}
        for k in self.main_dict.keys():
            tmp[k] = {'value': self.main_dict[k]['value'], 'type': self.main_dict[k]['type']}
        if ctx.ID().getText() not in self.sub_dict.keys():
            raise MyError("необходимо объявить перед реализацией")
        for key in self.sub_dict[ctx.ID().getText()].keys():
            self.main_dict.clear()
            if len(self.sub_dict[ctx.ID().getText()][key].keys()) != len(ctx.spr_arg()):
                raise MyError("неверное количество аргументов")
            for n in range(len(ctx.spr_arg())):
                self.main_dict[ctx.spr_arg(n).getText()] = self.sub_dict[ctx.ID().getText()][key][n]
            for i in range(len(ctx.stat())):
                self.visitStat(ctx.stat(i))
                if i == len(ctx.stat()) - 1:
                    rez = self.visitStat(ctx.stat(i))
                    tmp[key] = {'value': rez, 'type': type(rez)}
        self.main_dict = tmp


    def visitWrite_st(self, ctx:grammaParser.Write_stContext):
        if ctx.ID() != None:
            if ctx.ID().getText() not in self.main_dict.keys():
                raise MyError("переменная для arg для write(arg) не существует")
            else:
                print(self.main_dict[ctx.ID().getText()]['value'])
        else:
            raise MyError("в write(arg) arg обязано быть переменной")

    def visitRead_st(self, ctx:grammaParser.Read_stContext):
        if ctx.ID() != None:
            if self.main_dict.get(ctx.ID().getText()) != None:
                raise MyError("переменная  '" + ctx.ID().getText() + "' уже существует")
            print("введите значение для " + ctx.ID().getText())
            read = input()
            if read.isdigit():
                read = int(read)
                self.main_dict[ctx.ID().getText()] = {'value': read, 'type': type(read)}
            elif isinstance(read, (str, chr)):
                self.main_dict[ctx.ID().getText()] = {'value': read,'type': type(read)}
            else:
                raise MyError("тип должен быть: chr, int, str")
        else:
            raise MyError("выражение обязано иметь вид: a = read()")

    def visitReturn_st(self, ctx: grammaParser.Return_stContext):
        return  self.visitExpr(ctx.expr())


    def visitSwich_st(self, ctx:grammaParser.Swich_stContext):
        tmp = False
        if not isinstance(self.visitExpr(ctx),int):
            raise MyError("тип обязан быть int")
        for case in range(len(ctx.case_st())):
            if self.main_dict[ctx.ID().getText()]['value'] == int(ctx.case_st(case).INT().getText()):
                tmp = True
                self.visitCase_st(ctx.case_st(case))
            if case == len(ctx.case_st()) - 1 and tmp == False:
                raise MyError("case не существует")
    # Visit a parse tree produced by grammaParser#case_st.
    def visitCase_st(self, ctx:grammaParser.Case_stContext):
        for st in ctx.stat():
            self.visitStat(st)