class Instruccion :
    '''Clase abstracta para instrucciones'''

class Print(Instruccion) :
    def __init__(self, exp) :
        self.exp = exp

    def __str__(self) -> str:
        return f'type: print exp: {self.exp}'

class Println(Instruccion) :
    def __init__(self, exp) :
        self.exp = exp

    def __str__(self) -> str:
        return f'type: print exp: {self.exp}'

class Mientras(Instruccion) :
    def __init__(self, condicion, instrucciones = []) :
        self.condicion = condicion
        self.instrucciones = instrucciones

    def __str__(self) -> str:
        return f'type: while cond: {self.condicion} instrucciones: {self.instrucciones}'

class Definicion(Instruccion) :
    def __init__(self, id, exp = None) :
        self.id = id
        self.exp = exp

    def __str__(self) -> str:
        return f'type: definicion id: {self.id} exp: {self.exp}'

class If(Instruccion) :
    def __init__(self, condicion, instrucciones = []) :
        self.condicion = condicion
        self.instrucciones = instrucciones

    def __str__(self) -> str:
        return f'type: if condicion: {self.condicion} then: {self.instrucciones}'

class IfElse(Instruccion) :
    def __init__(self, condicion, instrucciones_v = [], instrucciones_f = []) :
        self.condicion = condicion
        self.instrucciones_v = instrucciones_v
        self.instrucciones_f = instrucciones_f

    def __str__(self) -> str:
        return f'type: if condicion: {self.condicion} then: {self.instrucciones_v} else {self.instrucciones_f}'