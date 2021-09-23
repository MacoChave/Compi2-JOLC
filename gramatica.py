reservadas = {
    'Int64': 'INT64',
    'Float64': 'FLOAT64',
    'String': 'STR',
    'Char': 'CHR',
    'Bool': 'BOOL',
    'true': 'TRUE',
    'false': 'FALSE',
    'Nothing': 'NOTHING',
    'print': 'PRINT',
    'println': 'PRINTLN',
    'typeof': 'TYPEOF',
    'parse': 'PARSE',
    'float': 'FLOAT',
    'string': 'STRING',
    'trunc': 'TRUNC',
    'sin': 'SIN',
    'cos': 'COS',
    'tan': 'TAN',
    'log10': 'LOG10',
    'sqrt': 'SQRT',
    'length': 'LENGTH',
    'uppercase': 'UPPERCASE',
    'lowercase': 'LOWERCASE',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    'end': 'END',
    'local': 'LOCAL',
    'global': 'GLOBAL',
    'function': 'FUNCTION'
}

tokens = [
    'SEMICOL', 'AS', 'COLON', 'COMMA',
    # 'QUESTION',
    # 'LBRACE', 'RBRACE',
    'LPAR', 'RPAR',
    'EQUAL',
    # 'ADDITION', 'DIFFERENCE', 'PRODUCT', 'QUOTIENT',
    'AND', 'OR', 'NOT',
    'PLUS', 'MINUS', 'TIMES', 'DIV', 'MOD', 'POT',
    'LESS', 'LESSEQ', 'GREATHER', 'GREATHEREQ',
    'EQUALITY', 'DIFERENT',
    'DECIMAL', 'NUMERO', 'CARACTER', 'CADENA', 'ID'
] + list(reservadas.values())

t_SEMICOL = r';'
t_AS = r'::'
t_COLON = r':'
t_COMMA = r','
# t_QUESTION = r'\?'
# t_LBRACE = r'{'
# t_RBRACE = r'}'
t_LPAR = r'\('
t_RPAR = r'\)'
t_EQUAL = r'='
# t_ADDITION = r'\+='
# t_DIFFERENCE = r'-='
# t_PRODUCT = r'\*='
# t_QUOTIENT = r'/='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_MOD = r'%'
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

def t_NUMERO(t) :
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f'Error léxico: {t.value} es muy grande')
        t.value = 0
    return t

def t_CARACTER(t) :
    r'\'([^\\\n]|(\\.))\''
    char = t.value[1:-1]
    if len(char) == 1 : t.value = char[0]
    elif char[1] == 'n' : t.value = '\n'
    elif char[1] == 't' : t.value = '\t'
    elif char[1] == 'r' : t.value = '\r'

    return t

def t_CADENA(t) :
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_ID(t) :
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_COMMENT_MUL(t) :
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count('\n')

def t_COMMENT_SIM(t) :
    r'\#.*\n'
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
    ('right', 'EQUAL'),
    # ('right', 'ADDITION', 'DIFFERENCE'),
    # ('right', 'PRODUCT', 'QUOTIENT'),
    ('left', 'AND'),
    ('left', 'OR'),
    # ('left', 'QUESTION', 'COLON'),
    ('nonassoc', 'EQUALITY', 'DIFERENT'),
    ('nonassoc', 'LESS', 'GREATHER', 'LESSEQ', 'GREATHEREQ'),
    ('left', 'COLON'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV', 'MOD'),
    ('left', 'POT'),
    ('right', 'NOT'),
    ('right', 'UMINUS'),
)

from instrucciones import *
from expresiones import *
from funciones import *

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
    '''instruccion  : print semicolon
                    | println semicolon
                    | definicion semicolon
                    | while semicolon
                    | for semicolon
                    | function semicolon
                    | if semicolon
                    | if_else semicolon'''
    t[0] = t[1]

def p_print(t) :
    'print : PRINT LPAR print_args RPAR'
    t[0] = Print(t[3])

def p_println(t) :
    'println : PRINTLN LPAR print_args RPAR'
    t[0] = Println(t[3])

def p_print_args(t) :
    'print_args : print_args COMMA exp_logica'
    t[1].append(t[3])
    t[0] = t[1]

def p_print_arg(t) :
    'print_args : exp_logica'
    t[0] = [t[1]]

def p_definicion(t) :
    'definicion : ambito ID asignacion'
    t[0] = Definicion(t[1], t[2], t[3])

def p_ambito_local(t) :
    'ambito : LOCAL'
    t[0] = ALCANCE_VAR.LOCAL

def p_ambito_global(t) :
    'ambito : GLOBAL'
    t[0] = ALCANCE_VAR.GLOBAL

def p_ambito_empty(t) :
    'ambito : empty'
    t[0] = ALCANCE_VAR.EMPTY

def p_asignacion(t) :
    'asignacion : EQUAL exp_logica assign_type'
    t[0] = t[2]

