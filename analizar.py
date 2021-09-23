from typing import List
import ts as TS
from te import Error
import math
from funciones import *
from expresiones import *
from instrucciones import *

globales = TS.TablaSimbolo()
errores: List[Error] = []
response = ''

# ========== ==========> PRINT

def ejecutar_print(instruccion: Print, locales: TS.TablaSimbolo, globales_inner: TS.TablaSimbolo) :
    global response
    global errores
    for instr in instruccion.exp :
        cadena = ejecutar_logica(instr, locales, globales_inner)
        if cadena is None :
            print('Error semántico, En print, no hay expresión para imprimir')
            errores.append(Error('Error semántico', 'En print se esperaba una expresión válida'))
            cadena = ''

        if isinstance(cadena, bool) :
            if cadena : cadena = 'True'
            else : cadena = 'False'
        response = f'{response}{cadena}'
    # print(response)

def ejecutar_println(instruccion: Println, locales: TS.TablaSimbolo, globales_inner: TS.TablaSimbolo) :
    global response
    global errores
    for instr in instruccion.exp :
        cadena = ejecutar_logica(instr, locales, globales_inner)
        if cadena is None :
            print('Error semántico, En print, no hay expresión para imprimir')
            errores.append(Error('Error semántico', 'En println se esperaba una expresión válida'))
            cadena = ''

        if isinstance(cadena, bool) :
            if cadena : cadena = 'True'
            else : cadena = 'False'
        response = f'{response}{cadena}'

    response = f'{response}\n'
    # print(response)

# ========== ==========> DECLARACIÓN

def ejecutar_definicion(instruccion: Definicion, locales: TS.TablaSimbolo, globales_inner: TS.TablaSimbolo) :
    global globales
    # VARIABLE GLOBAL
    if instruccion.alcance == ALCANCE_VAR.GLOBAL : 
        simbolo = globales.declarar(instruccion.id)

        if not instruccion.exp is None :
            value = ejecutar_logica(instruccion.exp, locales, globales_inner)
            simbolo.valor = value
            globales.actualizar(simbolo)
            globales_inner.declarar(simbolo.id)
    # VARIBLE LOCAL
    elif instruccion.alcance == ALCANCE_VAR.LOCAL : 
        simbolo = locales.declarar(instruccion.id)

        if not instruccion.exp is None :
            value = ejecutar_logica(instruccion.exp, locales, globales_inner)
            simbolo.valor = value
            locales.actualizar(simbolo)
    # VARIABLE EMPTY
    else :
        simbolo = globales.obtener(instruccion.id)

        if simbolo is None :
            simbolo = locales.declarar(instruccion.id)

            if not instruccion.exp is None :
                value = ejecutar_logica(instruccion.exp, locales, globales_inner)
                simbolo.valor = value
                locales.actualizar(simbolo)
        else :
            if not instruccion.exp is None :
                value = ejecutar_logica(instruccion.exp, locales, globales_inner)
                simbolo.valor = value
                globales.actualizar(simbolo)
                globales_inner.declarar(simbolo.id)
        
# ========== ==========> CONDICIONAL

def ejecutar_if(instruccion: If, locales: TS.TablaSimbolo, globales_inner: TS.TablaSimbolo) :
    global errores
    cond = ejecutar_logica(instruccion.condicion, locales, globales_inner)
    if isinstance(cond, bool) :
        if cond :
            # ts_local = TS.TablaSimbolo(locales.simbolos)
            return ejecutar_instrucciones(instruccion.instrucciones, locales, globales_inner)
    else :
        print('Error semántico: En if. Se esperaba un tipo bool en la condición')
        errores.append('Error semántico', 'La condición del if esperaba un tipo ::Bool')

