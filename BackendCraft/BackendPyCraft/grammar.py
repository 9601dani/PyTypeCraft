import re
import ply.lex as lex
from src.ObjectError.ExceptionPyType import ExceptionPyType

# here start grammar
# --------------------------------------------------------------
# 04-06-2023: Created by Daniel Morales
# proyecto 1 - compiladores 2 usac 2023
# --------------------------------------------------------------
# Definimos las palabras reservadas de nuestro lenguaje
global_arr = []

reservadas = {
    # Conditions
    'if': 'IF',
    'else': 'ELSE',
    # Loops
    'for': 'FOR',
    'of': 'OF',
    'while': 'WHILE',
    'continue': 'CONTINUE',
    'break': 'BREAK',
    # Natives Functions
    # '.toString' : 'TOSTRING',
    # '.tofixed' : 'TOFIXED',
    # '.toExponential' : 'TOEXPONENTIAL',
    # '.toLowercase' : 'TOLOWERCASE',
    # '.toUppercase' : 'TOUPPERCASE',
    # '.split' : 'SPLIT',
    # '.concat' : 'CONCAT',
    'toString': 'TOSTRING',
    'toFixed': 'TOFIXED',
    'toExponential': 'TOEXPONENTIAL',
    'toLowerCase': 'TOLOWERCASE',
    'toUpperCase': 'TOUPPERCASE',
    'split': 'SPLIT',
    'concat': 'CONCAT',
    'length': 'LENGTH',
    'push': 'PUSH',
    # Print Console
    'console': 'CONSOLE',
    'log': 'LOG',
    # Declaration
    'let': 'LET',
    # Types Declaration
    'string': 'STRING',
    'boolean': 'BOOLEAN',
    'number': 'NUMBER',
    'any': 'ANY',
    'null': 'NULL',
    # Funtion
    'function': 'FUNCTION',
    'return': 'RETURN',
    # Struct
    'interface': 'INTERFACE',
    'true': 'TRUE',
    'false': 'FALSE',
}
tokens = [
             # Operadores Booleanos
             'TRIPLE_IGUAL',
             'MENOR_IGUAL_QUE',
             'MAYOR_IGUAL_QUE',
             'MENOR_QUE',
             'MAYOR_QUE',
             'DISTINTO_QUE',
             'NOT',
             'AND',
             'OR',
             # Signos de Agrupacion
             'L_PAREN',
             'R_PAREN',
             'L_LLAVE',
             'R_LLAVE',
             'R_CORCHETE',
             'L_CORCHETE',
             # Operadores Aritmeticos
             'MAS',
             'MENOS',
             'MOD',
             'DIVIDE',
             'TIMES',
             'POTENCIA',
             'IGUAL',
             # Signos de Puntuacion
             'PUNTO',
             'COLON',
             'SEMI_COLON',
             'COMA',
             'CADENA',
             'LITERAL',
             'ENTERO',
             'DECIMAL',
         ] + list(reservadas.values())

# Tokens
t_TRIPLE_IGUAL = r'==='
t_MENOR_IGUAL_QUE = r'<='
t_MAYOR_IGUAL_QUE = r'>='
t_MENOR_QUE = r'<'
t_MAYOR_QUE = r'>'
t_DISTINTO_QUE = r'!=='
t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'
t_L_PAREN = r'\('
t_R_PAREN = r'\)'
t_L_LLAVE = r'\{'
t_R_LLAVE = r'\}'
t_R_CORCHETE = r'\]'
t_L_CORCHETE = r'\['
t_MAS = r'\+'
t_MENOS = r'-'
t_MOD = r'%'
t_DIVIDE = r'/'
t_TIMES = r'\*'
t_POTENCIA = r'\^'
t_IGUAL = r'='
t_PUNTO = r'\.'
t_COLON = r':'
t_SEMI_COLON = r';'
t_COMA = r','


# Expresiones Regulares de las cadenas con "" o ''
def t_CADENA(t):
    r'\"(\\\'|\\"|\\\\|\\n|\\t|[^\'\\\"])*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas

    print(str(t.value))
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\r', '\r')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace("\\'", '\'')
    t.value = t.value.replace('\\\\', '\\')
    return t


# Expersion Regular para decimal
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        global_arr.append(ExceptionPyType(str(t.value) + " DEMASIADO GRANDE", t.lexer.lineno, -1))
        t.value = 0
    return t


