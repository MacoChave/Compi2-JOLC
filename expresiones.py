from enum import Enum

class OP_ARITHMETIC(Enum) :
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    POTENCIA = 5

class OP_LOGIC(Enum) :
    MAYOR = 1
    MENOR = 2
    MAYOR_IGUAL = 3
    MENOR_IGUAL = 4
    IGUAL = 5
    DIFERENTE = 6

class ExpresionNumerica :
    '''Clase para expresiones numéricas'''

class ExpresionBinaria(ExpresionNumerica) :
    '''Clase para expresión aritmetica binaria'''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionNegativo(ExpresionNumerica) :
    '''Clase para expresión aritmetica negativa'''

    def __init__(self, exp1) :
        self.exp1 = exp1

class ExpresionNumero(ExpresionNumerica) :
    '''Clase para numero o decimal'''

    def __init__(self, val = 0) :
        self.val = val

class ExpresionIdentificador(ExpresionNumerica) :
    '''Clase para identificadores'''

    def __init__(self, id = '') :
        self.id = id

class ExpresionCadena :
    '''Clase para cadenas'''

class ExpresionCadenaSimple(ExpresionCadena) :
    '''Clase para una cadena normal'''
    def __init__(self, val = '') :
        self.val = val

class ExpresionCadenaNumero(ExpresionCadena) :
    '''Clase para una cadena tratada como número'''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionLogica() :
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador