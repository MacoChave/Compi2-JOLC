from enum import Enum

class ALCANCE_VAR(Enum) :
    GLOBAL = 1
    LOCAL = 2
    EMPTY = 3

class Instruccion :
    '''Clase abstracta para instrucciones'''

class Print(Instruccion) :
    def __init__(self, exp, line = 0) :
        self.exp = exp
        self.line = line

    def __str__(self) -> str:
        return f'inst: print exp: {self.exp}' + '\n'

class Println(Instruccion) :
    def __init__(self, exp, line = 0) :
        self.exp = exp
        self.line = line

    def __str__(self) -> str:
        return f'inst: print exp: {self.exp}' + '\n'

class Mientras(Instruccion) :
    def __init__(self, condicion, instrucciones = [], line = 0) :
        self.condicion = condicion
        self.line = line
        self.instrucciones = instrucciones

    def __str__(self) -> str:
        return f'inst: while cond: {self.condicion} instrucciones: {self.instrucciones}' + '\n'

class Definicion(Instruccion) :
    def __init__(self, alcance, id, exp, line = 0) :
        self.alcance = alcance
        self.id = id
        self.exp = exp
        self.line = line

    def __str__(self) -> str:
        return f'inst: definicion id: {self.id} exp: {self.exp}' + '\n'

class If(Instruccion) :
    def __init__(self, condicion, instrucciones = [], line = 0) :
        self.condicion = condicion
        self.line = line
        self.instrucciones = instrucciones

    def __str__(self) -> str:
        return f'inst: if condicion: {self.condicion} then: {self.instrucciones}' + '\n'

class IfElse(Instruccion) :
    def __init__(self, condicion, instrucciones_v = [], instrucciones_f = [], line = 0) :
        self.condicion = condicion
        self.line = line
        self.instrucciones_v = instrucciones_v
        self.instrucciones_f = instrucciones_f

    def __str__(self) -> str:
        return f'inst: if condicion: {self.condicion} then: {self.instrucciones_v} else {self.instrucciones_f}' + '\n'

class For(Instruccion) :
    def __init__(self, inicio, lista, instrucciones) -> None:
        self.inicio = inicio
        self.lista = lista
        self.instrucciones = instrucciones
    
    def __str__(self) -> str:
        return f'inicio: {self.inicio} lista: {self.lista} instrucciones: {self.instrucciones}' + '\n'

class Funcion(Instruccion) :
    def __init__(self, id, instrucciones, parametros = None) -> None:
        self.id = id
        self.instrucciones = instrucciones
        self.parametros = parametros
    
    def __str__(self) -> str:
        return super().__str__()