# Expresion Regular para Entero
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        global_arr.append(ExceptionPyType(str(t.value) + " DEMASIADO GRANDE", t.lexer.lineno, -1))
        t.value = 0
    return t


# Expresion Regular para Booleano


# Expresion Regular para literales
def t_LITERAL(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'LITERAL')
    return t


# Expresion Regular para comentarios multilinea
def t_COMENTARIO_MULTILINEA(t):
    r'\/\*(.|\n)*?\*\/'
    t.lexer.lineno += t.value.count('\n')


# Expresion Regular para comentarios simple
def t_COMENTARIO_SIMPLE(t):
    r'\/\/.*'
    t.lexer.lineno += 1


# ignorar espacios
t_ignore = " \t"


# Manejo de Linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Manejo de columna
def find_column(inp, token):
    line_start = str(inp).rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


def t_error(t):
    # errores.append(Excepcion("Lexico","Error léxico." + t.value[0] , t.lexer.lineno, find_column(input, t)))
    global_arr.append(
        ExceptionPyType(str(t.value) + " NO FORMA PARTE DEL LENGUAJE", t.lexer.lineno, find_column(input, t)))

    t.lexer.skip(1)


# Se construye el analizador lexico
import ply.lex as lex

lexer = lex.lex(reflags=re.IGNORECASE)

##GRAMATICA "CUP"
import os
from src.models.ConsoleLog import ConsoleLog
from src.models.Instruction import Instruction
from src.models.OperationType import OperationType
from src.models.VariableType import VariableType
from src.models.BinaryOperation import BinaryOperation
from src.models.UnaryOperation import UnaryOperation
from src.models.Declaration import Declaration
from src.models.Assignment import Assignment
from src.models.OnlyAssignment import OnlyAssignment
from src.models.IfState import IfState
from src.models.ElseState import ElseState
from src.models.WhileState import WhileState
from src.models.ForEachState import ForEachState
from src.models.ForState import ForState
from src.models.NativeFunType import NativeFunType
from src.models.FunctionState import FunctionState
from src.models.Parameter import Parameter
from src.models.InterAttributeAssign import InterAttributeAssign
from src.models.InterfaceState import InterfaceState
from src.models.Break import Break
from src.models.Return import Return
from src.models.Continue import Continue
from src.models.CallFunction import CallFunction
from src.models.NativeFunction import NativeFunction
from src.models.Value import Value
from src.models.ValueType import ValueType
from src.visitor.Debugger import Debugger
from src.visitor.Runner import Runner
from src.visitor.CstDrawer import CstDrawer
from src.symbolTable.SymbolTable import SymbolTable
from src.models.InterfaceAssign import InterfaceAssign
from src.models.CallAttribute import CallAttribute
from src.models.ArrayState import ArrayState
from src.models.CallArray import CallArray
from src.models.ArrayAssign import ArrayAssign
from src.visitor.C3DGenerator import C3DGenerator
from src.symbolTable.TableC3d import TableC3d
import sys
sys.setrecursionlimit(10000000)


def return_operation_type(operation_type):
    if (operation_type == "||"):
        return OperationType.OR
    elif (operation_type == "&&"):
        return OperationType.AND
    elif (operation_type == "!"):
        return OperationType.NOT
    elif (operation_type == ">"):
        return OperationType.MAYOR_QUE
    elif (operation_type == "<"):
        return OperationType.MENOR_QUE
    elif (operation_type == ">="):
        return OperationType.MAYOR_IGUAL_QUE
    elif (operation_type == "<="):
        return OperationType.MENOR_IGUAL_QUE
    elif (operation_type == "==="):
        return OperationType.TRIPLE_IGUAL
    elif (operation_type == "!=="):
        return OperationType.DISTINTO_QUE
    elif (operation_type == "+"):
        return OperationType.MAS
    elif (operation_type == "-"):
        return OperationType.MENOS
    elif (operation_type == "*"):
        return OperationType.TIMES
    elif (operation_type == "/"):
        return OperationType.DIVIDE
    elif (operation_type == "%"):
        return OperationType.MOD
    elif (operation_type == "^"):
        return OperationType.POTENCIA