def ejecutar_if_else(instruccion: IfElse, locales: TS.TablaSimbolo, globales_inner: TS.TablaSimbolo) :
    global errores
    cond = ejecutar_logica(instruccion.condicion, locales, globales_inner)
    # ts_local = TS.TablaSimbolo(locales.simbolos)
    if isinstance(cond, bool) :
        if cond :
            return ejecutar_instrucciones(instruccion.instrucciones_v, locales, globales_inner)
        else :
            return ejecutar_instrucciones(instruccion.instrucciones_f, locales, globales_inner)
    else: 
        print('Error semántico: En if else. Se esperaba un tipo bool en la condición')
        errores.append('Error semántico', 'La condición del if esperaba un tipo ::Bool')

# ========== ==========> LOOP

def ejecutar_mientras(instruccion: Mientras, locales: TS.TablaSimbolo, globales_inner: TS.TablaSimbolo) :
    global errores
    cond = ejecutar_logica(instruccion.condicion, locales, globales_inner)
    if isinstance(cond, bool) :
        while cond :
            # ts_local = TS.TablaSimbolo(locales.simbolos)
            ejecutar_instrucciones(instruccion.instrucciones, locales, globales_inner)
            cond = ejecutar_logica(instruccion.condicion, locales, globales_inner)
    else :
        print('Error semántico: En while. Se esperaba un tipo bool en la condición')
        errores.append(Error('Error semántico', 'La condición del while esperaba tipo ::Bool'))

def ejecutar_for(instruccion: For, locales: TS.TablaSimbolo, globales_inner: TS.TablaSimbolo) :
    simbolo = globales_inner.obtener(instruccion.inicio)
    if simbolo is None :
        simbolo = locales.declarar(instruccion.inicio)
        if isinstance(instruccion.lista, str) : 
            lista = list(instruccion.lista)
            for i in lista :
                simbolo.valor = i
                locales.actualizar(simbolo)
                ejecutar_instrucciones(instruccion.instrucciones, locales, globales_inner)
    else: 
        if isinstance(instruccion.lista, str) : 
            lista = list(instruccion.lista)
            for i in lista :
                simbolo.valor = i
                globales_inner.actualizar(simbolo)
                ejecutar_instrucciones(instruccion.instrucciones, locales, globales_inner)

def ejecutar_funcion(instruccion: Funcion, locales: TS.TablaSimbolo, globales_inner: TS.TablaSimbolo) :
    pass
# ========== ==========> LOGICA

def ejecutar_logica(expresion, locales: TS.TablaSimbolo, globales_inner: TS.TablaSimbolo) :
    global errores
    if isinstance(expresion, LogicaBinaria) : 
        exp1 = ejecutar_logica(expresion.exp1, locales, globales_inner)
        exp2 = ejecutar_logica(expresion.exp2, locales, globales_inner)
        if not isinstance(exp1, bool) and not isinstance(exp2, bool) :
            print('Error semántico, En expresion lógica, se esperaban instancias de bool')
            errores.append('Error semántico', 'Se esperaba comparar un tipo ::Bool en la condición lógica')
            return None

        if expresion.operador == OP_LOGICA.AND : return exp1 and exp2
        if expresion.operador == OP_LOGICA.OR : return exp1 or exp2
    elif isinstance(expresion, Negado) : 
        exp1 = ejecutar_logica(expresion.exp1, locales, globales_inner)
        if not isinstance(exp1, bool) :
            print('Error semántico, En not, se esperaba instancia de bool')
            errores.append('Error semántico', 'Se esperaba comparar un tipo ::Bool en la condición lógica')
            return None
        
        return not exp1
    elif isinstance(expresion, ExpresionRelacional) : return ejecutar_relacional(expresion, locales, globales_inner)
    elif isinstance(expresion, ExpresionAritmetica) : return ejecutar_aritmetica(expresion, locales, globales_inner)
    elif isinstance(expresion, FuncionNativa) :
        return ejecutar_funcion_nativa(expresion, locales, globales_inner)

# ========== ==========> RELACIONAL    

