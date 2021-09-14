from enum import Enum

class TIPO_DATO(Enum) :
    NUMERO = 1

class Simbolo() :
    def __init__(self, id, valor = None) -> None:
        self.id = id
        self.valor = valor

class TablaSimbolo() :
    def __init__(self, simbolos = {}) -> None:
        self.simbolos = simbolos
    
    def agregar(self, simbolo) :
        self.simbolos[simbolo.id] = simbolo
    
    def obtener(self, id) :
        if not id in self.simbolos :
            simbolo = Simbolo(id)
            self.agregar(simbolo)
            return simbolo

        return self.simbolos[id]
    
    def actualizar(self, simbolo) :
        self.simbolos[simbolo.id] = simbolo