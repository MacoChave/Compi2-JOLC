from enum import Enum

class TIPO_DATO(Enum) :
    NUMERO = 1

class Simbolo() :
    def __init__(self, id, tipo, valor) -> None:
        self.id = id
        self.tipo = tipo
        self.valor = valor

class TablaSimbolo() :
    def __init__(self, simbolos = {}) -> None:
        self.simbolos = simbolos
    
    def agregar(self, simbolo) :
        self.simbolos[simbolo.id] = simbolo
    
    def obtener(self, id) :
        if not id in self.simbolos :
            return None
        return self.simbolos[id]
    
    def actualizar(self, simbolo) :
        if not simbolo.id in self.simbolos :
            return None
        else :
            self.simbolo[simbolo.id] = simbolo