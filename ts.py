class Simbolo() :
    id = ''
    valor = None
    data_type = None

    def __init__(self, id, valor = None, data_type = None) -> None:
        self.id = id
        self.valor = valor
        self.data_type = data_type
    
    def __str__(self) -> str:
        return f'id: {self.id}, valor: {self.valor}, data_type: {self.data_type}' + '\n'

class TablaSimbolo() :
    simbolos = {}
    
    def __init__(self, simbolos = {}) -> None:
        self.simbolos = simbolos
    
    def __str__(self) -> str:
        return str(self.simbolos)
    
    def agregar(self, simbolo) :
        self.simbolos[simbolo.id] = simbolo
    
    def declarar(self, id) :
        if not id in self.simbolos :
            simbolo = Simbolo(id)
            self.agregar(simbolo)
            return simbolo

        return self.simbolos[id]
    
    def obtener(self, id) :
        if not id in self.simbolos :
            return None
        
        return self.simbolos[id]
    
    def actualizar(self, simbolo) :
        if not simbolo.id in self.simbolos : return False

        self.simbolos[simbolo.id] = simbolo
        return True