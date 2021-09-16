from enum import Enum

class DATA_TYPE(Enum) :
    NUMERO = 1
    DECIMAL = 2
    CADENA = 3
    CARACTER = 4
    BOLEANO = 5

class FuncionNativa :
    '''Clase abstracta para funciones'''

class NativaParse(FuncionNativa) :
    def __init__(self, tipo, exp) -> None:
        self.tipo = tipo
        self.exp = exp

class NativaTrunc(FuncionNativa) :
    def __init__(self, exp) -> None:
        self.exp = exp

class NativaFloat(FuncionNativa) :
    def __init__(self, exp) -> None:
        self.exp = exp

class NativaString(FuncionNativa) :
    def __init__(self, exp) -> None:
        self.exp = exp

class NativaTypeof(FuncionNativa) :
    def __init__(self, exp) -> None:
        self.exp = exp

class NativaSin(FuncionNativa) :
    def __init__(self, exp) -> None:
        self.exp = exp

class NativaCos(FuncionNativa) :
    def __init__(self, exp) -> None:
        self.exp = exp

class NativaTan(FuncionNativa) :
    def __init__(self, exp) -> None:
        self.exp = exp

class NativaLog10(FuncionNativa) :
    def __init__(self, exp) -> None:
        self.exp = exp

class NativaSqrt(FuncionNativa) :
    def __init__(self, exp) -> None:
        self.exp = exp