######## FUNCIÓN UTILIZADA PARA RETORNAR EL TIPO DE FUNCIÓN NATIVA USADA EN LA PRODUCCIÓN 'nativeFun'
def return_native_fun_type(native_type):
    if (native_type == "toString"):
        return NativeFunType.TOSTRING
    elif (native_type == "toFixed"):
        return NativeFunType.TOFIXED
    elif (native_type == "toExponential"):
        return NativeFunType.TOEXPONENTIAL
    elif (native_type == "toLowerCase"):
        return NativeFunType.TOLOWERCASE
    elif (native_type == "toUpperCase"):
        return NativeFunType.TOUPPERCASE
    elif (native_type == "split"):
        return NativeFunType.SPLIT
    elif (native_type == "concat"):
        return NativeFunType.CONCAT
    elif (native_type == "length"):
        return NativeFunType.LENGTH
    elif (native_type == "push"):
        return NativeFunType.PUSH


def p_init(t):
    'init            : instrucciones'
    t[0] = t[1]


def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    if (t[2] != ""):
        t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion'
    if (t[1] == ""):
        t[0] = []
    else:
        t[0] = [t[1]]


def p_instruccion(t):
    '''instruccion      : console_pro sc
                        | declaration_instruction sc
                        | assig_pro sc
                        | interface_assign_pro sc
                        | array_assign_pro sc
                        | if_pro sc
                        | while_pro sc
                        | for_pro sc
                        | for_each_pro sc
                        | interface_pro sc
                        | continue_pro sc
                        | break_pro sc
                        | return_pro sc
                        | function_pro sc
                        | call_function_pro sc
                        | a sc
                        | sumadores sc'''
    t[0] = t[1]


############################################## PRODUCCION ';' ##############################################
def p_semi_colon(t):
    '''sc   : SEMI_COLON
            |'''


############################################## DECLARACION DE FUNCIÓN ##############################################
def p_instruccion_function(t):
    '''function_pro : FUNCTION LITERAL L_PAREN parameters_pro R_PAREN L_LLAVE instrucciones R_LLAVE'''
    t[0] = FunctionState(t.lineno(1), find_column(input, t.slice[1]), t[2], False, t[4], t[7], None)


def p_instruccion_function2(t):
    '''function_pro : FUNCTION LITERAL L_PAREN R_PAREN L_LLAVE instrucciones R_LLAVE'''
    t[0] = FunctionState(t.lineno(1), find_column(input, t.slice[1]), t[2], False, None, t[6], None)


def p_instruccion_function3(t):
    '''function_pro : FUNCTION LITERAL L_PAREN parameters_pro R_PAREN COLON type L_LLAVE instrucciones R_LLAVE
                    | FUNCTION LITERAL L_PAREN parameters_pro R_PAREN COLON LITERAL L_LLAVE instrucciones R_LLAVE'''
    t[0] = FunctionState(t.lineno(1), find_column(input, t.slice[1]), t[2], False, t[4], t[9], t[7], )


def p_instruccion_function4(t):
    '''function_pro : FUNCTION LITERAL L_PAREN R_PAREN COLON type L_LLAVE instrucciones R_LLAVE
                    | FUNCTION LITERAL L_PAREN R_PAREN COLON LITERAL L_LLAVE instrucciones R_LLAVE'''
    t[0] = FunctionState(t.lineno(1), find_column(input, t.slice[1]), t[2], False, None, t[8], t[6])


############################################## LLAMADA DE FUNCIÓN ##############################################
def p_instruccion_call_function(t):
    '''call_function_pro    : LITERAL L_PAREN values R_PAREN'''
    t[0] = CallFunction(t.lineno(1), find_column(input, t.slice[1]), t[1], t[3])


def p_instruccion_call_function2(t):
    '''call_function_pro    : LITERAL L_PAREN R_PAREN'''
    t[0] = CallFunction(t.lineno(1), find_column(input, t.slice[1]), t[1], [])


def p_instruccion_call_function3(t):
    '''call_function_pro    : TOSTRING L_PAREN values R_PAREN'''
    t[0] = CallFunction(t.lineno(1), find_column(input, t.slice[1]), t[1], t[3])


############################################## VALUES ##############################################
### ESTA PRODUCCIÓN ES LA UTILIZADA PARA LOS PARÁMETROS DE LA FUNCIÓN Y DE LOS ARREGLOS
### suma ( 3, 4, 3 ) ó let a = [ 1, 4, 3 ]
###       _^ _^ _^              _^ _^ _^
###################################################################################################
def p_instruccion_values(t):
    '''values   : values COMA a'''
    t[0] = t[1]
    t[0].append(t[3])


