from typing import List
import ts as TS
from te import Error
import math
from funciones import *
from expresiones import *
from instrucciones import *

def ejecutar_print(instruccion, ts, lista_error: List[Error]) -> str :
    res = ''
    for instr in instruccion.exp :
        print(instr)
        cadena = ejecutar_logica(instr, ts, lista_error)
        print(instruccion)
        if cadena is None : 
            # TODO: Agregar error
            print('Error semántico, En print, no hay expresión para imprimir')
            lista_error.append(Error('Error semántico', 'En print se esperaba una expresión válida'))
            cadena = ''

        if isinstance(cadena, bool) :
            if cadena : cadena = 'True'
            else : cadena = 'False'
        res = f'{res}{cadena}'
    return res

def ejecutar_println(instruccion, ts, lista_error: List[Error]) -> str :
    res = ''
    for instr in instruccion.exp :
        print(instr)
        cadena = ejecutar_logica(instr, ts, lista_error)
        if cadena is None : 
            # TODO: Agregar error
            print('Error semántico, En print, no hay expresión para imprimir')
            lista_error.append(Error('Error semántico', 'En println se esperaba una expresión válida'))
            cadena = ''

        if isinstance(cadena, bool) :
            if cadena : cadena = 'True'
            else : cadena = 'False'
        res = f'{res}{cadena}'

    res = f'{res}\n'
    return res

def ejecutar_definicion(instruccion, ts, lista_error: List[Error]) :
    simbolo = ts.obtener(instruccion.id)
    print(instruccion)

    if not instruccion.exp is None :
        value = ejecutar_logica(instruccion.exp, ts, lista_error)
        simbolo.valor = value
        ts.actualizar(simbolo)
        print(ts)

def ejecutar_mientras(instruccion, ts, lista_error: List[Error]) :
    cond = ejecutar_logica(instruccion.condicion, ts, lista_error)
    response = ''
    if isinstance(cond, bool) :
        while cond :
            ts_local = TS.TablaSimbolo(ts.simbolos)
            response = f'{response}{ejecutar_instrucciones(instruccion.instrucciones, ts_local, lista_error)}'
            cond = ejecutar_logica(instruccion.condicion, ts_local, lista_error)
        return response
    else :
        # TODO: Agregar error
        print('Error semántico: En while. Se esperaba un tipo bool en la condición')
        lista_error.append(Error('Error semántico', 'La condición del while esperaba tipo ::Bool'))

def ejecutar_if(instruccion, ts, lista_error: List[Error]) :
    cond = ejecutar_logica(instruccion.condicion, ts, lista_error)
    if isinstance(cond, bool) :
        if cond :
            ts_local = TS.TablaSimbolo(ts.simbolos)
            return ejecutar_instrucciones(instruccion.instrucciones, ts_local, lista_error)
    else :
        # TODO: Agregar error
        print('Error semántico: En if. Se esperaba un tipo bool en la condición')
        lista_error.append('Error semántico', 'La condición del if esperaba un tipo ::Bool')

def ejecutar_if_else(instruccion, ts, lista_error: List[Error]) :
    cond = ejecutar_logica(instruccion.condicion, ts, lista_error)
    ts_local = TS.TablaSimbolo(ts.simbolos)
    if isinstance(cond, bool) :
        if cond :
            return ejecutar_instrucciones(instruccion.instrucciones_v, ts_local, lista_error)
        else :
            return ejecutar_instrucciones(instruccion.instrucciones_f, ts_local, lista_error)
    else: 
        # TODO: Agregar error
        print('Error semántico: En if else. Se esperaba un tipo bool en la condición')
        lista_error.append('Error semántico', 'La condición del if esperaba un tipo ::Bool')