def ejecutar_relacional(expresion, locales: TS.TablaSimbolo, globales_inner: TS.TablaSimbolo) :
    global errores
    if isinstance(expresion, ExpresionAritmetica) : return ejecutar_aritmetica(expresion, locales, globales_inner)
    elif isinstance(expresion, FuncionNativa) :
        return ejecutar_funcion_nativa(expresion, locales, globales_inner)
    
    exp1 = ejecutar_relacional(expresion.exp1, locales, globales_inner)
    exp2 = ejecutar_relacional(expresion.exp2, locales, globales_inner)

    if isinstance(exp1, str) and isinstance(exp2, str) : 
        if expresion.operador == OP_RELACIONAL.MENOR : return exp1 < exp2
        elif expresion.operador == OP_RELACIONAL.MENOR_IGUAL : return exp1 <= exp2
        elif expresion.operador == OP_RELACIONAL.MAYOR : return exp1 > exp2
        elif expresion.operador == OP_RELACIONAL.MAYOR_IGUAL : return exp1 >= exp2
        elif expresion.operador == OP_RELACIONAL.IGUAL : return exp1 == exp2
        elif expresion.operador == OP_RELACIONAL.DIFERENTE : return exp1 != exp2
    elif isinstance(exp1, str) or isinstance(exp2, str) :
        print('Error semántico: En operación relacional, se esperaba comparar string y string')
        errores.append(Error('Error semántico', 'Se esperaba comparar ::String con ::String'))
        return None
    else :
        if expresion.operador == OP_RELACIONAL.MENOR : return exp1 < exp2
        elif expresion.operador == OP_RELACIONAL.MENOR_IGUAL : return exp1 <= exp2
        elif expresion.operador == OP_RELACIONAL.MAYOR : return exp1 > exp2
        elif expresion.operador == OP_RELACIONAL.MAYOR_IGUAL : return exp1 >= exp2
        elif expresion.operador == OP_RELACIONAL.IGUAL : return exp1 == exp2
        elif expresion.operador == OP_RELACIONAL.DIFERENTE : return exp1 != exp2

# ========== ==========> ARITMÉTICA