def p_instruccion_values2(t):
    '''values   : a'''
    t[0] = []
    t[0].append(t[1])


############################################## PARAMETROS ##############################################

def p_instruccion_parameters(t):
    '''parameters_pro   : parameters_pro COMA parameter_pro'''
    t[0] = t[1]
    t[0].append(t[3])
    # print("---- ASIGNANDO  PARAMETRO ----- "+t[3].id)


def p_instruccion_parameters2(t):
    '''parameters_pro   : parameter_pro'''
    t[0] = []
    t[0].append(t[1])
    # print("---- ASIGNANDO  PARAMETRO ----- "+t[1].id)


def p_instruccion_parameter(t):
    '''parameter_pro    : LITERAL COLON type'''
    t[0] = Parameter(t.lineno(1), find_column(input, t.slice[1]), t[1], t[3], False)


def p_instruccion_parameter2(t):
    '''parameter_pro    : LITERAL'''
    t[0] = Parameter(t.lineno(1), find_column(input, t.slice[1]), t[1], None, True)


############################################## CONTINUE / BREAK / RETURN ##############################################
def p_instruccion_continue(t):
    '''continue_pro : CONTINUE'''
    t[0] = Continue(t.lineno(1), find_column(input, t.slice[1]))


def p_instruccion_break(t):
    '''break_pro : BREAK'''
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))


def p_instruccion_return(t):
    '''return_pro : RETURN'''
    t[0] = Return(t.lineno(1), find_column(input, t.slice[1]), None)


def p_instruccion_return2(t):
    '''return_pro : RETURN a'''
    t[0] = Return(t.lineno(1), find_column(input, t.slice[1]), t[2])


############################################## DECLARACION DE INTERFACE ##############################################

def p_instruccion_declarationInterface(t):
    '''interface_pro    : INTERFACE LITERAL L_LLAVE interface_atributos R_LLAVE'''
    t[0] = InterfaceState(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4])


def p_instruccion_interfaceAtributos(t):
    '''interface_atributos  : interface_atributos interface_atributo sc'''
    t[0] = t[1]
    t[0].append(t[2])


def p_instruccion_interfaceAtributos2(t):
    '''interface_atributos  : '''
    t[0] = []


def p_intruccion_interfaceAtributo(t):
    '''interface_atributo   : LITERAL COLON type'''
    t[0] = Assignment(t.lineno(1), find_column(input, t.slice[1]), t[1], t[3], None, False)


def p_instruccion_interfaceAtributo2(t):
    '''interface_atributo   : LITERAL'''
    t[0] = Assignment(t.lineno(1), find_column(input, t.slice[1]), t[1], None, None, True)


############################################## ASIGNACIÓN A ATRIBUTOS DE INTERFAZ ##############################################

def p_instruccion_interface_assign_pro(t):
    '''interface_assign_pro : i PUNTO LITERAL IGUAL a'''
    attrVal = CallAttribute(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3])
    t[0] = InterAttributeAssign(t.lineno(1), find_column(input, t.slice[2]), attrVal, t[5])


############################################## DECLARACION DE VARIABLE ##############################################
def p_instruccion_declarationInstruction(t):
    '''declaration_instruction      : LET declaracion_list'''
    t[0] = Declaration(t.lineno(1), find_column(input, t.slice[1]), "LET", t[2])
    # print("###### IMPRIMIENDO LISTA ######")
    # print(t[2])


def p_instruccion_declaracion_list(t):
    '''declaracion_list      : declaracion_list COMA assignacion_instruction'''
    t[0] = t[1]
    t[0].append(t[3])
    # print("####ASIGNACION EN LISTA####")
    # print(t[3])
    # print("#####IMPRIMIENDO LISTA EN LISTA########")
    # print(t[0])


def p_instruccion_declaracion_list2(t):
    '''declaracion_list      : assignacion_instruction'''
    t[0] = []
    t[0].append(t[1])
    # print("####ASIGNACION####")
    # print(t[1])


def p_instruccion_assignacion_instruction(t):
    '''assignacion_instruction      : LITERAL COLON type IGUAL a'''
    t[0] = Assignment(t.lineno(1), find_column(input, t.slice[1]), t[1], t[3], t[5], False)


def p_instruccion_assingnacion_instruction2(t):
    '''assignacion_instruction      : LITERAL COLON type'''
    t[0] = Assignment(t.lineno(1), find_column(input, t.slice[1]), t[1], t[3], None, False)


