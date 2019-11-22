/*
 * header
 * name :   Bui Quoc Khai
 * id   :   1711726
 */

grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        result.text = result.text[1:]
        for i in range(len(result.text)):
            if result.text[i] == '\n' or result.text[i] == '\r':
                result.text = result.text[0:i]
                break
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        result.text = result.text[1:]
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    elif tk == self.STRINGLIT:
        result = super().emit();
        result.text = result.text[1:-1]
        return result
    else:
        return super().emit();
}

options{
	language=Python3;
}

/*
 * Parser for MC language
 */

program     :   manyDecl EOF
            ;

manyDecl    :   decl | decl manyDecl
            ;

decl        :   varDecl | funcDecl
            ;

//Variable declaration

varDecl     :   typeList idList  SEMI
            ;

typeList    :   INTTYPE
            |   FLOATTYPE
            |   BOOLEANTYPE
            |   STRINGTYPE
            ;

idList      :   ID COMMA idList 
            |   ID LS INTLIT RS COMMA idList
            |   ID
            |   ID LS INTLIT RS
            ;


//Function declareation

funcDecl    :   (typeList | VOIDTYPE) ID LB paramList RB blockStmt
            |   typeList LS RS ID LB paramList RB blockStmt
            ;

paramList   :   (param paramTemp)?
            ;

paramTemp   :   (COMMA param paramTemp)? 
            ;

param       :   typeList ID (LS RS)?
            ;

//Body

blockStmt   :   LP singStmt* RP
            ;


singStmt    :   varDecl
            |   doWhileStmt SEMI
            |   ifStmt
            |   forStmt
            |   breakStmt SEMI
            |   contiStmt SEMI
            |   returnStmt SEMI
            |   expression SEMI
            |   blockStmt
            ; 

//assignStmt  :   expression (EQUAL expression)+
//            ;

doWhileStmt :   'do' singStmt+ 'while' expression
            ;

ifStmt      :   'if' LB expression RB singStmt (ELSE singStmt)?            
            ;

forStmt     :   'for' LB expression SEMI expression SEMI expression RB singStmt
            ;

breakStmt   :   'break'
            ;

contiStmt   :   'continue'
            ;

returnStmt  :   'return' expression?
            ;

expression  :   expression_1 ASSG expression 
            |   expression_1
            ;

expression_1:   expression_1 OR expression_2
            |   expression_2
            ;

expression_2:   expression_2 AND expression_3
            |   expression_3
            ;

expression_3:   expression_3 (EQUAL|NOTEQUAL) expression_3
            |   expression_4
            ;

expression_4:   expression_4 (LRELA|MRELA|LERELA|MERELA) expression_4
            |   expression_5
            ;

expression_5:   expression_5 (ADD|SUB) expression_6
            |   expression_6
            ;

expression_6:   expression_6 (MUL|DIV|MOD) expression_7
            |   expression_7
            ;

expression_7:   (NOT | SUB) expression_7
            |   expression_8
            ;

expression_8:   expression_9  LS expression_5 RS
            |   expression_9
            ;

expression_9:   LB expression_1 RB
            |   expression_0
            ;

expression_0:   primary 
            |   ID LB (expression (COMMA expression)*)? RB 
            ;

primary     :   INTLIT
            |   FLOATLIT
            |   STRINGLIT
            |   BOOLEANLIT
            |   ID
            ;

/*
 * Lexer tokens initialization
 */

/*
 * Fragment tokens declaration
 */

fragment    EXPONENT    :   [eE][+-]?[0-9]+
                        ;

fragment    ESC_SEQ     :   '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\')
                        ;

fragment    STR_CHAR    :   ~('\\'|'"')
                        ;

fragment    NOT_ESC_SEQ     :   '\\'~('b'|'f'| '\'' | '"' | '\\') |'\\''r''\\'~('n')
                            ;

COMMENT     :   '/*'.*?'*/' -> skip
            ;

COMMENT_LINE:   '//'~[\r\n]* -> skip
            ;

NOT         :   '!'
            ;

MUL         :   '*'
            ;

DIV         :   '/'
            ;

MOD         :   '%'
            ;

ADD         :   '+'
            ;

SUB         :   '-'
            ;

LRELA       :   '<'
            ;

MRELA       :   '>'
            ;

MERELA      :   '>='
            ;

LERELA      :   '<='
            ;

EQUAL       :   '=='
            ;

NOTEQUAL    :   '!='
            ;

AND         :   '&&'
            ;

OR          :   '||'
            ;

ASSG        :   '='
            ;

INTTYPE     :   'int'
            ;

FLOATTYPE   :   'float'
            ;

BOOLEANTYPE :   'boolean'
            ;

STRINGTYPE  :   'string'
            ;

VOIDTYPE    :   'void'
            ;

ELSE        :   'else'
            ;


INTLIT      :   [0-9]+
            ;

FLOATLIT    :   [0-9]+'.'[0-9]* EXPONENT?
            |   '.'[0-9]+ EXPONENT?
            |   [0-9]+ EXPONENT?
            ;

BOOLEANLIT  :   'true'
            |   'false'
            ;
            
ID          :   [a-zA-Z_][0-9a-zA-Z_]*
            ;

LB          :   '('
            ;

RB          :   ')'
            ;

LP          :   '{'
            ;

RP          :   '}'
            ;

LS          :   '['
            ;

RS          :   ']'
            ;

SEMI        :   ';'
            ;

COMMA       :   ','
            ;

WS          :   [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING      :   '"' (ESC_SEQ | STR_CHAR)* ~('"')
                    |   '"' ((ESC_SEQ | STR_CHAR)*('\n'|'\r')(ESC_SEQ | STR_CHAR)*) '"'
                    |   '"' <EOF>
                    ;

ILLEGAL_ESCAPE      :   '"' ( STR_CHAR | ESC_SEQ )* NOT_ESC_SEQ 
                    ;

STRINGLIT   :   '"' ( ESC_SEQ | STR_CHAR )* '"'
            ;


ERROR_CHAR  :   .
            ;
