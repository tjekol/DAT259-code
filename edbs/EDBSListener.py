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


    # Enter a parse tree produced by EDBSParser#main_stmt.
    def enterMain_stmt(self, ctx:EDBSParser.Main_stmtContext):
        pass

    # Exit a parse tree produced by EDBSParser#main_stmt.
    def exitMain_stmt(self, ctx:EDBSParser.Main_stmtContext):
        pass


    # Enter a parse tree produced by EDBSParser#module_def.
    def enterModule_def(self, ctx:EDBSParser.Module_defContext):
        pass

    # Exit a parse tree produced by EDBSParser#module_def.
    def exitModule_def(self, ctx:EDBSParser.Module_defContext):
        pass


    # Enter a parse tree produced by EDBSParser#input_params.
    def enterInput_params(self, ctx:EDBSParser.Input_paramsContext):
        pass

    # Exit a parse tree produced by EDBSParser#input_params.
    def exitInput_params(self, ctx:EDBSParser.Input_paramsContext):
        pass


    # Enter a parse tree produced by EDBSParser#output_params.
    def enterOutput_params(self, ctx:EDBSParser.Output_paramsContext):
        pass

    # Exit a parse tree produced by EDBSParser#output_params.
    def exitOutput_params(self, ctx:EDBSParser.Output_paramsContext):
        pass


    # Enter a parse tree produced by EDBSParser#param_list.
    def enterParam_list(self, ctx:EDBSParser.Param_listContext):
        pass

    # Exit a parse tree produced by EDBSParser#param_list.
    def exitParam_list(self, ctx:EDBSParser.Param_listContext):
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


    # Enter a parse tree produced by EDBSParser#mul.
    def enterMul(self, ctx:EDBSParser.MulContext):
        pass

    # Exit a parse tree produced by EDBSParser#mul.
    def exitMul(self, ctx:EDBSParser.MulContext):
        pass


    # Enter a parse tree produced by EDBSParser#var.
    def enterVar(self, ctx:EDBSParser.VarContext):
        pass

    # Exit a parse tree produced by EDBSParser#var.
    def exitVar(self, ctx:EDBSParser.VarContext):
        pass


    # Enter a parse tree produced by EDBSParser#concat.
    def enterConcat(self, ctx:EDBSParser.ConcatContext):
        pass

    # Exit a parse tree produced by EDBSParser#concat.
    def exitConcat(self, ctx:EDBSParser.ConcatContext):
        pass


    # Enter a parse tree produced by EDBSParser#nested.
    def enterNested(self, ctx:EDBSParser.NestedContext):
        pass

    # Exit a parse tree produced by EDBSParser#nested.
    def exitNested(self, ctx:EDBSParser.NestedContext):
        pass


    # Enter a parse tree produced by EDBSParser#substr.
    def enterSubstr(self, ctx:EDBSParser.SubstrContext):
        pass

    # Exit a parse tree produced by EDBSParser#substr.
    def exitSubstr(self, ctx:EDBSParser.SubstrContext):
        pass


    # Enter a parse tree produced by EDBSParser#div.
    def enterDiv(self, ctx:EDBSParser.DivContext):
        pass

    # Exit a parse tree produced by EDBSParser#div.
    def exitDiv(self, ctx:EDBSParser.DivContext):
        pass


    # Enter a parse tree produced by EDBSParser#call_op.
    def enterCall_op(self, ctx:EDBSParser.Call_opContext):
        pass

    # Exit a parse tree produced by EDBSParser#call_op.
    def exitCall_op(self, ctx:EDBSParser.Call_opContext):
        pass


    # Enter a parse tree produced by EDBSParser#strlit.
    def enterStrlit(self, ctx:EDBSParser.StrlitContext):
        pass

    # Exit a parse tree produced by EDBSParser#strlit.
    def exitStrlit(self, ctx:EDBSParser.StrlitContext):
        pass


    # Enter a parse tree produced by EDBSParser#split.
    def enterSplit(self, ctx:EDBSParser.SplitContext):
        pass

    # Exit a parse tree produced by EDBSParser#split.
    def exitSplit(self, ctx:EDBSParser.SplitContext):
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


    # Enter a parse tree produced by EDBSParser#lit.
    def enterLit(self, ctx:EDBSParser.LitContext):
        pass

    # Exit a parse tree produced by EDBSParser#lit.
    def exitLit(self, ctx:EDBSParser.LitContext):
        pass


    # Enter a parse tree produced by EDBSParser#repeat.
    def enterRepeat(self, ctx:EDBSParser.RepeatContext):
        pass

    # Exit a parse tree produced by EDBSParser#repeat.
    def exitRepeat(self, ctx:EDBSParser.RepeatContext):
        pass


    # Enter a parse tree produced by EDBSParser#list_op.
    def enterList_op(self, ctx:EDBSParser.List_opContext):
        pass

    # Exit a parse tree produced by EDBSParser#list_op.
    def exitList_op(self, ctx:EDBSParser.List_opContext):
        pass


    # Enter a parse tree produced by EDBSParser#comp.
    def enterComp(self, ctx:EDBSParser.CompContext):
        pass

    # Exit a parse tree produced by EDBSParser#comp.
    def exitComp(self, ctx:EDBSParser.CompContext):
        pass


    # Enter a parse tree produced by EDBSParser#not.
    def enterNot(self, ctx:EDBSParser.NotContext):
        pass

    # Exit a parse tree produced by EDBSParser#not.
    def exitNot(self, ctx:EDBSParser.NotContext):
        pass


    # Enter a parse tree produced by EDBSParser#or.
    def enterOr(self, ctx:EDBSParser.OrContext):
        pass

    # Exit a parse tree produced by EDBSParser#or.
    def exitOr(self, ctx:EDBSParser.OrContext):
        pass


    # Enter a parse tree produced by EDBSParser#and.
    def enterAnd(self, ctx:EDBSParser.AndContext):
        pass

    # Exit a parse tree produced by EDBSParser#and.
    def exitAnd(self, ctx:EDBSParser.AndContext):
        pass


    # Enter a parse tree produced by EDBSParser#cond.
    def enterCond(self, ctx:EDBSParser.CondContext):
        pass

    # Exit a parse tree produced by EDBSParser#cond.
    def exitCond(self, ctx:EDBSParser.CondContext):
        pass


    # Enter a parse tree produced by EDBSParser#comparison.
    def enterComparison(self, ctx:EDBSParser.ComparisonContext):
        pass

    # Exit a parse tree produced by EDBSParser#comparison.
    def exitComparison(self, ctx:EDBSParser.ComparisonContext):
        pass


    # Enter a parse tree produced by EDBSParser#str_lit.
    def enterStr_lit(self, ctx:EDBSParser.Str_litContext):
        pass

    # Exit a parse tree produced by EDBSParser#str_lit.
    def exitStr_lit(self, ctx:EDBSParser.Str_litContext):
        pass


    # Enter a parse tree produced by EDBSParser#list_command.
    def enterList_command(self, ctx:EDBSParser.List_commandContext):
        pass

    # Exit a parse tree produced by EDBSParser#list_command.
    def exitList_command(self, ctx:EDBSParser.List_commandContext):
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