def p_instruccion_assignacion_instruction3(t):
    '''assignacion_instruction      : LITERAL IGUAL a'''
    t[0] = Assignment(t.lineno(1), find_column(input, t.slice[1]), t[1], None, t[3], True)


def p_instruccion_assignacion_instruction4(t):
    '''assignacion_instruction      : LITERAL'''
    t[0] = Assignment(t.lineno(1), find_column(input, t.slice[1]), t[1], None, None, True)
    # print("####ASIGNACION####")
    # print(t[0])


def p_instruccion_type(t):
    '''type      : NUMBER
                 | STRING
                 | BOOLEAN
                 | ANY
                 | LITERAL
                 | NULL'''
    t[0] = t[1]


############################################## ASIGNACION DE VARIABLE ##############################################
def p_instruccion_assig_pro(t):
    '''assig_pro      : LITERAL IGUAL a'''
    t[0] = OnlyAssignment(t.lineno(1), find_column(input, t.slice[1]), t[1], VariableType().buscar_type("definirla"),
                          t[3])


############################################## IF ##############################################
def p_instruccion_if_pro(t):
    '''if_pro      : IF L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE else_pro'''
    t[0] = IfState(t.lineno(1), find_column(input, t.slice[1]), t[3], t[6], t[8])


# CONTENPLAR LA IDEA QUE instrucciones PUEDE VENIR VACIO
############################################## ELSE ##############################################
def p_instruccion_else_pro(t):
    '''else_pro      : ELSE IF L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE else_pro'''
    t[0] = IfState(t.lineno(1), find_column(input, t.slice[1]), t[4], t[7], t[9])


def p_instruccion_else_pro2(t):
    '''else_pro      : ELSE L_LLAVE instrucciones R_LLAVE'''
    t[0] = ElseState(t.lineno(1), find_column(input, t.slice[1]), t[3])


def p_instruccion_else_pro3(t):
    '''else_pro      : '''
    t[0] = None


############################################## WHILE ##############################################
def p_instruccion_while_pro(t):
    '''while_pro      : WHILE L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE'''
    t[0] = WhileState(t.lineno(1), find_column(input, t.slice[1]), t[3], t[6])


############################################## FOR ##############################################
def p_instruccion_for_pro(t):
    '''for_pro      : FOR L_PAREN declaration_instruction SEMI_COLON a SEMI_COLON inDec_pro R_PAREN L_LLAVE instrucciones R_LLAVE
                    | FOR L_PAREN assig_pro SEMI_COLON a SEMI_COLON inDec_pro R_PAREN L_LLAVE instrucciones R_LLAVE'''

    t[0] = ForState(t.lineno(1), find_column(input, t.slice[1]), t[3], t[5], t[7], t[10])


############################################## INCREMENTO DECREMENTO PRODUCCIÓN PARA FOR ##############################################
def p_instruccion_in_dec_pro(t):
    '''inDec_pro   : assig_pro
                    | sumadores'''
    t[0] = t[1]


############################################## FOR EACH ##############################################

def p_instruccion_for_each_pro(t):
    '''for_each_pro : FOR L_PAREN LET LITERAL OF a R_PAREN L_LLAVE instrucciones R_LLAVE'''
    t[0] = ForEachState(t.lineno(1), find_column(input, t.slice[1]), t[4], t[6], t[9])


############################################## CONSOLE.LOG ##############################################
def p_instruccion_console(t):
    '''console_pro      : CONSOLE PUNTO LOG L_PAREN expresion R_PAREN'''
    t[0] = ConsoleLog(t.lineno(1), find_column(input, t.slice[1]), t[5])
    # print(f"""si encontre algo en la produccion console.log -> {t[5]} """)


def p_instruccion_expresion(t):
    '''expresion      : expresion COMA a'''
    t[0] = t[1]
    t[0].append(t[3])


def p_instruccion_expresion2(t):
    '''expresion      : a'''
    t[0] = []
    t[0].append(t[1])


def p_instruccion_expresion3(t):
    '''a      : a OR b'''
    t[0] = BinaryOperation(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3], OperationType.OR)


def p_instruccion_expresion4(t):
    '''a      : b'''
    t[0] = t[1]


def p_instruccion_expresion5(t):
    ''' b      : b AND c'''
    t[0] = BinaryOperation(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3], OperationType.AND)


