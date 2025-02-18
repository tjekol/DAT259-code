# Generated from EDBS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EDBSParser import EDBSParser
else:
    from EDBSParser import EDBSParser

# This class defines a complete generic visitor for a parse tree produced by EDBSParser.

class EDBSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EDBSParser#program.
    def visitProgram(self, ctx:EDBSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#statement.
    def visitStatement(self, ctx:EDBSParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#fin_stmt.
    def visitFin_stmt(self, ctx:EDBSParser.Fin_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#write_stmt.
    def visitWrite_stmt(self, ctx:EDBSParser.Write_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#write_arg.
    def visitWrite_arg(self, ctx:EDBSParser.Write_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#calc_stmt.
    def visitCalc_stmt(self, ctx:EDBSParser.Calc_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#cond_stmt.
    def visitCond_stmt(self, ctx:EDBSParser.Cond_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#bool_op.
    def visitBool_op(self, ctx:EDBSParser.Bool_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#div.
    def visitDiv(self, ctx:EDBSParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#add.
    def visitAdd(self, ctx:EDBSParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#sub.
    def visitSub(self, ctx:EDBSParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#not.
    def visitNot(self, ctx:EDBSParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#len.
    def visitLen(self, ctx:EDBSParser.LenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#null.
    def visitNull(self, ctx:EDBSParser.NullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#bool.
    def visitBool(self, ctx:EDBSParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#mul.
    def visitMul(self, ctx:EDBSParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#lit.
    def visitLit(self, ctx:EDBSParser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#var.
    def visitVar(self, ctx:EDBSParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#nested.
    def visitNested(self, ctx:EDBSParser.NestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#str_op.
    def visitStr_op(self, ctx:EDBSParser.Str_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#len_op.
    def visitLen_op(self, ctx:EDBSParser.Len_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#list_op.
    def visitList_op(self, ctx:EDBSParser.List_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#call_mod_op.
    def visitCall_mod_op(self, ctx:EDBSParser.Call_mod_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#def_module_op.
    def visitDef_module_op(self, ctx:EDBSParser.Def_module_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#while_stmt.
    def visitWhile_stmt(self, ctx:EDBSParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#update_stmt.
    def visitUpdate_stmt(self, ctx:EDBSParser.Update_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#read_assgn.
    def visitRead_assgn(self, ctx:EDBSParser.Read_assgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#read_file_stmt.
    def visitRead_file_stmt(self, ctx:EDBSParser.Read_file_stmtContext):
        return self.visitChildren(ctx)



del EDBSParser