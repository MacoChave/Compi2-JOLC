from datetime import datetime

class Error() :
    def __init__(self, tipo, descripcion, linea = 0, columna = 0) -> None:
        self.tipo = tipo
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna
        today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.fecha = today

class TablaError() :
    def __init__(self, errores = []) -> None:
        self.errores = errores
    
    def agregar(self, error) :
        self.errores.append(error)
    
    def count(self) :
        return self.errores.count()
