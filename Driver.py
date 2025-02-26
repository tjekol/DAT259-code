import sys

from antlr4 import *
from edbs.EDBSLexer import EDBSLexer
from edbs.EDBSParser import EDBSParser
from edbs.EDBSVisitor import EDBSVisitor

class ExitCall(Exception):
    pass

class UndefinedVarRef(Exception):
    def __init__(self, name: str):
        self.name = name

class VarAlreadyDefined(Exception):
    def __init__(self, name: str):
        self.name = name

class Module:
    def __init__(self, formal_params, result, body):
        self.formal_params = formal_params
        self.result = result
        self.body = body

class SymbolTable:
    def __init__(self, next = None):
        self.storage = {}
        self.modules = {}
        self.next = next

    def add_var(self, name: str, value: float):
        # if name in self.storage:
        #     raise VarAlreadyDefined(name)
        self.storage[name] = value

    def get_var(self, name: str):
        if name not in self.storage:
            if self.next is not None:
                return self.next.get_var(name)
            else:
                UndefinedVarRef(name)
        return self.storage[name]

    def mutate_var(self, name: str, value):
        if self.next is not None:
            self.next.mutate_var(name, value)
        else:
            self.storage[name] = value

    def is_defined(self, name: str):
        result = name in self.storage
        if not result and self.next is not None:
            return self.next.is_defined(name)
        return result

class CollectActualParams(EDBSVisitor):
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        self.values = []

    def visitActual_param_list(self, ctx:EDBSParser.Actual_param_listContext):
        for p in ctx.getChildren():
            self.visit(p)

    def visitActual_param(self, ctx:EDBSParser.Actual_paramContext):
        if ctx.IDENTIFIER() is not None:
            self.values.append(self.symbol_table.get_var(str(ctx.IDENTIFIER())))
        elif ctx.NUMBER():
            self.values.append(float(str(ctx.NUMBER()).replace(".","").replace(",",".")))
        else:
            self.values.append(self.visit(ctx.str_literal()))

    def visitStr_literal(self, ctx:EDBSParser.Str_literalContext):
        if ctx.STRING() is not None:
            return str(ctx.STRING())[1:-1]
        elif ctx.NEWLINE_CHAR():
            return '\n'
        elif ctx.WHITESPACE_CHAR():
            return ' '
        elif ctx.NULL_CHAR():
            return None