def p_asignacion_empty(t) :
    'asignacion : empty'
    t[0] = None

def p_asignacion_type(t) :
    'assign_type : AS data_type'
    t[0] = t[2]

def p_asignacion_type_empty(t) :
    'assign_type : empty'
    t[0] = None

def p_data_type(t) :
    '''data_type    : INT64
                    | FLOAT64
                    | STR
                    | CHR
                    | BOOL
                    | NOTHING'''
    if t[1] == 'Int64' : t[0] = DATA_TYPE.NUMERO
    elif t[1] == 'Float64' : t[0] = DATA_TYPE.DECIMAL
    elif t[1] == 'String' : t[0] = DATA_TYPE.CADENA
    elif t[1] == 'Char' : t[0] = DATA_TYPE.CARACTER
    elif t[1] == 'Bool' : t[0] = DATA_TYPE.BOLEANO

def p_while(t) :
    'while : WHILE exp_logica instrucciones END'
    t[0] = Mientras(t[2], t[3])

def p_if(t) :
    'if : IF exp_logica instrucciones END'
    t[0] = If(t[2], t[3])

def p_if_else(t) :
    'if_else : IF exp_logica instrucciones ELSE instrucciones END'
    t[0] = IfElse(t[2], t[3], t[5])

def p_for(t) :
    'for : FOR ID IN for_list instrucciones END'
    t[0] = For(t[2], t[4], t[5])

def p_for_from_cadena(t) :
    'for_list : CADENA'
    t[0] = t[1]

def p_function(t) :
    'function : FUNCTION ID LPAR param RPAR instrucciones END'
    t[0] = Funcion(t[2], t[6], t[4])

def p_function_param_list(t) :
    'param : params'
    t[0] = t[1]

def p_function_param_empty(t) :
    'param : empty'
    t[0] = []

def p_function_params(t) :
    'params : params COMMA ID'
    t[1].append(t[3])
    t[0] = t[1]

def p_function_param(t) :
    'params : ID'
    t[0] = [t[1]]

def p_semicolon(t) :
    '''semicolon    : SEMICOL
                    | empty'''
    pass

def p_logica_binaria(t) :
    '''exp_logica    : exp_logica AND exp_logica
                    | exp_logica OR exp_logica'''
    if t[2] == '&&'      : t[0] = LogicaBinaria(t[1], t[3], OP_LOGICA.AND)
    elif t[2] == '||'    : t[0] = LogicaBinaria(t[1], t[3], OP_LOGICA.OR)

def p_logica_not(t) :
    'exp_logica : NOT exp_logica'
    t[0] = Negado(t[2], OP_LOGICA.NOT)

def p_logica_to_relacional(t) :
    'exp_logica : exp_relacional'
    t[0] = t[1]

def p_relacional_binaria(t) :
    '''exp_relacional   : exp_relacional LESS exp_relacional
                        | exp_relacional LESSEQ exp_relacional
                        | exp_relacional GREATHER exp_relacional
                        | exp_relacional GREATHEREQ exp_relacional
                        | exp_relacional EQUALITY exp_relacional
                        | exp_relacional DIFERENT exp_relacional'''
    if t[2] == '<'      : t[0] = ExpresionRelacional(t[1], t[3], OP_RELACIONAL.MENOR)
    elif t[2] == '<='   : t[0] = ExpresionRelacional(t[1], t[3], OP_RELACIONAL.MENOR_IGUAL)
    elif t[2] == '>'    : t[0] = ExpresionRelacional(t[1], t[3], OP_RELACIONAL.MAYOR)
    elif t[2] == '>='   : t[0] = ExpresionRelacional(t[1], t[3], OP_RELACIONAL.MAYOR_IGUAL)
    elif t[2] == '=='   : t[0] = ExpresionRelacional(t[1], t[3], OP_RELACIONAL.IGUAL)
    elif t[2] == '!='   : t[0] = ExpresionRelacional(t[1], t[3], OP_RELACIONAL.DIFERENTE)

def p_relacinal_to_aritmetica(t) :
    'exp_relacional : exp_aritmetica'
    t[0] = t[1]

def p_aritmetica_binaria(t) :
    '''exp_aritmetica   : exp_aritmetica PLUS exp_aritmetica
                        | exp_aritmetica MINUS exp_aritmetica
                        | exp_aritmetica TIMES exp_aritmetica
                        | exp_aritmetica DIV exp_aritmetica
                        | exp_aritmetica MOD exp_aritmetica
                        | exp_aritmetica POT exp_aritmetica
                        | exp_aritmetica COLON exp_aritmetica'''
    if t[2] == '+'      : t[0] = AritmeticaBinaria(t[1], t[3], OP_ARITMETICA.MAS)
    elif t[2] == '-'    : t[0] = AritmeticaBinaria(t[1], t[3], OP_ARITMETICA.MENOS)
    elif t[2] == '*'    : t[0] = AritmeticaBinaria(t[1], t[3], OP_ARITMETICA.POR)
    elif t[2] == '/'    : t[0] = AritmeticaBinaria(t[1], t[3], OP_ARITMETICA.DIVIDIDO)
    elif t[2] == '%'    : t[0] = AritmeticaBinaria(t[1], t[3], OP_ARITMETICA.MODULO)
    elif t[2] == '^'    : t[0] = AritmeticaBinaria(t[1], t[3], OP_ARITMETICA.POTENCIA)
    elif t[2] == ':'    : t[0] = AritmeticaBinaria(t[1], t[3], OP_ARITMETICA.RANGO)
    