def ejecutar_logica(expresion, ts, lista_error: List[Error]) :
    if isinstance(expresion, LogicaBinaria) : 
        exp1 = ejecutar_logica(expresion.exp1, ts, lista_error)
        exp2 = ejecutar_logica(expresion.exp2, ts, lista_error)
        if not isinstance(exp1, bool) and not isinstance(exp2, bool) :
            # TODO: Agregar error
            print('Error semántico, En expresion lógica, se esperaban instancias de bool')
            lista_error.append('Error semántico', 'Se esperaba comparar un tipo ::Bool en la condición lógica')
            return None

        if expresion.operador == OP_LOGICA.AND : return exp1 and exp2
        if expresion.operador == OP_LOGICA.OR : return exp1 or exp2
    elif isinstance(expresion, Negado) : 
        exp1 = ejecutar_logica(expresion.exp1, ts, lista_error)
        if not isinstance(exp1, bool) :
            # TODO: Agregar error
            print('Error semántico, En not, se esperaba instancia de bool')
            lista_error.append('Error semántico', 'Se esperaba comparar un tipo ::Bool en la condición lógica')
            return None
        
        return not exp1
    elif isinstance(expresion, ExpresionRelacional) : return ejecutar_relacional(expresion, ts, lista_error)
    elif isinstance(expresion, ExpresionAritmetica) : return ejecutar_aritmetica(expresion, ts, lista_error)
    elif isinstance(expresion, FuncionNativa) :
        return ejecutar_funcion_nativa(expresion, ts, lista_error)
    
def ejecutar_relacional(expresion, ts, lista_error: List[Error]) :
    if isinstance(expresion, ExpresionAritmetica) : return ejecutar_aritmetica(expresion, ts, lista_error)
    elif isinstance(expresion, FuncionNativa) :
        return ejecutar_funcion_nativa(expresion, ts, lista_error)
    
    exp1 = ejecutar_relacional(expresion.exp1, ts, lista_error)
    exp2 = ejecutar_relacional(expresion.exp2, ts, lista_error)

    if isinstance(exp1, str) and isinstance(exp2, str) : 
        if expresion.operador == OP_RELACIONAL.MENOR : return exp1 < exp2
        elif expresion.operador == OP_RELACIONAL.MENOR_IGUAL : return exp1 <= exp2
        elif expresion.operador == OP_RELACIONAL.MAYOR : return exp1 > exp2
        elif expresion.operador == OP_RELACIONAL.MAYOR_IGUAL : return exp1 >= exp2
        elif expresion.operador == OP_RELACIONAL.IGUAL : return exp1 == exp2
        elif expresion.operador == OP_RELACIONAL.DIFERENTE : return exp1 != exp2
    elif isinstance(exp1, str) or isinstance(exp2, str) :
        print('Error semántico: En operación relacional, se esperaba comparar string y string')
        lista_error.append(Error('Error semántico', 'Se esperaba comparar ::String con ::String'))
        return None
    else :
        if expresion.operador == OP_RELACIONAL.MENOR : return exp1 < exp2
        elif expresion.operador == OP_RELACIONAL.MENOR_IGUAL : return exp1 <= exp2
        elif expresion.operador == OP_RELACIONAL.MAYOR : return exp1 > exp2
        elif expresion.operador == OP_RELACIONAL.MAYOR_IGUAL : return exp1 >= exp2
        elif expresion.operador == OP_RELACIONAL.IGUAL : return exp1 == exp2
        elif expresion.operador == OP_RELACIONAL.DIFERENTE : return exp1 != exp2

