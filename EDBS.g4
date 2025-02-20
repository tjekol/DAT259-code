grammar EDBS;

import EDBSTokens;

program : statement* FINISH_KEYWORD NEWLINE?;

statement : module_def | main_stmt PERIOD NEWLINE* | COMMENT NEWLINE*;

main_stmt : while_stmt | update_stmt | write_stmt | read_assgn  | calc_stmt | read_file_stmt;

module_def : DEF_MOULE_KEYWORD IDENTIFIER MODULE_PARAM_KEYWORD input_params output_params NEWLINE?
    MODULE_BODY_KEYWORD COLON NEWLINE? statement* EXIT_MODULE_KEYWORD NEWLINE?;

input_params : INPUT_PARAM_KEYWORD COLON param_list;
output_params : OUTPUT_PARAM_KEYWORD COLON IDENTIFIER;
param_list : IDENTIFIER (COMMA IDENTIFIER)*;

write_stmt : WRITE_KEYWORD write_arg+;

write_arg : STRING | IDENTIFIER;

calc_stmt : CALC_KEYWORD IDENTIFIER COLON expr_op;

expr_op : expr_op OP_MUL expr_op # mul
    | expr_op OP_DIV expr_op # div
    | expr_op OP_ADD expr_op # add
    | expr_op OP_SUB expr_op # sub
    | expr_op SOP_CONCAT expr_op # concat
    | expr_op SOP_REPEAT expr_op # repeat
    | expr_op SOP_SUBSTR expr_op # substr
    | expr_op SOP_SPLIT expr_op # split
    | OPEN_PAREN expr_op CLOSE_PAREN # nested
    | LENGTH_KEYWORD OF_KEYWORD expr_op # len
    | list_command OF_KEYWORD? IDENTIFIER (LOP_RESET_IDX expr_op)? # list_op
    | CALL_MODULE_KEYWORD IDENTIFIER MODULE_PARAM_KEYWORD expr_op # call_op
    | NUMBER # lit
    | IDENTIFIER # var
    | str_lit # strlit
    | NULL_CHAR # null;

bool_expr : CONDITION_KEYWORD bool_expr # cond
    | BOP_NOT bool_expr # not
    | bool_expr BOP_AND bool_expr # and
    | bool_expr BOP_OR bool_expr # or
    | comparison # comp
    ;

comparison : expr_op (COMP_EQL | COMP_LT | COMP_LEQ | COMP_GT | COMP_GEQ) expr_op;

str_lit : NULL_CHAR | NEWLINE_CHAR | WHITESPACE_CHAR | STRING;

list_command : NEXT_KEYWORD | LOP_FIND | LOP_BACK | LOP_RESET;

while_stmt : REPEAT_KEYWORD (main_stmt COMMA?)* NEWLINE? bool_expr | REPEAT_KEYWORD main_stmt* EXIT_MODULE_KEYWORD* bool_expr;

update_stmt : UPDATE_KEYWORD IDENTIFIER COLON expr_op;

read_assgn : READ_KEYWORD IDENTIFIER COLON STRING;

read_file_stmt : READ_KEYWORD FILE_KEYWORD IDENTIFIER;
