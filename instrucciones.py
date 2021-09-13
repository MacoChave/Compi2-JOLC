class Instruccion :
    '''Clase abstracta para instrucciones'''

class Print(Instruccion) :
    def __init__(self, exp) :
        self.exp = exp

    def __str__(self) -> str:
        return 'Instancia print'

class Println(Instruccion) :
    def __init__(self, exp) :
        self.exp = exp

    def __str__(self) -> str:
        return 'Instancia println'

class Mientras(Instruccion) :
    def __init__(self, condicion, instrucciones = []) :
        self.condicion = condicion
        self.instrucciones = instrucciones

    def __str__(self) -> str:
        return 'Instancia mientras'

class Definicion(Instruccion) :
    def __init__(self, id, exp = 0) :
        self.id = id
        self.exp = exp

    def __str__(self) -> str:
        return 'Instancia definicion'

class If(Instruccion) :
    def __init__(self, condicion, instrucciones = []) :
        self.condicion = condicion
        self.instrucciones = instrucciones

    def __str__(self) -> str:
        return 'Instancia if'

class IfElse(Instruccion) :
    def __init__(self, condicion, instrucciones_v = [], instrucciones_f = []) :
        self.condicion = condicion
        self.instrucciones_v = instrucciones_v
        self.instrucciones_f = instrucciones_f

    def __str__(self) -> str:
        return 'Instancia if else'