def ejecutar_aritmetica(expresion, ts, lista_error: List[Error]) :
    if isinstance(expresion, AritmeticaBinaria) :
        exp1 = ejecutar_aritmetica(expresion.exp1, ts, lista_error)
        exp2 = ejecutar_aritmetica(expresion.exp2, ts, lista_error)
        
        if expresion.operador == OP_ARITMETICA.MAS :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                return exp1 + exp2
            if (isinstance(exp1, str) or isinstance(exp2, str)) :
                if isinstance(exp1, str) and len(exp1) == 1 : exp1 = int(exp1)
                if isinstance(exp2, str) and len(exp2) == 1 : exp2 = int(exp2)
                return exp1 + exp2
            
            # TODO: Agregar error
            print('Error semántico: En +, se esperaba Int64, Float64, Char o Bool')
            lista_error.append(Error('Error semántico', 'Se esperaba sumar tipos ::Int64, ::Float64, ::Char o ::Bool'))
            return None
        elif expresion.operador == OP_ARITMETICA.MENOS :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                return exp1 - exp2
            
            # TODO: Agregar error
            print('Error semántico: En -, se esperaba Int64, Float64 o Bool')
            lista_error.append(Error('Error semántico', 'Se esperaba restar tipos ::Int64, ::Float64 o ::Bool'))
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
            lista_error.append(Error('Error semántico', 'Se esperaba sumar tipos ::Int64, ::Float64 o Bool'))
            return None
        elif expresion.operador == OP_ARITMETICA.DIVIDIDO :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                return exp1 / exp2
            
            # TODO: Agregar error
            print('Error semántico: En /, se esperaba Int64, Float64 o Bool')
            lista_error.append(Error('Error semántico', 'Se esperaba dividir tipos ::Int64, ::Float64 o ::Bool'))
            return None
        elif expresion.operador == OP_ARITMETICA.MODULO :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                return exp1 % exp2
            
            # TODO: Agregar error
            print('Error semántico: En %, se esperaba Int64, Float64 o Bool')
            lista_error.append(Error('Error semántico', 'Se esperaba obtener el módulo de los tipos ::Int64, ::Float64 o ::Bool'))
            return None
        elif expresion.operador == OP_ARITMETICA.POTENCIA :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                if isinstance(exp1, bool) : return bool(exp1 ** exp2)
                return exp1 ** exp2
            elif isinstance(exp1, str) and (isinstance(exp2, int) or isinstance(exp2, float)) :
                return exp1 * exp2
            
            # TODO: Agregar error
            print('Error semántico: En ^, se esperaba Int64, Float64, Bool o string ^ Int64')
            lista_error.append(Error('Error semántico', 'Se esperaba obtener la potencia de tipos ::Int64, ::Float64 o ::Bool, ::String ^ ::Int64'))
            return None
        elif expresion.operador == OP_ARITMETICA.RANGO : 
            if isinstance(exp1, int) and isinstance(exp2, int) :
                if exp2 > exp1 :
                    return range(exp1, exp2 + 1) # RETURN TYPE RANGE
                else :
                    print('Error semántico: En rango, El segundo término debe ser mayor al primero')
                    lista_error.append('Error semántico', 'El segundo término debe ser mayor al primero')
            else :
                print('Error semántico: En rango, se esperaban rangos de ::Int64')
                lista_error.append('Error semántico', 'Se esperaban tipo ::Int64')
                return None
    elif isinstance(expresion, Negativo) :
        exp1 = ejecutar_aritmetica(expresion.exp1, ts, lista_error)
        if isinstance(exp1, int) or isinstance(exp1, float) :
            return exp1 * -1
        # TODO: Agregar error
        print('Error semántico: En negativo, se esperaba Int64 o Float64')
        lista_error.append(Error('Error semántico', 'Se esperaba los tipos ::Int64 o ::Float64'))
        return None
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
        return ejecutar_funcion_nativa(expresion, ts, lista_error)

