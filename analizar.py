from funciones import *
import ts as TS
from expresiones import *
from instrucciones import *

def ejecutar_print(instruccion, ts) -> str :
    res = ''
    for instr in instruccion.exp :
        cadena = ejecutar_logica(instr, ts)
        if cadena is None : 
            # TODO: Agregar error
            print('Error semántico, En print, no hay expresión para imprimir')
            cadena = ''

        if isinstance(cadena, bool) :
            if cadena : res = 'True'
            else : res = 'False'
        res = f'{res}{cadena}'
    return res

def ejecutar_println(instruccion, ts) -> str :
    res = ''
    for instr in instruccion.exp :
        cadena = ejecutar_logica(instr, ts)
        if cadena is None : 
            # TODO: Agregar error
            print('Error semántico, En print, no hay expresión para imprimir')
            cadena = ''

        if isinstance(cadena, bool) :
            if cadena : res = 'True'
            else : res = 'False'
        res = f'{res}{cadena}'
        res = f'{res}\n'
    return res

def ejecutar_definicion(instruccion, ts) :
    simbolo = ts.obtener(instruccion.id)

    if not instruccion.exp is None :
        value = ejecutar_logica(instruccion.exp, ts)
        simbolo.valor = value
        ts.actualizar(simbolo)

def ejecutar_mientras(instruccion, ts) :
    cond = ejecutar_logica(instruccion.condicion, ts)
    response = ''
    if isinstance(cond, bool) :
        while cond :
            ts_local = TS.TablaSimbolo(ts.simbolos)
            response = f'{response}{ejecutar_instrucciones(instruccion.instrucciones, ts_local)}'
            cond = ejecutar_logica(instruccion.condicion, ts_local)
        return response
    else :
        # TODO: Agregar error
        print('Error semántico: En while. Se esperaba un tipo bool en la condición')

def ejecutar_if(instruccion, ts) :
    cond = ejecutar_logica(instruccion.condicion, ts)
    if isinstance(cond, bool) :
        if cond :
            ts_local = TS.TablaSimbolo(ts.simbolos)
            return ejecutar_instrucciones(instruccion.instrucciones, ts_local)
    else :
        # TODO: Agregar error
        print('Error semántico: En if. Se esperaba un tipo bool en la condición')

def ejecutar_if_else(instruccion, ts) :
    cond = ejecutar_logica(instruccion.condicion, ts)
    ts_local = TS.TablaSimbolo(ts.simbolos)
    if isinstance(cond, bool) :
        if cond :
            return ejecutar_instrucciones(instruccion.instrucciones_v, ts_local)
        else :
            return ejecutar_instrucciones(instruccion.instrucciones_f, ts_local)
    else: 
        # TODO: Agregar error
        print('Error semántico: En if else. Se esperaba un tipo bool en la condición')

def ejecutar_logica(expresion, ts) :
    if isinstance(expresion, LogicaBinaria) : 
        exp1 = ejecutar_logica(expresion.exp1, ts)
        exp2 = ejecutar_logica(expresion.exp2, ts)
        if not isinstance(exp1, bool) and not isinstance(exp2, bool) :
            # TODO: Agregar error
            print('Error semántico, En expresion lógica, se esperaban instancias de bool')
            return None

        if expresion.operador == OP_LOGICA.AND : exp1 and exp2
        if expresion.operador == OP_LOGICA.OR : exp1 or exp2
    elif isinstance(expresion, Negado) : 
        exp1 = ejecutar_logica(expresion.exp1, ts)
        if not isinstance(exp1, bool) :
            # TODO: Agregar error
            print('Error semántico, En not, se esperaba instancia de bool')
            return None
        
        return not exp1
    elif isinstance(expresion, ExpresionRelacional) : return ejecutar_relacional(expresion, ts)
    elif isinstance(expresion, ExpresionAritmetica) : return ejecutar_aritmetica(expresion, ts)
    elif isinstance(expresion, FuncionNativa) :
        return ejecutar_funcion_nativa(expresion, ts)
    
def ejecutar_relacional(expresion, ts) :
    if isinstance(expresion, ExpresionAritmetica) : return ejecutar_aritmetica(expresion, ts)
    elif isinstance(expresion, FuncionNativa) :
        return ejecutar_funcion_nativa(expresion, ts)
    
    exp1 = ejecutar_relacional(expresion.exp1, ts)
    exp2 = ejecutar_relacional(expresion.exp2, ts)

    if not ((isinstance(exp1, int) or isinstance(exp1, float)) and (isinstance(exp2, int) or isinstance(exp2, float))) : 
        # TODO: Agregar error
        print('Error semántico, En relacional, se esperaban instancias de Int64 o Float64')
        return None

    if expresion.operador == OP_RELACIONAL.MENOR : return exp1 < exp2
    elif expresion.operador == OP_RELACIONAL.MENOR_IGUAL : return exp1 <= exp2
    elif expresion.operador == OP_RELACIONAL.MAYOR : return exp1 > exp2
    elif expresion.operador == OP_RELACIONAL.MAYOR_IGUAL : return exp1 >= exp2
    elif expresion.operador == OP_RELACIONAL.IGUAL : return exp1 == exp2
    elif expresion.operador == OP_RELACIONAL.DIFERENTE : return exp1 != exp2