def p_instruccion_expresion6(t):
    ''' b      : c'''
    t[0] = t[1]


def p_instruccion_expresion7(t):
    ''' c      : NOT d'''
    t[0] = UnaryOperation(t.lineno(1), find_column(input, t.slice[1]), t[2], OperationType.NOT)


def p_instruccion_expresion8(t):
    ''' c      : d '''
    t[0] = t[1]


def p_instruccion_expresion9(t):
    ''' d     : d DISTINTO_QUE e
                | d MENOR_QUE e
                | d MENOR_IGUAL_QUE e
                | d MAYOR_QUE e
                | d MAYOR_IGUAL_QUE e
                | d TRIPLE_IGUAL e '''
    t[0] = BinaryOperation(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3], return_operation_type(t[2]))


def p_instruccion_expresion10(t):
    ''' d     : e '''
    t[0] = t[1]


def p_instruccion_expresion11(t):
    ''' e     : e MAS f
                | e MENOS f '''
    t[0] = BinaryOperation(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3], return_operation_type(t[2]))


def p_instruccion_expresion12(t):
    ''' e     :  f '''
    t[0] = t[1]


def p_instruccion_expresion13(t):
    ''' f     : MENOS g
                | MAS g '''
    if t[1] == "-":
        t[0] = UnaryOperation(t.lineno(1), find_column(input, t.slice[1]), t[2], OperationType.NEGATIVE)
    elif t[1] == "+":
        t[0] = UnaryOperation(t.lineno(1), find_column(input, t.slice[1]), t[2], OperationType.POSITIVE)


def p_instruccion_expresion14(t):
    ''' f     : g '''
    t[0] = t[1]


def p_instruccion_expresion15(t):
    ''' g     : g TIMES h
                | g DIVIDE h
                | g MOD h'''
    t[0] = BinaryOperation(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3], return_operation_type(t[2]))


def p_instruccion_expresion16(t):
    ''' g     : h '''
    t[0] = t[1]


def p_instruccion_expresion17(t):
    '''h    : h POTENCIA i'''
    t[0] = BinaryOperation(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3], return_operation_type(t[2]))


def p_instruccion_expresion17_1(t):
    '''h    : i'''
    t[0] = t[1]


def p_instruccion_expresion18(t):
    ''' i     : ENTERO'''
    t[0] = Value(t.lineno(1), find_column(input, t.slice[1]), t[1], ValueType.ENTERO)


def p_instruccion_expresion19(t):
    ''' i     : DECIMAL'''
    t[0] = Value(t.lineno(1), find_column(input, t.slice[1]), t[1], ValueType.DECIMAL)


def p_instruccion_expresion20(t):
    ''' i     : CADENA'''
    t[0] = Value(t.lineno(1), find_column(input, t.slice[1]), t[1], ValueType.CADENA)


def p_instruccion_expresion21(t):
    ''' i     : LITERAL'''
    t[0] = Value(t.lineno(1), find_column(input, t.slice[1]), t[1], ValueType.LITERAL)


def p_instruccion_expresion22(t):
    ''' i     : TRUE
              | FALSE'''
    t[0] = Value(t.lineno(1), find_column(input, t.slice[1]), t[1], ValueType.BOOLEANO)


def p_instruccion_expresion23(t):
    ''' i     : call_function_pro
              | array_pro
              | interface_assi'''
    t[0] = t[1]


def p_instruccion_expresion24(t):
    ''' i     : L_PAREN a R_PAREN'''
    t[0] = t[2]


def p_instruccion_expresion25(t):
    '''i    : array_val_pro'''
    t[0] = t[1]


def p_instruccion_expresion26(t):
    '''i    : i PUNTO LITERAL'''
    t[0] = CallAttribute(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3])


def p_instruccion_expresion27(t):
    '''i    : i PUNTO nativeFun L_PAREN expresion R_PAREN
            | i PUNTO nativeFun L_PAREN R_PAREN'''
    # print("EVALUANDO NATIVAS")
    # print(t[3])
    if (t[5] == ")"):
        t[0] = NativeFunction(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3], [])
    else:
        t[0] = NativeFunction(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3], t[5])


def p_instruccion_array_val_pro(t):
    '''array_val_pro    : LITERAL dimensions'''
    t[0] = CallArray(t.lineno(1), find_column(input, t.slice[1]), t[1], t[2])


