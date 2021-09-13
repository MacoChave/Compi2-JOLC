import ts as TS
from expresiones import *
from instrucciones import *

def ejecutar_print(instruccion, ts) :
    print(ejecutar_cadena(instruccion.exp, ts))

def ejecutar_println(instruccion, ts) :
    print(ejecutar_cadena(instruccion.exp, ts), '\n')

def ejecutar_definicion(instruccion, ts) :
    if instruccion.exp == 0 :
        simbolo = TS.Simbolo(instruccion, TS.TIPO_DATO.NUMERO, 0)
        ts.agregar(simbolo)
    else :
        val = ejecutar_aritmetica(instruccion.exp, ts)
        simbolo = TS.Simbolo(instruccion.id, TS.TIPO_DATO.NUMERO, val)
        ts.actualizar(simbolo)

def ejecutar_mientras(instruccion, ts) :
    while ejecutar_logica(instruccion.condicion, ts) :
        ts_local = TS.TablaSimbolo(ts.simbolos)
        ejecutar_instrucciones(instruccion.instrucciones, ts_local)

def ejecutar_if(instruccion, ts) :
    val = ejecutar_logica(instruccion.condicion, ts)
    if val :
        ts_local = TS.TablaSimbolo(ts.simbolos)
        ejecutar_instrucciones(instruccion.instrucciones, ts_local)

def ejecutar_if_else(instruccion, ts) :
    val = ejecutar_logica(instruccion.condicion, ts)
    ts_local = TS.TablaSimbolo(ts.simbolos)
    if val :
        ejecutar_instrucciones(instruccion.instrucciones_v, ts_local)
    else :
        ejecutar_instrucciones(instruccion.instrucciones_f, ts_local)

def ejecutar_cadena(expresion, ts) :
    if isinstance(expresion, ExpresionCadenaSimple) :
        return expresion.val
    elif isinstance(expresion, ExpresionCadenaNumero) :
        return ejecutar_aritmetica(expresion.exp, ts)
    else :
        print('Error: Expresion cadena no válida')

def ejecutar_logica(expresion, ts) :
    exp1 = ejecutar_aritmetica(expresion.exp1, ts)
    exp2 = ejecutar_aritmetica(expresion.exp2, ts)
    if expresion.operador == OP_LOGIC.MENOR : return exp1 < exp2
    elif expresion.operador == OP_LOGIC.MENOR_IGUAL : return exp1 <= exp2
    elif expresion.operador == OP_LOGIC.MAYOR : return exp1 > exp2
    elif expresion.operador == OP_LOGIC.MAYOR_IGUAL : return exp1 >= exp2
    elif expresion.operador == OP_LOGIC.IGUAL : return exp1 == exp2
    elif expresion.operador == OP_LOGIC.DIFERENTE : return exp1 != exp2

def ejecutar_aritmetica(expresion, ts) :
    if isinstance(expresion, ExpresionBinaria) :
        exp1 = ejecutar_aritmetica(expresion.exp1, ts)
        exp2 = ejecutar_aritmetica(expresion.exp2, ts)
        if expresion.operador == OP_ARITHMETIC.MAS : return exp1 + exp2
        elif expresion.operador == OP_ARITHMETIC.MENOS : return exp1 - exp2
        elif expresion.operador == OP_ARITHMETIC.POR : return exp1 * exp2
        elif expresion.operador == OP_ARITHMETIC.DIVIDIDO : return exp1 / exp2
        elif expresion.operador == OP_ARITHMETIC.POTENCIA : return exp1 ** exp2
    elif isinstance(expresion, ExpresionNegativo) :
        exp1 = ejecutar_aritmetica(expresion.exp1, ts)
        return exp1 * -1
    elif isinstance(expresion, ExpresionNumero) :
        return expresion.val
    elif isinstance(expresion, ExpresionIdentificador) :
        return ts.obtener(expresion.id).valor

def ejecutar_instrucciones(instrucciones, ts = TS.TablaSimbolo()) :
    for instruccion in instrucciones :
        if isinstance(instruccion, Print) : ejecutar_print(instruccion, ts)
        elif isinstance(instruccion, Print) : ejecutar_println(instruccion, ts)
        elif isinstance(instruccion, Definicion) : ejecutar_definicion(instruccion, ts)
        elif isinstance(instruccion, Mientras) : ejecutar_mientras(instruccion, ts)
        elif isinstance(instruccion, If) : ejecutar_if(instruccion, ts)
        elif isinstance(instruccion, IfElse) : ejecutar_if_else(instruccion, ts)
        else : 
            print('Error semantico: Instrucción no válida')