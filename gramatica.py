reservadas = {
    'Int64': 'INT',
    'Float64': 'FLOAT',
    'String': 'STR',
    'print': 'PRINT',
    'println': 'PRINTLN',
    'typeof': 'TYPEOF',
    'parse': 'PARSE',
    'uppercase': 'UPPERCASE',
    'lowercase': 'LOWERCASE',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
}

tokens = [
    'SEMICOL',
    'LBRACE',
    'RBRACE',
    'LPAR',
    'RPAR',
    'EQUAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'POT',
    'LESS',
    'LESSEQ',
    'GREATHER',
    'GREATHEREQ',
    'EQUALITY',
    'DIFERENT',
    'DECIMAL',
    'NUMBER',
    'STRING',
    'ID'
] + list(reservadas.values())

t_SEMICOL = r';'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LPAR = r'\('
t_RPAR = r'\)'
t_EQUAL = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_POT = r'\^'
t_LESS = r'<'
t_LESSEQ = r'<='
t_GREATHER = r'>'
t_GREATHEREQ = r'>='
t_EQUALITY = r'=='
t_DIFERENT = r'!='

def t_DECIMAL(t) :
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print(f'Error léxico: {t.value} es muy grande')
        t.value = 0
    return t

def t_NUMBER(t) :
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f'Error léxico: {t.value} es muy grande')
        t.value = 0
    return t

def t_STRING(t) :
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_ID(t) :
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t

def t_COMMENT_MUL(t) :
    r'\#.*\n'
    t.lexer.lineno += t.value.count('\n')

def t_COMMENT_SIM(t) :
    r'\#=.*=\#'
    t.lexer.lineno += 1

t_ignore = " \t"

def t_newline(t) :
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t) :
    print(f'Error léxico: Caracter {t.value[0]} no reconocido')
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV'),
    ('left', 'POT'),
    ('right', 'UMINUS'),
)

from instrucciones import *
from expresiones import *

def p_init(t) :
    'init : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones(t) :
    'instrucciones : instruccion'
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion  : print
                    | println
                    | definicion
                    | asignacion
                    | while
                    | if
                    | if_else'''
    t[0] = t[1]

def p_print(t) :
    'print : PRINT LPAR expresion_cadena RPAR'
    t[0] = Print(t[3])

def p_println(t) :
    'println : PRINTLN LPAR expresion_cadena RPAR'
    t[0] = Println(t[3])

def p_definicion(t) :
    'definicion : ID'
    t[0] = Definicion(t[1])

def p_asignacion(t) :
    'asignacion : ID EQUAL expresion_numerica'
    t[0] = Definicion(t[1], t[3])

def p_while(t) :
    'while : WHILE LPAR expresion_logica RPAR LBRACE instrucciones RBRACE'
    t[0] = Mientras(t[3], t[6])

def p_if(t) :
    'if : IF LPAR expresion_logica RPAR LBRACE instrucciones RBRACE'
    t[0] = If(t[3], t[6])

def p_if_else(t) :
    'if_else : IF LPAR expresion_logica RPAR LBRACE instrucciones RBRACE ELSE LBRACE instrucciones RBRACE'
    t[0] = IfElse(t[3], t[6], t[10])

def p_expresion_binaria(t) :
    '''expresion_numerica   : expresion_numerica PLUS expresion_numerica
                            | expresion_numerica MINUS expresion_numerica
                            | expresion_numerica TIMES expresion_numerica
                            | expresion_numerica DIV expresion_numerica
                            | expresion_numerica POT expresion_numerica'''
    if t[2] == '+'      : t[0] = ExpresionBinaria(t[1], t[3], OP_ARITHMETIC.MAS)
    elif t[2] == '-'    : t[0] = ExpresionBinaria(t[1], t[3], OP_ARITHMETIC.MENOS)
    elif t[2] == '*'    : t[0] = ExpresionBinaria(t[1], t[3], OP_ARITHMETIC.POR)
    elif t[2] == '/'    : t[0] = ExpresionBinaria(t[1], t[3], OP_ARITHMETIC.DIVIDIDO)
    elif t[2] == '^'    : t[0] = ExpresionBinaria(t[1], t[3], OP_ARITHMETIC.POTENCIA)

def p_expresion_unaria(t) :
    'expresion_numerica : MINUS expresion_numerica %prec UMINUS'
    t[0] = ExpresionNegativo(t[2])

def p_expresion_agrupacion(t) :
    'expresion_numerica : LPAR expresion_numerica RPAR'
    t[0] = t[2]

def p_number(t) :
    '''expresion_numerica : NUMBER
                        | DECIMAL'''
    t[0] = ExpresionNumero(t[1])    

def p_id(t) :
    'expresion_numerica : ID'
    t[0] = ExpresionIdentificador(t[1])

def p_cadena(t) :
    'expresion_cadena : STRING'
    t[0] = ExpresionCadenaSimple(t[1])

def p_cadena_numerica(t) :
    'expresion_cadena : expresion_numerica'
    t[0] = ExpresionCadenaNumero(t[1])

def p_expresion_logica(t) :
    '''expresion_logica : expresion_numerica LESS expresion_numerica
                        | expresion_numerica LESSEQ expresion_numerica
                        | expresion_numerica GREATHER expresion_numerica
                        | expresion_numerica GREATHEREQ expresion_numerica
                        | expresion_numerica EQUALITY expresion_numerica
                        | expresion_numerica DIFERENT expresion_numerica'''
    if t[2] == '<'      : t[0] = ExpresionLogica(t[1], t[3], OP_LOGIC.MENOR)
    elif t[2] == '<='   : t[0] = ExpresionLogica(t[1], t[3], OP_LOGIC.MENOR_IGUAL)
    elif t[2] == '>'    : t[0] = ExpresionLogica(t[1], t[3], OP_LOGIC.MAYOR)
    elif t[2] == '>='   : t[0] = ExpresionLogica(t[1], t[3], OP_LOGIC.MAYOR_IGUAL)
    elif t[2] == '='    : t[0] = ExpresionLogica(t[1], t[3], OP_LOGIC.IGUAL)
    elif t[2] == '!='   : t[0] = ExpresionLogica(t[1], t[3], OP_LOGIC.DIFERENTE)

def p_error(t) :
    print(t)
    print(f'Error sintáctico: {t.value} no esperado')

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)