def ejecutar_aritmetica(expresion, locales: TS.TablaSimbolo, globales_inner: TS.TablaSimbolo) :
    global errores
    if isinstance(expresion, AritmeticaBinaria) :
        exp1 = ejecutar_aritmetica(expresion.exp1, locales, globales_inner)
        exp2 = ejecutar_aritmetica(expresion.exp2, locales, globales_inner)
        
        if expresion.operador == OP_ARITMETICA.MAS :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                return exp1 + exp2
            if (isinstance(exp1, str) or isinstance(exp2, str)) :
                if isinstance(exp1, str) and len(exp1) == 1 : exp1 = int(exp1)
                if isinstance(exp2, str) and len(exp2) == 1 : exp2 = int(exp2)
                return exp1 + exp2
            
            print('Error semántico: En +, se esperaba Int64, Float64, Char o Bool')
            errores.append(Error('Error semántico', 'Se esperaba sumar tipos ::Int64, ::Float64, ::Char o ::Bool'))
            return None
        elif expresion.operador == OP_ARITMETICA.MENOS :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                return exp1 - exp2
            
            print('Error semántico: En -, se esperaba Int64, Float64 o Bool')
            errores.append(Error('Error semántico', 'Se esperaba restar tipos ::Int64, ::Float64 o ::Bool'))
            return None
        elif expresion.operador == OP_ARITMETICA.POR :
            if isinstance(exp1, bool) and isinstance(exp2, bool) : return bool(exp1 * exp2)
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                if isinstance(exp1, bool) and isinstance(exp2, bool) :
                    return bool(exp1 * exp2)
                return exp1 * exp2
            if isinstance(exp1, str) and isinstance(exp2, str) : return exp1 + exp2
            
            print('Error semántico: En *, se esperaba Int64, Float64 o Bool')
            errores.append(Error('Error semántico', 'Se esperaba sumar tipos ::Int64, ::Float64 o Bool'))
            return None
        elif expresion.operador == OP_ARITMETICA.DIVIDIDO :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                return exp1 / exp2
            
            print('Error semántico: En /, se esperaba Int64, Float64 o Bool')
            errores.append(Error('Error semántico', 'Se esperaba dividir tipos ::Int64, ::Float64 o ::Bool'))
            return None
        elif expresion.operador == OP_ARITMETICA.MODULO :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                return exp1 % exp2
            
            print('Error semántico: En %, se esperaba Int64, Float64 o Bool')
            errores.append(Error('Error semántico', 'Se esperaba obtener el módulo de los tipos ::Int64, ::Float64 o ::Bool'))
            return None
        elif expresion.operador == OP_ARITMETICA.POTENCIA :
            if (isinstance(exp1, int) or isinstance(exp1, float) or isinstance(exp1, bool)) and (isinstance(exp2, int) or isinstance(exp2, float) or isinstance(exp2, bool)) :
                if isinstance(exp1, bool) : return bool(exp1 ** exp2)
                return exp1 ** exp2
            elif isinstance(exp1, str) and (isinstance(exp2, int) or isinstance(exp2, float)) :
                return exp1 * exp2
            
            print('Error semántico: En ^, se esperaba Int64, Float64, Bool o string ^ Int64')
            errores.append(Error('Error semántico', 'Se esperaba obtener la potencia de tipos ::Int64, ::Float64 o ::Bool, ::String ^ ::Int64'))
            return None
        elif expresion.operador == OP_ARITMETICA.RANGO : 
            if isinstance(exp1, int) and isinstance(exp2, int) :
                if exp2 > exp1 :
                    return range(exp1, exp2 + 1) # RETURN TYPE RANGE
                else :
                    print('Error semántico: En rango, El segundo término debe ser mayor al primero')
                    errores.append('Error semántico', 'El segundo término debe ser mayor al primero')
            else :
                print('Error semántico: En rango, se esperaban rangos de ::Int64')
                errores.append('Error semántico', 'Se esperaban tipo ::Int64')
                return None
    elif isinstance(expresion, Negativo) :
        exp1 = ejecutar_aritmetica(expresion.exp1, locales, globales_inner)
        if isinstance(exp1, int) or isinstance(exp1, float) :
            return exp1 * -1
        print('Error semántico: En negativo, se esperaba Int64 o Float64')
        errores.append(Error('Error semántico', 'Se esperaba los tipos ::Int64 o ::Float64'))
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
        # Buscar entre globales declarados ámbito
        simbolo = globales_inner.obtener(expresion.id)
        if not simbolo is None :
            return simbolo.valor
        else :
            # Buscar en locales declarados dentro del ámbito
            return locales.obtener(expresion.id).valor
    elif isinstance(expresion, FuncionNativa) :
        return ejecutar_funcion_nativa(expresion, locales, globales_inner)

# ========== ==========> LLAMADA A FUNCIONES

