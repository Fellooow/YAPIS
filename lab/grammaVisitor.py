# Generated from C:/Users/Asus/PycharmProjects/antlrTest\gramma.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grammaParser import grammaParser
else:
    from grammaParser import grammaParser

# This class defines a complete generic visitor for a parse tree produced by grammaParser.

class grammaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammaParser#program.
    def visitProgram(self, ctx:grammaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#stat.
    def visitStat(self, ctx:grammaParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#in_crit.
    def visitIn_crit(self, ctx:grammaParser.In_critContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#short_stat.
    def visitShort_stat(self, ctx:grammaParser.Short_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#long_stat.
    def visitLong_stat(self, ctx:grammaParser.Long_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#write_st.
    def visitWrite_st(self, ctx:grammaParser.Write_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#read_st.
    def visitRead_st(self, ctx:grammaParser.Read_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#if_st.
    def visitIf_st(self, ctx:grammaParser.If_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#in_else.
    def visitIn_else(self, ctx:grammaParser.In_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#while_st.
    def visitWhile_st(self, ctx:grammaParser.While_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#swich_st.
    def visitSwich_st(self, ctx:grammaParser.Swich_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#case_st.
    def visitCase_st(self, ctx:grammaParser.Case_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#sub_programm.
    def visitSub_programm(self, ctx:grammaParser.Sub_programmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#sub_pr_get.
    def visitSub_pr_get(self, ctx:grammaParser.Sub_pr_getContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#return_st.
    def visitReturn_st(self, ctx:grammaParser.Return_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#dupl.
    def visitDupl(self, ctx:grammaParser.DuplContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#spr_arg.
    def visitSpr_arg(self, ctx:grammaParser.Spr_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaParser#expr.
    def visitExpr(self, ctx:grammaParser.ExprContext):
        return self.visitChildren(ctx)



del grammaParser