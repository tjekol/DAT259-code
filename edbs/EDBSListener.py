# Generated from EDBS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EDBSParser import EDBSParser
else:
    from EDBSParser import EDBSParser

# This class defines a complete listener for a parse tree produced by EDBSParser.
class EDBSListener(ParseTreeListener):

    # Enter a parse tree produced by EDBSParser#program.
    def enterProgram(self, ctx:EDBSParser.ProgramContext):
        pass

    # Exit a parse tree produced by EDBSParser#program.
    def exitProgram(self, ctx:EDBSParser.ProgramContext):
        pass


    # Enter a parse tree produced by EDBSParser#statement.
    def enterStatement(self, ctx:EDBSParser.StatementContext):
        pass

    # Exit a parse tree produced by EDBSParser#statement.
    def exitStatement(self, ctx:EDBSParser.StatementContext):
        pass


    # Enter a parse tree produced by EDBSParser#fin_stmt.
    def enterFin_stmt(self, ctx:EDBSParser.Fin_stmtContext):
        pass

    # Exit a parse tree produced by EDBSParser#fin_stmt.
    def exitFin_stmt(self, ctx:EDBSParser.Fin_stmtContext):
        pass


    # Enter a parse tree produced by EDBSParser#write_stmt.
    def enterWrite_stmt(self, ctx:EDBSParser.Write_stmtContext):
        pass

    # Exit a parse tree produced by EDBSParser#write_stmt.
    def exitWrite_stmt(self, ctx:EDBSParser.Write_stmtContext):
        pass


    # Enter a parse tree produced by EDBSParser#write_arg.
    def enterWrite_arg(self, ctx:EDBSParser.Write_argContext):
        pass

    # Exit a parse tree produced by EDBSParser#write_arg.
    def exitWrite_arg(self, ctx:EDBSParser.Write_argContext):
        pass


    # Enter a parse tree produced by EDBSParser#calc_stmt.
    def enterCalc_stmt(self, ctx:EDBSParser.Calc_stmtContext):
        pass

    # Exit a parse tree produced by EDBSParser#calc_stmt.
    def exitCalc_stmt(self, ctx:EDBSParser.Calc_stmtContext):
        pass


    # Enter a parse tree produced by EDBSParser#cond_stmt.
    def enterCond_stmt(self, ctx:EDBSParser.Cond_stmtContext):
        pass

    # Exit a parse tree produced by EDBSParser#cond_stmt.
    def exitCond_stmt(self, ctx:EDBSParser.Cond_stmtContext):
        pass


    # Enter a parse tree produced by EDBSParser#bool_op.
    def enterBool_op(self, ctx:EDBSParser.Bool_opContext):
        pass

    # Exit a parse tree produced by EDBSParser#bool_op.
    def exitBool_op(self, ctx:EDBSParser.Bool_opContext):
        pass


    # Enter a parse tree produced by EDBSParser#div.
    def enterDiv(self, ctx:EDBSParser.DivContext):
        pass

    # Exit a parse tree produced by EDBSParser#div.
    def exitDiv(self, ctx:EDBSParser.DivContext):
        pass


    # Enter a parse tree produced by EDBSParser#add.
    def enterAdd(self, ctx:EDBSParser.AddContext):
        pass

    # Exit a parse tree produced by EDBSParser#add.
    def exitAdd(self, ctx:EDBSParser.AddContext):
        pass


    # Enter a parse tree produced by EDBSParser#sub.
    def enterSub(self, ctx:EDBSParser.SubContext):
        pass

    # Exit a parse tree produced by EDBSParser#sub.
    def exitSub(self, ctx:EDBSParser.SubContext):
        pass


    # Enter a parse tree produced by EDBSParser#not.
    def enterNot(self, ctx:EDBSParser.NotContext):
        pass

    # Exit a parse tree produced by EDBSParser#not.
    def exitNot(self, ctx:EDBSParser.NotContext):
        pass


    # Enter a parse tree produced by EDBSParser#len.
    def enterLen(self, ctx:EDBSParser.LenContext):
        pass

    # Exit a parse tree produced by EDBSParser#len.
    def exitLen(self, ctx:EDBSParser.LenContext):
        pass


    # Enter a parse tree produced by EDBSParser#null.
    def enterNull(self, ctx:EDBSParser.NullContext):
        pass

    # Exit a parse tree produced by EDBSParser#null.
    def exitNull(self, ctx:EDBSParser.NullContext):
        pass


    # Enter a parse tree produced by EDBSParser#bool.
    def enterBool(self, ctx:EDBSParser.BoolContext):
        pass

    # Exit a parse tree produced by EDBSParser#bool.
    def exitBool(self, ctx:EDBSParser.BoolContext):
        pass


    # Enter a parse tree produced by EDBSParser#mul.
    def enterMul(self, ctx:EDBSParser.MulContext):
        pass

    # Exit a parse tree produced by EDBSParser#mul.
    def exitMul(self, ctx:EDBSParser.MulContext):
        pass


    # Enter a parse tree produced by EDBSParser#lit.
    def enterLit(self, ctx:EDBSParser.LitContext):
        pass

    # Exit a parse tree produced by EDBSParser#lit.
    def exitLit(self, ctx:EDBSParser.LitContext):
        pass


    # Enter a parse tree produced by EDBSParser#var.
    def enterVar(self, ctx:EDBSParser.VarContext):
        pass

    # Exit a parse tree produced by EDBSParser#var.
    def exitVar(self, ctx:EDBSParser.VarContext):
        pass


    # Enter a parse tree produced by EDBSParser#nested.
    def enterNested(self, ctx:EDBSParser.NestedContext):
        pass

    # Exit a parse tree produced by EDBSParser#nested.
    def exitNested(self, ctx:EDBSParser.NestedContext):
        pass


    # Enter a parse tree produced by EDBSParser#str_op.
    def enterStr_op(self, ctx:EDBSParser.Str_opContext):
        pass

    # Exit a parse tree produced by EDBSParser#str_op.
    def exitStr_op(self, ctx:EDBSParser.Str_opContext):
        pass


    # Enter a parse tree produced by EDBSParser#len_op.
    def enterLen_op(self, ctx:EDBSParser.Len_opContext):
        pass

    # Exit a parse tree produced by EDBSParser#len_op.
    def exitLen_op(self, ctx:EDBSParser.Len_opContext):
        pass


    # Enter a parse tree produced by EDBSParser#list_op.
    def enterList_op(self, ctx:EDBSParser.List_opContext):
        pass

    # Exit a parse tree produced by EDBSParser#list_op.
    def exitList_op(self, ctx:EDBSParser.List_opContext):
        pass


    # Enter a parse tree produced by EDBSParser#call_mod_op.
    def enterCall_mod_op(self, ctx:EDBSParser.Call_mod_opContext):
        pass

    # Exit a parse tree produced by EDBSParser#call_mod_op.
    def exitCall_mod_op(self, ctx:EDBSParser.Call_mod_opContext):
        pass


    # Enter a parse tree produced by EDBSParser#def_module_op.
    def enterDef_module_op(self, ctx:EDBSParser.Def_module_opContext):
        pass

    # Exit a parse tree produced by EDBSParser#def_module_op.
    def exitDef_module_op(self, ctx:EDBSParser.Def_module_opContext):
        pass


    # Enter a parse tree produced by EDBSParser#while_stmt.
    def enterWhile_stmt(self, ctx:EDBSParser.While_stmtContext):
        pass

    # Exit a parse tree produced by EDBSParser#while_stmt.
    def exitWhile_stmt(self, ctx:EDBSParser.While_stmtContext):
        pass


    # Enter a parse tree produced by EDBSParser#update_stmt.
    def enterUpdate_stmt(self, ctx:EDBSParser.Update_stmtContext):
        pass

    # Exit a parse tree produced by EDBSParser#update_stmt.
    def exitUpdate_stmt(self, ctx:EDBSParser.Update_stmtContext):
        pass


    # Enter a parse tree produced by EDBSParser#read_assgn.
    def enterRead_assgn(self, ctx:EDBSParser.Read_assgnContext):
        pass

    # Exit a parse tree produced by EDBSParser#read_assgn.
    def exitRead_assgn(self, ctx:EDBSParser.Read_assgnContext):
        pass


    # Enter a parse tree produced by EDBSParser#read_file_stmt.
    def enterRead_file_stmt(self, ctx:EDBSParser.Read_file_stmtContext):
        pass

    # Exit a parse tree produced by EDBSParser#read_file_stmt.
    def exitRead_file_stmt(self, ctx:EDBSParser.Read_file_stmtContext):
        pass



del EDBSParser