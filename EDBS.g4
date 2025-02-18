grammar EDBS;

import EDBSTokens;

program : statement* FINISH_KEYWORD NEWLINE?;

statement : def_module_op | fin_stmt PERIOD NEWLINE* | COMMENT NEWLINE*;

fin_stmt : while_stmt | update_stmt | write_stmt | read_assgn  | calc_stmt | read_file_stmt;

write_stmt : WRITE_KEYWORD write_arg+;

write_arg : STRING | IDENTIFIER;

calc_stmt : CALC_KEYWORD IDENTIFIER COLON (expr_op | call_mod_op | list_op | str_op);

cond_stmt : CONDITION_KEYWORD expr_op cond_stmt expr_op | COMP_EQL | COMP_LT | COMP_LEQ | COMP_GT | COMP_GEQ;

bool_op : BOP_AND | BOP_OR;

expr_op : BOP_NOT expr_op # not
    | expr_op bool_op expr_op # bool
    | expr_op OP_MUL expr_op # mul
    | expr_op OP_DIV expr_op # div
    | expr_op OP_ADD expr_op # add
    | expr_op OP_SUB expr_op # sub
    | len_op # len
    | OPEN_PAREN expr_op CLOSE_PAREN # nested
    | NUMBER # lit | IDENTIFIER # var | NULL_CHAR # null;

str_op : str_op SOP_CONCAT str_op | str_op SOP_REPEAT str_op | str_op SOP_SUBSTR str_op | str_op SOP_SPLIT str_op | NULL_CHAR | NEWLINE_CHAR | WHITESPACE_CHAR | IDENTIFIER;

len_op : LENGTH_KEYWORD OF_KEYWORD str_op;

list_op : NEXT_KEYWORD OF_KEYWORD? IDENTIFIER;

call_mod_op : CALL_MODULE_KEYWORD IDENTIFIER MODULE_PARAM_KEYWORD IDENTIFIER;

def_module_op : DEF_MOULE_KEYWORD IDENTIFIER MODULE_PARAM_KEYWORD INPUT_PARAM_KEYWORD COLON expr_op OUTPUT_PARAM_KEYWORD COLON IDENTIFIER NEWLINE MODULE_BODY_KEYWORD COLON statement* EXIT_MODULE_KEYWORD;

while_stmt : REPEAT_KEYWORD (fin_stmt COMMA?)* NEWLINE? cond_stmt | REPEAT_KEYWORD fin_stmt* EXIT_MODULE_KEYWORD* cond_stmt;

update_stmt : UPDATE_KEYWORD IDENTIFIER COLON (expr_op | list_op | str_op);

read_assgn : READ_KEYWORD IDENTIFIER COLON STRING;

read_file_stmt : READ_KEYWORD FILE_KEYWORD IDENTIFIER;