def ejecutar_aritmetica(expresion, ts) :
    if isinstance(expresion, AritmeticaBinaria) :
        exp1 = ejecutar_aritmetica(expresion.exp1, ts)
        exp2 = ejecutar_aritmetica(expresion.exp2, ts)
        
        if expresion.operador == OP_ARITMETICA.MAS :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                return exp1 + exp2
            if (isinstance(exp1, str) or isinstance(exp2, str)) :
                if isinstance(exp1, str) and len(exp1) == 1 : exp1 = int(exp1)
                if isinstance(exp2, str) and len(exp2) == 1 : exp2 = int(exp2)
                return exp1 + exp2
            
            # TODO: Agregar error
            print('Error semántico: En +, se esperaba Int64, Float64, Char o Bool')
            return None
        elif expresion.operador == OP_ARITMETICA.MENOS :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                return exp1 - exp2
            
            # TODO: Agregar error
            print('Error semántico: En -, se esperaba Int64, Float64 o Bool')
            return None
        elif expresion.operador == OP_ARITMETICA.POR :
            if isinstance(exp1, bool) and isinstance(exp2, bool) : return bool(exp1 * exp2)
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                if isinstance(exp1, bool) and isinstance(exp2, bool) :
                    return bool(exp1 * exp2)
                return exp1 * exp2
            if isinstance(exp1, str) and isinstance(exp2, str) : return exp1 + exp2
            
            # TODO: Agregar error
            print('Error semántico: En *, se esperaba Int64, Float64 o Bool')
            return None
        elif expresion.operador == OP_ARITMETICA.DIVIDIDO :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                return exp1 / exp2
            
            # TODO: Agregar error
            print('Error semántico: En /, se esperaba Int64, Float64 o Bool')
            return None
        elif expresion.operador == OP_ARITMETICA.MODULO :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                return exp1 % exp2
            
            # TODO: Agregar error
            print('Error semántico: En %, se esperaba Int64, Float64 o Bool')
            return None
        elif expresion.operador == OP_ARITMETICA.POTENCIA :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                if isinstance(exp1, bool) : return bool(exp1 ** exp2)
                return exp1 ** exp2
            elif isinstance(exp1, str) and (isinstance(exp2, int) or isinstance(exp2, float)) :
                return exp1 * exp2
            
            # TODO: Agregar error
            print('Error semántico: En ^, se esperaba Int64, Float64, Bool o string ^ Int64')
            return None
    elif isinstance(expresion, Negativo) :
        exp1 = ejecutar_aritmetica(expresion.exp1, ts)
        if isinstance(exp1, int) or isinstance(exp1, float) :
            return exp1 * -1
        # TODO: Agregar error
        print('Error semántico: En negativo, se esperaba Int64 o Float64')
    elif isinstance(expresion, Numero) :
        return expresion.val
    elif isinstance(expresion, Caracter) :
        return expresion.val
    elif isinstance(expresion, Cadena) :
        return expresion.val
    elif isinstance(expresion, BoolTrue) :
        return True
    elif isinstance(expresion, BoolFalse) :
        return False
    elif isinstance(expresion, Identificador) :
        return ts.obtener(expresion.id).valor
    elif isinstance(expresion, FuncionNativa) :
        return ejecutar_funcion_nativa(expresion, ts)

def ejecutar_funcion_nativa(expresion, ts) :
    exp = ejecutar_logica(expresion.exp, ts)
    if isinstance(expresion, NativaParse) :
        if isinstance(exp, str) : 
            print(expresion.tipo)
            if expresion.tipo == DATA_TYPE.NUMERO : return int(exp)
            elif expresion.tipo == DATA_TYPE.DECIMAL : return float(exp)
            else : 
                print('Error semántico: En parse, se esperaba convertir a Int64 o Float64')
                return None
        else :
            print('Error semántico: En parse, se esperaba convertir de string')
            return None
    if isinstance(expresion, NativaTrunc) :
        if isinstance(exp, float) :
            return int(exp)
        elif isinstance(exp, int) :
            return exp
        else :
            print('Error semántico: En trunc, se esperaba un tipo Float64')
            return None
    if isinstance(expresion, NativaFloat) :
        if isinstance(exp, int) :
            return float(exp)
        elif isinstance(exp, float) :
            return exp
        else :
            print('Error semántico: En float, se esperaba un tipo Int64')
            return None
    if isinstance(expresion, NativaString) :
        if isinstance(exp, int) or isinstance(exp, float) :
            return str(exp)
        else :
            print('Error semántico: En string, se esperaba un tipo Int64 o Float64')
            return None
    if isinstance(expresion, NativaTypeof) :
        if isinstance(exp, int) : return 'Int64'
        elif isinstance(exp, float) : return 'Float64'
        elif isinstance(exp, str) : return 'String'
        elif isinstance(exp, bool) : return 'Bool'
        elif isinstance(exp, str) : return 'Char'
        else : return None

def ejecutar_instrucciones(instrucciones, ts = TS.TablaSimbolo()) :
    response = ''
    for instruccion in instrucciones :
        if isinstance(instruccion, Print) : 
            response = f'{response}{ejecutar_print(instruccion, ts)}'
        elif isinstance(instruccion, Println) : 
            response = f'{response}{ejecutar_println(instruccion, ts)}'
        elif isinstance(instruccion, Definicion) : ejecutar_definicion(instruccion, ts)
        elif isinstance(instruccion, Mientras) : 
            response = f'{response}{ejecutar_mientras(instruccion, ts)}'
        elif isinstance(instruccion, If) : 
            response = f'{response}{ejecutar_if(instruccion, ts)}'
        elif isinstance(instruccion, IfElse) : 
            response = f'{response}{ejecutar_if_else(instruccion, ts)}'
        else : 
            print('Error semantico: Instrucción no válida')
    return response