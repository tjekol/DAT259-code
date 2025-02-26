grammar EDBS;

import EDBSTokens;

program : module_def* main_stmt* FINISH_KEYWORD NEWLINE?;

module_def : DEF_MOULE_KEYWORD IDENTIFIER MODULE_PARAM_KEYWORD NEWLINE?
     input_params NEWLINE? output_params
     NEWLINE? MODULE_BODY_KEYWORD COLON NEWLINE?
     module_body
     EXIT_KEYWORD MODULE_KEYWORD PERIOD NEWLINE?;

input_params : INPUT_PARAM_KEYWORD COLON param_list;
output_params : OUTPUT_PARAM_KEYWORD COLON IDENTIFIER;
module_body : main_stmt+;
param_list : IDENTIFIER (COMMA IDENTIFIER)*;

main_stmt : statement PERIOD NEWLINE;

statement : while_stmt | mutate_stmt | write_stmt | read_assgn  | calc_stmt | read_file_stmt | return;

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
    | CALL_MODULE_KEYWORD IDENTIFIER MODULE_PARAM_KEYWORD actual_param_list # call_op
    | list_command OF_KEYWORD? IDENTIFIER (LOP_RESET_IDX expr_op)? # list_op
    | IDENTIFIER PRIMED? # var
    | str_literal # strlit
    | NUMBER # nolit
    ;

bool_expr : CONDITION_KEYWORD bool_expr # cond
    | BOP_NOT bool_expr # not
    | bool_expr BOP_AND bool_expr # and
    | bool_expr BOP_OR bool_expr # or
    | comparison # comp
    ;

actual_param_list : actual_param (COMMA actual_param)*;

actual_param : NUMBER | str_literal | IDENTIFIER;

comparison : expr_op (COMP_EQL | COMP_LT | COMP_LEQ | COMP_GT | COMP_GEQ) expr_op;

str_literal : NULL_CHAR | NEWLINE_CHAR | WHITESPACE_CHAR | STRING;

list_command : LOP_NEXT | LOP_FIND | LOP_BACK | LOP_RESET;

while_stmt : REPEAT_KEYWORD NEWLINE? statement (COMMA NEWLINE? statement)* NEWLINE? CONDITION_KEYWORD bool_expr;

mutate_stmt : UPDATE_KEYWORD IDENTIFIER COLON expr_op;

read_assgn : READ_KEYWORD IDENTIFIER COLON STRING;

read_file_stmt : READ_KEYWORD FILE_KEYWORD IDENTIFIER;

return : EXIT_KEYWORD EXCLAMATION;