def ejecutar_funcion_nativa(funcionNativa: FuncionNativa, locales: TS.TablaSimbolo, globales_inner: TS.TablaSimbolo) :
    if isinstance(funcionNativa, CallFuncion) : return

    global errores
    exp = ejecutar_logica(funcionNativa.exp, locales, globales_inner)
    if isinstance(funcionNativa, NativaParse) :
        if isinstance(exp, str) :
            if exp.isnumeric() or exp.isdecimal() :
                if funcionNativa.tipo == DATA_TYPE.NUMERO : return int(exp)
                elif funcionNativa.tipo == DATA_TYPE.DECIMAL : return float(exp)
                else : 
                    print('Error semántico: En parse, se esperaba convertir a Int64 o Float64')
                    errores.append(Error('Error semántico', 'Se esperaba convertir a ::Int64 a ::Float64'))
                    return None
            else :
                print('Error semántico: En parse, la cadena no se puede convertir a Int64 o Float64')
                errores.append(Error('Error semántico', 'Se esperaba convertir un tipo ::Int64 o ::Float64'))
                return None
        else :
            print('Error semántico: En parse, se esperaba convertir de string')
            errores.append(Error('Error semántico', 'Se esperaba convertir un tipo ::String'))
            return None
    elif isinstance(funcionNativa, NativaTrunc) :
        if isinstance(exp, float) :
            return int(exp)
        elif isinstance(exp, int) :
            return exp
        else :
            print('Error semántico: En trunc, se esperaba un tipo Float64')
            errores.append(Error('Error semántico', 'Se esperaba convertir un tipo ::Float64'))
            return None
    elif isinstance(funcionNativa, NativaFloat) :
        if isinstance(exp, int) :
            return float(exp)
        elif isinstance(exp, float) :
            return exp
        else :
            print('Error semántico: En float, se esperaba un tipo Int64')
            errores.append(Error('Error semántico', 'Se esperaba un tipo ::Int64'))
            return None
    elif isinstance(funcionNativa, NativaString) :
        if isinstance(exp, int) or isinstance(exp, float) :
            return str(exp)
        else :
            print('Error semántico: En string, se esperaba un tipo Int64 o Float64')
            errores.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(funcionNativa, NativaTypeof) :
        if isinstance(exp, int) : return 'Int64'
        elif isinstance(exp, float) : return 'Float64'
        elif isinstance(exp, str) : return 'String'
        elif isinstance(exp, bool) : return 'Bool'
        elif isinstance(exp, str) : return 'Char'
        else : return None
    elif isinstance(funcionNativa, NativaSin) :
        if isinstance(exp, int) or isinstance(exp, float) :
            return math.sin(exp)
        else :
            print('Error semántico: Sin solo acepta Int64 o Float64')
            errores.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(funcionNativa, NativaCos) :
        if isinstance(exp, int) or isinstance(exp, float) :
            return math.cos(exp)
        else :
            print('Error semántico: Cos solo acepta Int64 o Float64')
            errores.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(funcionNativa, NativaTan) :
        if isinstance(exp, int) or isinstance(exp, float) :
            return math.tan(exp)
        else :
            print('Error semántico: Tan solo acepta Int64 o Float64')
            errores.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(funcionNativa, NativaLog10) :
        if isinstance(exp, int) or isinstance(exp, float) :
            return math.log10(exp)
        else :
            print('Error semántico: Log10 solo acepta Int64 o Float64')
            errores.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(funcionNativa, NativaSqrt) :
        if isinstance(exp, int) or isinstance(exp, float) :
            return math.sqrt(exp)
        else :
            print('Error semántico: Sqrt solo acepta Int64 o Float64')
            errores.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(funcionNativa, NativaLength) :
        if isinstance(exp, str) :
            return len(exp)
        else :
            print('Error semántico: length solo acepta Int64 o Float64')
            errores.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(funcionNativa, NativaUppercase) :
        if isinstance(exp, str) :
            return exp.upper()
        else :
            print('Error semántico: uppercase solo acepta Int64 o Float64')
            errores.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None
    elif isinstance(funcionNativa, NativaLowercase) :
        if isinstance(exp, str) :
            return exp.lower()
        else :
            print('Error semántico: lowercase solo acepta Int64 o Float64')
            errores.append(Error('Error semántico', 'Se esperaba un tipo ::Int64 o ::Float64'))
            return None

# ========== ==========> EJECUTAR INSTRUCCIONES

def ejecutar_instrucciones(instrucciones: Instruccion, locales: TS.TablaSimbolo, globales_inner: TS.TablaSimbolo) :
    global errores
    for instruccion in instrucciones :
        if isinstance(instruccion, Print) : 
            ejecutar_print(instruccion, locales, globales_inner)
        elif isinstance(instruccion, Println) : 
            ejecutar_println(instruccion, locales, globales_inner)
        elif isinstance(instruccion, Definicion) : ejecutar_definicion(instruccion, locales, globales_inner)
        elif isinstance(instruccion, Mientras) : 
            ejecutar_mientras(instruccion, locales, globales_inner)
        elif isinstance(instruccion, For) : 
            ejecutar_for(instruccion, locales, globales_inner)
        elif isinstance(instruccion, If) : 
            ejecutar_if(instruccion, locales, globales_inner)
        elif isinstance(instruccion, IfElse) : 
            ejecutar_if_else(instruccion, locales, globales_inner)
        else : 
            print('Error semantico: Instrucción no válida')
            errores.append(Error('Error semántico', 'Instrucción no reconocida'))
    return response, errores