def p_aritmetica_negativo(t) :
    'exp_aritmetica : MINUS exp_aritmetica %prec UMINUS'
    t[0] = Negativo(t[2])

def p_aritmetica_agrupacion(t) :
    'exp_aritmetica : LPAR exp_logica RPAR'
    t[0] = t[2]

def p_aritmetica_basico_num(t) :
    'exp_aritmetica  : NUMERO'
    t[0] = Numero(t[1])

def p_aritmetica_basico_dec(t) :
    'exp_aritmetica : DECIMAL'
    t[0] = Numero(t[1])

def p_aritmetica_basico_char(t) :
    'exp_aritmetica : CARACTER'
    t[0] = Caracter(t[1])

def p_aritmetica_basico_str(t) :
    'exp_aritmetica : CADENA'
    t[0] = Cadena(t[1])

def p_aritmetica_basico_true(t) :
    'exp_aritmetica : TRUE'
    t[0] = BoolTrue(t[1])

def p_aritmetica_basico_false(t) :
    'exp_aritmetica : FALSE'
    t[0] = BoolFalse(t[1])

def p_aritmetica_basico_id(t) :
    'exp_aritmetica : ID'
    t[0] = Identificador(t[1])

def p_aritmetica_nativa_typeof(t) :
    'exp_aritmetica : TYPEOF LPAR exp_logica RPAR'
    t[0] = NativaTypeof(t[3])

def p_aritmetica_nativa_string(t) :
    'exp_aritmetica : STRING LPAR exp_logica RPAR'
    t[0] = NativaString(t[3])

def p_aritmetica_nativa_float(t) :
    'exp_aritmetica : FLOAT LPAR exp_logica RPAR'
    t[0] = NativaFloat(t[3])

def p_aritmetica_nativa_trunc(t) :
    'exp_aritmetica : TRUNC LPAR data_type COMMA exp_logica RPAR'
    t[0] = NativaTrunc(t[5])

def p_aritmetica_nativa_parse(t) :
    'exp_aritmetica : PARSE LPAR data_type COMMA exp_logica RPAR'
    t[0] = NativaParse(t[3], t[5])

def p_aritmetica_nativa_sin(t) :
    'exp_aritmetica : SIN LPAR exp_logica RPAR'
    t[0] = NativaSin(t[3])
    
def p_aritmetica_nativa_cos(t) :
    'exp_aritmetica : COS LPAR exp_logica RPAR'
    t[0] = NativaCos(t[3])
    
def p_aritmetica_nativa_tan(t) :
    'exp_aritmetica : TAN LPAR exp_logica RPAR'
    t[0] = NativaTan(t[3])
    
def p_aritmetica_nativa_log10(t) :
    'exp_aritmetica : LOG10 LPAR exp_logica RPAR'
    t[0] = NativaLog10(t[3])

def p_aritmetica_nativa_sqrt(t) :
    'exp_aritmetica : SQRT LPAR exp_logica RPAR'
    t[0] = NativaSqrt(t[3])
    
def p_aritmetica_nativa_length(t) :
    'exp_aritmetica : LENGTH LPAR exp_logica RPAR'
    t[0] = NativaLength(t[3])
    
def p_aritmetica_nativa_uppercase(t) :
    'exp_aritmetica : UPPERCASE LPAR exp_logica RPAR'
    t[0] = NativaUppercase(t[3])
    
def p_aritmetica_nativa_lowercase(t) :
    'exp_aritmetica : LOWERCASE LPAR exp_logica RPAR'
    t[0] = NativaLowercase(t[3])
    
def p_aritmetica_call(t) :
    'exp_aritmetica : ID LPAR arg RPAR'
    t[0] = CallFuncion(t[1], t[3])

def p_aritmetica_call_arg(t) :
    'arg : args'
    t[0] = t[1]

def p_aritmetica_call_empty(t) :
    'arg : empty'
    t[0] = []

def p_aritmetica_call_args_list(t) :
    'args : args COMMA exp_logica'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_aritmetica_call_args(t) :
    'args : exp_logica'
    t[0] = [t[1]]

def p_empty(t) :
    'empty :'
    pass
    
def p_error(t) :
    print(t)
    print(f'Error sintáctico: {t.value} no esperado')

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)