def p_instruccion_dimensions(t):
    '''dimensions   : dimensions L_CORCHETE a R_CORCHETE'''
    t[0] = t[1]
    t[0].append(t[3])


def p_instruccion_dimensions2(t):
    '''dimensions   : L_CORCHETE a R_CORCHETE'''
    t[0] = []
    t[0].append(t[2])


def p_instruccion_sumadores(t):
    ''' sumadores     : LITERAL MAS MAS
                          | LITERAL MENOS MENOS '''
    if (t[2] == "+"):
        t[0] = UnaryOperation(t.lineno(1), find_column(input, t.slice[2]),
                              Value(t.lineno(1), find_column(input, t.slice[1]), t[1], ValueType.LITERAL),
                              OperationType.INCREMENT)
    else:
        t[0] = UnaryOperation(t.lineno(1), find_column(input, t.slice[2]),
                              Value(t.lineno(1), find_column(input, t.slice[1]), t[1], ValueType.LITERAL),
                              OperationType.DECREMENT)


############################################## ASIGNAR INTERFACE ##############################################
def p_instruccion_interfaceAssi(t):
    '''interface_assi   : L_LLAVE atributos_assi R_LLAVE'''
    t[0] = InterfaceAssign(t.lineno(1), find_column(input, t.slice[1]), t[2])


############################################## ASIGNAR ATRIBUTOS INTERFACE ##############################################
def p_instruccion_inter_atributesAssi(t):
    '''atributos_assi   : atributos_assi COMA LITERAL COLON a'''
    t[0] = t[1]
    t[0].append(Assignment(t.lineno(1), find_column(input, t.slice[3]), t[3], None, t[5], True))


def p_instruccion_inter_atributesAssi2(t):
    '''atributos_assi   : LITERAL COLON a'''
    t[0] = []
    t[0].append(Assignment(t.lineno(1), find_column(input, t.slice[1]), t[1], None, t[3], True))


############################################## ASIGNACION DE ARREGLOS ##############################################
def p_instruccion_array_pro(t):
    '''array_pro    : L_CORCHETE values R_CORCHETE'''
    t[0] = ArrayState(t.lineno(1), find_column(input, t.slice[1]), t[2])


############################################## ASIGNACION DE ELEMENTOS DE ARREGLO ##############################################
def p_instruccion_array_assign_pro(t):
    '''array_assign_pro    : LITERAL dimensions IGUAL a'''
    t[0] = ArrayAssign(t.lineno(1), find_column(input, t.slice[1]), t[1], t[2], t[4])


############################################## NATIVAS ##############################################

def p_instruccion_nativas(t):
    '''nativeFun    : TOSTRING
                    | TOFIXED
                    | TOEXPONENTIAL
                    | TOLOWERCASE
                    | TOUPPERCASE
                    | SPLIT
                    | CONCAT
                    | LENGTH
                    | PUSH'''

    t[0] = return_native_fun_type(t[1])
    # print("EVALUANDO NATIVAS EN RETURN")
    # print(t[0])


def p_error(t):
    # print("Error sintáctico en '%s'" % t.value+" "+ t.type)
    if t is not None:
        global_arr.append(
            ExceptionPyType("ERROR SINTACTICO en " + str(t.value) + " SE ESPERABA ALGO MAS", t.lexer.lineno,
                            find_column(input, t)))


# def test_lexer(lexer):
#    while True:
#        tok = lexer.token()
#        if not tok:
#            break  # No more input
#        print(tok)


import ply.yacc as yacc


def parse(inp):
    global parser
    global lexer
    lexer = lex.lex(reflags=re.IGNORECASE)
    parser = yacc.yacc()
    lexer.lineno = 1
    # print("TAMAÑO ARREGLO:",len(global_arr))
    return parser.parse(inp)


