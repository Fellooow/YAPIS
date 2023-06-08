grammar gramma;

EQ : '=' ;
PLUS : '+';
DIFFER : '-';
MULTI : '*';
QUONTIENT : '/';
LESS : '<';
MORRE : '>';
NEQ : '!=';
COMPR : '==';
INCR : '+=';
DECR : '-=';
LBRACKET : '(' ;
RBRACKET: ')' ;
LCURLBR : '{' ;
RCURLBR: '}' ;
LSQBR : '[' ;
RSQBR : ']' ;
COLON : ':' ;
COMMA : ',' ;
DCOMA : ';' ;
DOT : '.';
IF : 'if';
WHILE : 'while';
CASE : 'case';
SWITCH : 'switch';
SUBPROG: 'sub_prog';
RETURN : 'return';
FOR : 'for';
ELSE : 'else';
WRITE: 'write';
READ: 'read';
BREAK : 'break';
TRUE : 'true';
FALSE : 'false';
PROG : 'prog';

NEWLINE:'\n' ;
FLOAT : [0-9]+[.][0-9]+ ;
INT : [0-9]+ ;
STR : ["][a-zA-Z_ 0-9]*["];
CHAR : ["][a-zA-Z_]["];
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS : [ \t\r\f]+ -> skip ;

program
    : def* BEGIN '(' stat* ')' EOF?
    ;

stat: ID (',' ID)* INIT
    expr (',' expr)*
    | expr
    | if
    | def
    | for
    | while
    | switch
    ;
for: FOR  expr IN expr COLON (stat)+;

 if:IF  ifExpr  COLON
    (stat)+
    ELSE COLON (stat)+
    | IF '('expr')'
         (stat)+
    ;
def :TYPE ID '(' expr (',' expr)* ')' COLON (stat)+ RETURN expr
    ;
while:WHILE '(' ifExpr ')' COLON (stat)+;

switch: SWITCH '('expr')' COLON (CASE expr COLON (stat)+)+;


varibleDeclaration:  TYPE ID(','ID)*
    |TYPE varibleInitialisation
;

varibleInitialisation: ID INIT ID
    ;

list: '{' expr? (',' expr)* '}';
index: '{'expr?'}'|'{'expr?'}';
ifExpr: expr (EQ|NOTEQ|M|NM) expr;
op: (PLUS|MINUS|MULT);
expr: ID
    | STRING
    | INT
    | varibleDeclaration
    | varibleInitialisation
    | func
    | list
    | expr index
    | expr INIT expr
    | expr (INCREMENT|DECREMENT)
    | expr'.'expr
    | expr op expr
    ;

func :TYPE ID '(' expr? (',' expr)* ')'
| ID '(' expr? (',' expr)* ')';