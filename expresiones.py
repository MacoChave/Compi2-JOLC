from enum import Enum

class OP_ARITMETICA(Enum) :
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    MODULO = 5
    POTENCIA = 6
    RANGO = 7

class OP_RELACIONAL(Enum) :
    MAYOR = 1
    MENOR = 2
    MAYOR_IGUAL = 3
    MENOR_IGUAL = 4
    IGUAL = 5
    DIFERENTE = 6

class OP_LOGICA(Enum) :
    AND = 1
    OR = 2
    NOT = 3

class ExpresionAritmetica :
    '''Clase para ExpresionAritmeticaes numéricas'''

class AritmeticaBinaria(ExpresionAritmetica) :
    def __init__(self, exp1, exp2, operador, line = 0) :
        self.line = line
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
    
    def __str__(self) -> str:
        return f'Expresion: aritmetica binaria exp1: {self.exp1} exp2: {self.exp2} operador: {self.operador}' + '\n'

class Negativo(ExpresionAritmetica) :
    def __init__(self, exp1, line = 0) :
        self.line = line
        self.exp1 = exp1
    
    def __str__(self) -> str:
        return f'Expresion: negativo exp1: {self.exp1}' + '\n'

class Numero(ExpresionAritmetica) :
    def __init__(self, val = 0, line = 0) :
        self.line = line
        self.val = val
    
    def __str__(self) -> str:
        return f'Expresion: numero val: {self.val}' + '\n'

class Identificador(ExpresionAritmetica) :
    def __init__(self, id = '', line = 0) :
        self.line = line
        self.id = id
    
    def __str__(self) -> str:
        return f'Expresion: identificador id: {self.id}' + '\n'

class Cadena(ExpresionAritmetica) :
    def __init__(self, val = '', line = 0) :
        self.line = line
        self.val = val
    
    def __str__(self) -> str:
        return f'Expresion: cadena val: {self.val}' + '\n'

class BoolTrue(ExpresionAritmetica) :
    def __init__(self, val, line = 0) :
        self.line = line
        self.val = val
    
    def __str__(self) -> str:
        return f'Expresion: true val: {self.val}' + '\n'

class BoolFalse(ExpresionAritmetica) :
    def __init__(self, val, line = 0) :
        self.line = line
        self.val = val
    
    def __str__(self) -> str:
        return f'Expresion: false val: {self.val}' + '\n'

class Caracter(ExpresionAritmetica) :
    def __init__(self, val, line = 0) :
        self.line = line
        self.val = val
    
    def __str__(self) -> str:
        return f'Expresion: caracter  val: {self.val}' + '\n'

class Ternario(ExpresionAritmetica) :
    def __init__(self, condicion, exp_then, exp_else, line = 0) :
        self.line = line
        self.condicion = condicion
        self.exp_then = exp_then
        self.exp_else = exp_else

class ExpresionLogica :
    '''Clase para expresiones lógicas'''

class LogicaBinaria(ExpresionLogica) :
    def __init__(self, exp1, exp2, operador, line = 0) :
        self.line = line
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
    
    def __str__(self) -> str:
        return f'Expresion: logica binaria exp1: {self.exp1} exp2: {self.exp2} operador: {self.operador}' + '\n'

class Negado(ExpresionLogica) :
    def __init__(self, exp1, operador, line = 0) :
        self.line = line
        self.exp1 = exp1
        self.operador = operador
    
    def __str__(self) -> str:
        return f'Expresion: not exp1: {self.exp1} operador: {self.operador}' + '\n'

class ExpresionRelacional() :
    def __init__(self, exp1, exp2, operador, line = 0) :
        self.line = line
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
    
    def __str__(self) -> str:
        return f'Expresion: relacional exp2: {self.exp1} exp2: {self.exp2} operador: {self.operador}' + '\n'