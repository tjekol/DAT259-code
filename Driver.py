import sys
from antlr4 import *
from edbs.EDBSLexer import EDBSLexer
from edbs.EDBSParser import EDBSParser
from edbs.EDBSVisitor import EDBSVisitor

class InterpreterVisitor(EDBSVisitor):

    def visitWrite_arg(self, ctx: EDBSParser.Write_argContext):
        if ctx.IDENTIFIER() is not None:
            name = str(ctx.STRING())
            value = name
            print(str(value), end=' ')
        elif ctx.STRING():
            string_token = ctx.STRING()
            print(str(string_token)[1:-1], end=' ')
    
    def visitWrite_stmt(self, ctx: EDBSParser.Write_stmtContext):
        for c in ctx.children:
            self.visit(c)
        print()

def main():
    input_stream = FileStream("./Example code/hello.edbs", encoding="utf-8")
    lexer = EDBSLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = EDBSParser(token_stream)
    tree = parser.program()
    visitor = InterpreterVisitor()
    
    visitor.visit(tree)

if __name__ == '__main__':
    main()