instrucciones: Instruction = parse("""
interface Node {
    value: number;
    izq: any;
    der: any;
};

interface Tree {
    root: any;
};

let arbol: Tree = { root: "" };

function insertar(nodo, value: number): Node {
    if (typeof(nodo) !== "string") {
        nodo = { value: value, izq: "", der: "" };
    } else if (value < nodo.value) {
        nodo.izq = insertar(nodo.izq, value);
    } else {
        nodo.der = insertar(nodo.der, value);
    }
    return nodo;
}

function preOrden(nodo) {
    if (typeof(nodo) === "Node") {
        console.log(nodo.value);
        preOrden(nodo.izq);
        preOrden(nodo.der);
    }
}

function inOrden(nodo: Node) {
    if (typeof(node.value) === "number") {
        inOrden(nodo.izq);
        console.log(nodo.value);
        inOrden(nodo.der);
    }
}

function postOrden(nodo) {
    if (typeof(nodo) === "Node") {
        postOrden(nodo.izq);
        postOrden(nodo.der);
        console.log(nodo.value);
    }
}

function encontrarValor(nodo, valor: number): boolean {
    let aux: Node = nodo;
    while (typeof(aux) === "Node") {
        if (aux.value === valor) {
            return true;
        } else if (aux.value > valor) {
            aux = aux.izq;
        } else {
            aux = aux.der;
        }
    }
    return false;
}

function encontrarValorR(nodo, valor: number): boolean {
    if (typeof(nodo) !== "Node") {
        return false;
    }
    if (nodo.value === valor) {
        return true;
    } else if (nodo.value > valor) {
        return encontrarValorR(nodo.izq, valor);
    } else {
        return encontrarValorR(nodo.der, valor);
    }
}

console.log("INSERTANDO DATOS");
arbol.root = insertar(arbol.root, 35);
arbol.root = insertar(arbol.root, 15);
arbol.root = insertar(arbol.root, 55);
arbol.root = insertar(arbol.root, 4);
arbol.root = insertar(arbol.root, 67);
arbol.root = insertar(arbol.root, 100);
arbol.root = insertar(arbol.root, 36);
arbol.root = insertar(arbol.root, 10);
arbol.root = insertar(arbol.root, 1);
arbol.root = insertar(arbol.root, 3);
console.log("SE TERMINO DE INSERTAR DATOS");

console.log("PREORDEN");
preOrden(arbol.root);
console.log("INORDEN");
inOrden(arbol.root);
console.log("POSTORDEN");
postOrden(arbol.root);

console.log("BUSCANDO VALORES");
console.log("Existe 7: " , encontrarValor(arbol.root, 7));
console.log("Existe 36: " , encontrarValor(arbol.root, 36));
console.log("Existe 1: " , encontrarValor(arbol.root, 1));
console.log("Existe 58: " , encontrarValor(arbol.root, 58));

console.log("BUSCANDO VALORES RECURSIVAMENTE");
console.log("Existe 7: " , encontrarValorR(arbol.root, 7));
console.log("Existe 36: " , encontrarValorR(arbol.root, 36));
console.log("Existe 1: " , encontrarValorR(arbol.root, 1));
console.log("Existe 58: " , encontrarValorR(arbol.root, 58));


""")

##############  VISITOR DEBUG  #################
errors = []
table= SymbolTable()
debbuger= Debugger(table,errors)


if instrucciones is not None:
   for instruccion in instrucciones:
       instruccion.accept(debbuger)

errorsR = errors
tableR =  SymbolTable()
console= []
VariableType().clean_types()
tableR.symbols = debbuger.symbol_table.getAllFunctions()
#################  VISITOR RUNNER  #################
print("#################  VISITOR RUNNER  #################")
runner = Runner(tableR,errorsR,console)
if instrucciones is not None:
    for instruccion in instrucciones:
        instruccion.accept(runner)
print("#############################TABLA DE SIMBOLOS")
for i in runner.symbol_table.symbols:
    print(str(i))
print("#############################ERRORES")
if len(runner.errors) > 0:
    for error in runner.errors:
        print(str(error))
print("#############################CONSOLE")
for console in runner.console:
    print(str(console))
# objeto_return= ModelResponse(runner.symbol_table.symbols,runner.errors,runner.console)
# print("#############################OBJETO RETURN")
# print(objeto_return)

#################  VISITOR CSTDRAWER  #################

# drawer = CstDrawer()
# content = "digraph {\n"
# if instrucciones is not None:
#    for i in instrucciones:
#        content = content + f'init -> {i.node_name()}\n'
#        content = content + i.accept(drawer)

# content = content+"}\n"

# print("#### CST ####")
# print(content)
#table = TableC3d()
#code_c3d = C3DGenerator(table)
#code_c3d.cleanAll()
#if instrucciones is not None:
#    for instruccion in instrucciones:
#        instruccion.accept(code_c3d)
#print("#############################CODIGO C3D")
#print(code_c3d.get_code())
#print("#############################TABLA DE SIMBOLOS")
#print(str(code_c3d.symbol_table))