def ejecutar_funcion_nativa(expresion, ts, lista_error: List[Error]) :
    exp = ejecutar_logica(expresion.exp, ts, lista_error)
    if isinstance(expresion, NativaParse) :
        if isinstance(exp, str) :
            if exp.isnumeric() or exp.isdecimal() :
                if expresion.tipo == DATA_TYPE.NUMERO : return int(exp)
                elif expresion.tipo == DATA_TYPE.DECIMAL : return float(exp)
                else : 
                    print('Error semántico: En parse, se esperaba convertir a Int64 o Float64')
                    lista_error.append(Error('Error semántico', 'Se esperaba convertir a ::Int64 a ::Float64'))
                    return None
            else :
                print('Error semántico: En parse, la cadena no se puede convertir a Int64 o Float64')
                lista_error.append(Error('Error semántico', 'Se esperaba convertir un tipo ::Int64 o ::Float64'))
                return None
        else :
            print('Error semántico: En parse, se esperaba convertir de string')
            lista_error.append(Error('Error semántico', 'Se esperaba convertir un tipo ::String'))
            return None
    elif isinstance(expresion, NativaTrunc) :
        if isinstance(exp, float) :
            return int(exp)
        elif isinstance(exp, int) :
            return exp
        else :
            print('Error semántico: En trunc, se esperaba un tipo Float64')
            lista_error.append(Error('Error semántico', 'Se esperaba convertir un tipo ::Float64'))
            return None
    elif isinstance(expresion, NativaFloat) :
        if isinstance(exp, int) :
            return float(exp)
        elif isinstance(exp, float) :
            return exp
        else :
            print('Error semántico: En float, se esperaba un tipo Int64')
            lista_error.append(Error('Error semántico', 'Se esperaba un tipo ::Int64'))
            return None
    elif isinstance(expresion, NativaString) :
        if isinstance(exp, int) or isinstance(exp, float) :
            return str(exp)
        else :
            print('Error semántico: En string, se esperaba un tipo Int64 o Float64')
            lista_error.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(expresion, NativaTypeof) :
        if isinstance(exp, int) : return 'Int64'
        elif isinstance(exp, float) : return 'Float64'
        elif isinstance(exp, str) : return 'String'
        elif isinstance(exp, bool) : return 'Bool'
        elif isinstance(exp, str) : return 'Char'
        else : return None
    elif isinstance(expresion, NativaSin) :
        if isinstance(exp, int) or isinstance(exp, float) :
            return math.sin(exp)
        else :
            print('Error semántico: Sin solo acepta Int64 o Float64')
            lista_error.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(expresion, NativaCos) :
        if isinstance(exp, int) or isinstance(exp, float) :
            return math.cos(exp)
        else :
            print('Error semántico: Cos solo acepta Int64 o Float64')
            lista_error.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(expresion, NativaTan) :
        if isinstance(exp, int) or isinstance(exp, float) :
            return math.tan(exp)
        else :
            print('Error semántico: Tan solo acepta Int64 o Float64')
            lista_error.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(expresion, NativaLog10) :
        if isinstance(exp, int) or isinstance(exp, float) :
            return math.log10(exp)
        else :
            print('Error semántico: Log10 solo acepta Int64 o Float64')
            lista_error.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(expresion, NativaSqrt) :
        if isinstance(exp, int) or isinstance(exp, float) :
            return math.sqrt(exp)
        else :
            print('Error semántico: Sqrt solo acepta Int64 o Float64')
            lista_error.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(expresion, NativaLength) :
        if isinstance(exp, str) :
            return len(exp)
        else :
            print('Error semántico: length solo acepta Int64 o Float64')
            lista_error.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(expresion, NativaUppercase) :
        if isinstance(exp, str) :
            return exp.upper()
        else :
            print('Error semántico: uppercase solo acepta Int64 o Float64')
            lista_error.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(expresion, NativaLowercase) :
        if isinstance(exp, str) :
            return exp.lower()
        else :
            print('Error semántico: lowercase solo acepta Int64 o Float64')
            lista_error.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None

def ejecutar_instrucciones(instrucciones, ts, lista_error: List[Error]) :
    response = ''
    for instruccion in instrucciones :
        if isinstance(instruccion, Print) : 
            response = f'{response}{ejecutar_print(instruccion, ts, lista_error)}'
        elif isinstance(instruccion, Println) : 
            response = f'{response}{ejecutar_println(instruccion, ts, lista_error)}'
        elif isinstance(instruccion, Definicion) : ejecutar_definicion(instruccion, ts, lista_error)
        elif isinstance(instruccion, Mientras) : 
            response = f'{response}{ejecutar_mientras(instruccion, ts, lista_error)}'
        elif isinstance(instruccion, If) : 
            response = f'{response}{ejecutar_if(instruccion, ts, lista_error)}'
        elif isinstance(instruccion, IfElse) : 
            response = f'{response}{ejecutar_if_else(instruccion, ts, lista_error)}'
        else : 
            print('Error semantico: Instrucción no válida')
            lista_error.append(Error('Error semántico', 'Instrucción no reconocida', 0))
    return response