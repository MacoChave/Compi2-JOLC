from enum import Enum

class OP_ARITMETICA(Enum) :
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    POTENCIA = 5

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
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class Negativo(ExpresionAritmetica) :
    def __init__(self, exp1) :
        self.exp1 = exp1

class Numero(ExpresionAritmetica) :
    def __init__(self, val = 0) :
        self.val = val

class Identificador(ExpresionAritmetica) :
    def __init__(self, id = '') :
        self.id = id

class Cadena(ExpresionAritmetica) :
    def __init__(self, val = '') :
        self.val = val

class BoolTrue(ExpresionAritmetica) :
    def __init__(self, val) :
        self.val = val

class BoolFalse(ExpresionAritmetica) :
    def __init__(self, val) :
        self.val = val

class Caracter(ExpresionAritmetica) :
    def __init__(self, val) :
        self.val = val

class ExpresionLogica :
    '''Clase para expresiones lógicas'''

class LogicaBinaria(ExpresionLogica) :
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class Negado(ExpresionLogica) :
    def __init__(self, exp1, operador) :
        self.exp1 = exp1
        self.operador = operador

class ExpresionRelacional() :
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador