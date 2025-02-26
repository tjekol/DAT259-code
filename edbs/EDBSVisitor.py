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


    # Visit a parse tree produced by EDBSParser#module_def.
    def visitModule_def(self, ctx:EDBSParser.Module_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#input_params.
    def visitInput_params(self, ctx:EDBSParser.Input_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#output_params.
    def visitOutput_params(self, ctx:EDBSParser.Output_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#module_body.
    def visitModule_body(self, ctx:EDBSParser.Module_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#param_list.
    def visitParam_list(self, ctx:EDBSParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#main_stmt.
    def visitMain_stmt(self, ctx:EDBSParser.Main_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#statement.
    def visitStatement(self, ctx:EDBSParser.StatementContext):
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


    # Visit a parse tree produced by EDBSParser#add.
    def visitAdd(self, ctx:EDBSParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#sub.
    def visitSub(self, ctx:EDBSParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#mul.
    def visitMul(self, ctx:EDBSParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#var.
    def visitVar(self, ctx:EDBSParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#concat.
    def visitConcat(self, ctx:EDBSParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#nested.
    def visitNested(self, ctx:EDBSParser.NestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#substr.
    def visitSubstr(self, ctx:EDBSParser.SubstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#div.
    def visitDiv(self, ctx:EDBSParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#call_op.
    def visitCall_op(self, ctx:EDBSParser.Call_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#strlit.
    def visitStrlit(self, ctx:EDBSParser.StrlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#split.
    def visitSplit(self, ctx:EDBSParser.SplitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#len.
    def visitLen(self, ctx:EDBSParser.LenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#nolit.
    def visitNolit(self, ctx:EDBSParser.NolitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#repeat.
    def visitRepeat(self, ctx:EDBSParser.RepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#list_op.
    def visitList_op(self, ctx:EDBSParser.List_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#comp.
    def visitComp(self, ctx:EDBSParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#not.
    def visitNot(self, ctx:EDBSParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#or.
    def visitOr(self, ctx:EDBSParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#and.
    def visitAnd(self, ctx:EDBSParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#cond.
    def visitCond(self, ctx:EDBSParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#actual_param_list.
    def visitActual_param_list(self, ctx:EDBSParser.Actual_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#actual_param.
    def visitActual_param(self, ctx:EDBSParser.Actual_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#comparison.
    def visitComparison(self, ctx:EDBSParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#str_literal.
    def visitStr_literal(self, ctx:EDBSParser.Str_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#list_command.
    def visitList_command(self, ctx:EDBSParser.List_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#while_stmt.
    def visitWhile_stmt(self, ctx:EDBSParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#mutate_stmt.
    def visitMutate_stmt(self, ctx:EDBSParser.Mutate_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#read_assgn.
    def visitRead_assgn(self, ctx:EDBSParser.Read_assgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#read_file_stmt.
    def visitRead_file_stmt(self, ctx:EDBSParser.Read_file_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#return.
    def visitReturn(self, ctx:EDBSParser.ReturnContext):
        return self.visitChildren(ctx)



del EDBSParser