class InterpreterVisitor(EDBSVisitor):

    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table

    # SKRIV «Hels på deg verda!».
    def visitWrite(self, ctx: EDBSParser.WriteContext):
        for c in ctx.children:
            self.visit(c)
        print()

    def visitWrite_arg(self, ctx: EDBSParser.Write_argContext):
        if ctx.IDENTIFIER() is not None:
            name = str(ctx.IDENTIFIER())
            value = self.symbol_table.get_var(name)
            if isinstance(value, float):
                value = str(round(value, 2)).replace(".", ",")
            if value.endswith(",0"):
                value = value[:-2]
            print(str(value), end=" ")
        elif ctx.STRING():
            string_token = ctx.STRING()
            print(str(string_token)[1:-1], end=" ")

    # LES beløp: «Tast inn lånebeløp».
    def visitRead(self, ctx:EDBSParser.ReadContext):
        prompt = str(ctx.STRING())[1:-1]
        value = float(input(f"{prompt}: ").replace(".", "").replace(",", "."))
        name = str(ctx.IDENTIFIER())
        self.symbol_table.add_var(name, value)

    # REKN totalt-betalt: nedbetaling * 12 * år.
    def visitCalc(self, ctx:EDBSParser.CalcContext):
        name = str(ctx.IDENTIFIER())
        value = self.visit(ctx.expr_op())
        self.symbol_table.add_var(name,value)

    # OPPDATER totalt-avdrag: totalt-avdrag' + avdrag,
    # OPPDATER beløp: ny-beløp,
    def visitMutate(self, ctx:EDBSParser.MutateContext):
        name = str(ctx.IDENTIFIER())
        if not self.symbol_table.is_defined(name):
            self.symbol_table.add_var(name, 0.0)
        value = self.visit(ctx.expr_op())
        self.symbol_table.mutate_var(name, value)

    def visitWhile(self, ctx:EDBSParser.WhileContext):
        is_true = self.visit(ctx.bool_expr())
        self.symbol_table = SymbolTable(self.symbol_table)
        while is_true:
            for c in ctx.children:
                self.visit(c)
            is_true = self.visit(ctx.bool_expr())
        self.symbol_table = self.symbol_table.next

    # module
    def visitModule_def(self, ctx:EDBSParser.Module_defContext):
        name = str(ctx.IDENTIFIER())
        params = self.visit(ctx.input_params())
        result = self.visit(ctx.output_params())
        ctx.output_params()
        m = Module(params, result, ctx.module_body())
        self.symbol_table.modules[name] = m

    def visitOutput_params(self, ctx:EDBSParser.Output_paramsContext):
        return str(ctx.IDENTIFIER())

    def visitInput_params(self, ctx:EDBSParser.Input_paramsContext):
        return self.visit(ctx.param_list())

    def visitParam_list(self, ctx:EDBSParser.Param_listContext):
        idx = 0
        current = ctx.IDENTIFIER(idx)
        result = []
        while current is not None:
            result.append(str(current))
            idx += 1
            current = ctx.IDENTIFIER(idx)
        return result

    # variables & literals
    def visitStrlit(self, ctx:EDBSParser.StrlitContext):
        return self.visit(ctx.str_literal())

    def visitStr_literal(self, ctx:EDBSParser.Str_literalContext):
        if ctx.STRING() is not None:
            return str(ctx.STRING())[1:-1]
        elif ctx.NEWLINE_CHAR():
            return '\n'
        elif ctx.WHITESPACE_CHAR():
            return ' '
        elif ctx.NULL_CHAR():
            return None

    def visitNolit(self, ctx:EDBSParser.NolitContext):
        value = float(str(ctx.NUMBER()).replace(",",'.'))
        return value

    def visitVar(self, ctx:EDBSParser.VarContext):
        name = str(ctx.IDENTIFIER())
        value = self.symbol_table.get_var(name)
        return value

    def visitCall_op(self, ctx:EDBSParser.Call_opContext):
        name = str(ctx.IDENTIFIER())
        actual_params = CollectActualParams(self.symbol_table)
        actual_params.visit(ctx.actual_param_list())
        module = self.symbol_table.modules[name]
        global_scope = self.symbol_table
        self.symbol_table = SymbolTable()
        for p, v in zip(module.formal_params, actual_params.values):
            self.symbol_table.add_var(p,v)
        try:
            self.visit(module.body)
        except ExitCall:
            pass # TODO: Error handling
        result = self.symbol_table.get_var(module.result)
        self.symbol_table = global_scope
        return result


    # expr operations
    def visitMul(self, ctx:EDBSParser.MulContext):
        return self.visit(ctx.getChild(0)) * self.visit(ctx.getChild(2))

    def visitDiv(self, ctx:EDBSParser.DivContext):
        return self.visit(ctx.getChild(0)) / self.visit(ctx.getChild(2))

    def visitAdd(self, ctx:EDBSParser.AddContext):
        return self.visit(ctx.getChild(0)) + self.visit(ctx.getChild(2))

    def visitSub(self, ctx:EDBSParser.SubContext):
        return self.visit(ctx.getChild(0)) - self.visit(ctx.getChild(2))

    def visitNested(self, ctx:EDBSParser.NestedContext):
        return self.visit(ctx.expr_op())

    def visitList_op(self, ctx:EDBSParser.List_opContext):
        return None # TODO: error handling

    # comp
    def visitNot(self, ctx:EDBSParser.NotContext):
        return not self.visit(ctx.bool_expr())

    def visitAnd(self, ctx:EDBSParser.AndContext):
        return self.visit(ctx.getChild(0)) and self.visit(ctx.getChild(2))

    def visitOr(self, ctx:EDBSParser.OrContext):
        return self.visit(ctx.getChild(0)) or self.visit(ctx.getChild(2))

    def visitComp(self, ctx:EDBSParser.CompContext):
        return self.visit(ctx.comparison())

    def visitComparison(self, ctx:EDBSParser.ComparisonContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(ctx.getChildCount() - 1))
        if ctx.COMP_EQL() is not None:
            return lhs == rhs
        elif ctx.COMP_LT() is not None:
            return lhs < rhs
        elif ctx.COMP_LEQ() is not None:
            return lhs <= rhs
        elif ctx.COMP_GT() is not None:
            return lhs > rhs
        elif ctx.COMP_GEQ() is not None:
            return lhs >= rhs


def main():
    # input_stream = FileStream("./Example code/hello.edbs", encoding="utf-8")
    # input_stream = FileStream("./Example code/calc.edbs", encoding="utf-8")
    # input_stream = FileStream("./Example code/laan.edbs", encoding="utf-8")
    input_stream = FileStream("./Example code/modules.edbs", encoding="utf-8")
    # input_stream = FileStream("./Example code/wordcount.edbs", encoding="utf-8")
    lexer = EDBSLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = EDBSParser(token_stream)
    tree = parser.program()
    symbol_table = SymbolTable()
    visitor = InterpreterVisitor(symbol_table)
    
    visitor.visit(tree)

if __name__ == '__main__':
    main()