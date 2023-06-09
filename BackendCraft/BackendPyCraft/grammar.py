
import re
import ply.lex as lex

# here start grammar
#--------------------------------------------------------------
# 04-06-2023: Created by Daniel Morales
# proyecto 1 - compiladores 2 usac 2023
#--------------------------------------------------------------
# Definimos las palabras reservadas de nuestro lenguaje
reservadas ={
    # Conditions
    'if' : 'IF',
    'else' : 'ELSE',
    # Loops
    'for' : 'FOR',
    'of' : 'OF',
    'while' : 'WHILE',
    'continue' : 'CONTINUE',
    'break' : 'BREAK',
    # Natives Functions
    #'.toString' : 'TOSTRING',
    #'.tofixed' : 'TOFIXED',
    #'.toExponential' : 'TOEXPONENTIAL',
    #'.toLowercase' : 'TOLOWERCASE',
    #'.toUppercase' : 'TOUPPERCASE',
    #'.split' : 'SPLIT',
    #'.concat' : 'CONCAT',
    'toString' : 'TOSTRING',
    'toFixed' : 'TOFIXED',
    'toExponential' : 'TOEXPONENTIAL',
    'toLowercase' : 'TOLOWERCASE',
    'toUppercase' : 'TOUPPERCASE',
    'split' : 'SPLIT',
    'concat' : 'CONCAT',
    # Print Console
    'console' : 'CONSOLE',
    'log' : 'LOG',
    # Declaration
    'let' : 'LET',
    # Types Declaration
    'string' : 'STRING',
    'boolean' : 'BOOLEAN',
    'number' : 'NUMBER',
    'any' : 'ANY',
    'null' : 'NULL',
    # Funtion
    'function' : 'FUNCTION',
    'return' : 'RETURN',
    # Struct
    'interface' : 'INTERFACE',
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
t_DISTINTO_QUE = r'!='
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
    t.value = t.value[1:-1] # remuevo las comillas

    print(str(t.value))
    t.value = t.value.replace('\\n','\n')
    t.value = t.value.replace('\\r','\r')
    t.value = t.value.replace('\\t','\t')
    t.value = t.value.replace('\\"','\"')
    t.value = t.value.replace("\\'",'\'')
    t.value = t.value.replace('\\\\','\\')
    return t

def t_CARACTER(t):
    r'\'(\\\'|\\"|\\t|\\n|\\\\|[^\'\\\"])?\''
    t.value = t.value[1:-1] # remuevo las comillas

    print(str(t.value))
    t.value = t.value.replace('\\n','\n')
    t.value = t.value.replace('\\r','\r')
    t.value = t.value.replace('\\t','\t')
    t.value = t.value.replace('\\"','\"')
    t.value = t.value.replace("\\'",'\'')
    t.value = t.value.replace('\\\\','\\')
    return t
# Expersion Regular para decimal
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

# Expresion Regular para Entero
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Expresion Regular para Booleano
def t_BOOLEANO(t):
    r'true|false'
    try:
        if t.value.lower()=='true':
            t.value=True
        elif t.value.lower()=='false':
            t.value=False
    except ValueError:
        t.value = 0
    return t

# Expresion Regular para literales
def t_LITERAL(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value,'LITERAL')
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
    #errores.append(Excepcion("Lexico","Error léxico." + t.value[0] , t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

# Se construye el analizador lexico
import ply.lex as lex
lexer = lex.lex(reflags= re.IGNORECASE)

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

def return_operation_type(operation_type):
    if(operation_type== "OR"):
        return OperationType.OR
    elif(operation_type== "AND"):
        return OperationType.AND
    elif(operation_type== "NOT"):
        return OperationType.NOT
    elif(operation_type== "MAYOR_QUE"):
        return OperationType.MAYOR_QUE
    elif(operation_type== "MENOR_QUE"):
        return OperationType.MENOR_QUE
    elif(operation_type== "MAYOR_IGUAL_QUE"):
        return OperationType.MAYOR_IGUAL_QUE
    elif(operation_type== "MENOR_IGUAL_QUE"):
        return OperationType.MENOR_IGUAL_QUE
    elif(operation_type== "DISTINTO_QUE"):
        return OperationType.DISTINTO_QUE
    elif(operation_type== "MAS"):
        return OperationType.MAS
    elif(operation_type== "MENOS"):
        return OperationType.MENOS
    elif(operation_type== "TIMES"):
        return OperationType.TIMES
    elif(operation_type== "DIVIDE"):
        return OperationType.DIVIDE
    elif(operation_type== "MOD"):
        return OperationType.MOD
    elif(operation_type== "POTENCIA"):
        return OperationType.POTENCIA

######## FUNCIÓN UTILIZADA PARA RETORNAR EL TIPO DE FUNCIÓN NATIVA USADA EN LA PRODUCCIÓN 'nativeFun'
def return_native_fun_type(native_type):
    if(native_type == "TOSTRING"):
        return NativeFunType.TOSTRING
    elif(native_type == "TOFIXED"):
        return NativeFunType.TOFIXED
    elif(native_type == "TOEXPONENTIAL"):
        return NativeFunType.TOEXPONENTIAL
    elif(native_type == "TOLOWERCASE"):
        return NativeFunType.TOLOWERCASE
    elif(native_type == "TOUPPERCASE"):
        return NativeFunType.TOUPPERCASE
    elif(native_type == "SPLIT"):
        return NativeFunType.SPLIT
    elif(native_type == "CONCAT"):
        return NativeFunType.CONCAT

def p_init(t):
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    if(t[2] != ""):
        t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion'
    if(t[1] == ""):
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instruccion(t):
    '''instruccion      : console_pro sc
                        | declaration_instruction sc
                        | assig_pro sc
                        | if_pro sc
                        | while_pro sc
                        | for_pro sc
                        | for_each_pro sc
                        | interface_pro sc
                        | continue_pro sc
                        | break_pro sc
                        | return_pro sc
                        | function_pro sc
                        | sumadores sc'''
    t[0] = t[1]
############################################## PRODUCCION ';' ##############################################
def p_semi_colon(t):
    '''sc   : SEMI_COLON
            |'''


############################################## DECLARACION DE FUNCIÓN ##############################################
def p_instruccion_function(t):
    '''function_pro : FUNCTION LITERAL L_PAREN parameters_pro R_PAREN L_LLAVE instrucciones R_LLAVE'''

def p_instruccion_function2(t):
    '''function_pro : FUNCTION LITERAL L_PAREN R_PAREN L_LLAVE instrucciones R_LLAVE'''

############################################## PARAMETROS ##############################################

def p_instruccion_parameters(t):
    '''parameters_pro   : parameters_pro COMA parameter_pro'''

def p_instruccion_parameters2(t):
    '''parameters_pro   : parameter_pro'''


def p_instruccion_parameter(t):
    '''parameter_pro    : LITERAL COLON type'''

def p_instruccion_parameter2(t):
    '''parameter_pro    : LITERAL'''




############################################## CONTINUE / BREAK / RETURN ##############################################
def p_instruccion_continue(t):
    '''continue_pro : CONTINUE'''

def p_instruccion_break(t):
    '''break_pro : BREAK'''

def p_instruccion_return(t):
    '''return_pro : RETURN'''

def p_instruccion_return2(t):
    '''return_pro : RETURN a'''

############################################## DECLARACION DE INTERFACE ##############################################

def p_instruccion_declarationInterface(t):
    '''interface_pro    : INTERFACE LITERAL L_LLAVE interface_atributos R_LLAVE'''


def p_instruccion_interfaceAtributos(t):
    '''interface_atributos  : interface_atributos interface_atributo sc'''

def p_instruccion_interfaceAtributos2(t):
    '''interface_atributos  : '''

def p_intruccion_interfaceAtributo(t):
    '''interface_atributo   : LITERAL COLON type'''

def p_instruccion_interfaceAtributo2(t):
    '''interface_atributo   : LITERAL'''

############################################## DECLARACION DE VARIABLE ##############################################
def p_instruccion_declarationInstruction(t):
    '''declaration_instruction      : LET declaracion_list'''
    t[0] = Declaration(t.lineno(1),find_column(input, t.slice[1]),"LET",t[2])

def p_instruccion_declaracion_list(t):
    '''declaracion_list      : declaracion_list COMA assignacion_instruction'''
    [t[0]].append(t[3])

def p_instruccion_declaracion_list2(t):
    '''declaracion_list      : assignacion_instruction'''
    t[0] = []
    t[0].append(t[1])

def p_instruccion_assignacion_instruction(t):
    '''assignacion_instruction      : LITERAL COLON type IGUAL a'''
    t[0] = Assignment(t.lineno(1),find_column(input, t.slice[1]),t[1],VariableType().buscar_type(t[3]),t[5], False)

def p_instruccion_assingnacion_instruction2(t):
    '''assignacion_instruction      : LITERAL COLON type'''
    t[0] = Assignment(t.lineno(1),find_column(input, t.slice[1]),t[1],VariableType().buscar_type(t[3]),None,False)

def p_instruccion_assignacion_instruction3(t):
    '''assignacion_instruction      : LITERAL IGUAL a'''
    t[0] = Assignment(t.lineno(1),find_column(input, t.slice[1]),t[1],None,t[3], True)
def p_instruccion_type(t):
    '''type      : NUMBER
                 | STRING
                 | BOOLEAN
                 | ANY
                 | LITERAL'''
    t[0] = t[1]
############################################## ASIGNACION DE VARIABLE ##############################################
def p_instruccion_assig_pro(t):
    '''assig_pro      : LITERAL IGUAL a'''
    t[0] = OnlyAssignment(t.lineno(1),find_column(input, t.slice[1]), t[1],VariableType().buscar_type("DEFINIRLA"),t[3])
############################################## IF ##############################################
def p_instruccion_if_pro(t):
    '''if_pro      : IF L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE else_pro'''
    t[0] = IfState(t.lineno(1),find_column(input, t.slice[1]),t[3],t[6],t[8])

#CONTENPLAR LA IDEA QUE instrucciones PUEDE VENIR VACIO
############################################## ELSE ##############################################
def p_instruccion_else_pro(t):
    '''else_pro      : ELSE IF L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE else_pro'''
    t[0] = IfState(t.lineno(1),find_column(input, t.slice[1]),t[4],t[7],t[9])

def p_instruccion_else_pro2(t):
    '''else_pro      : ELSE L_LLAVE instrucciones R_LLAVE'''
    t[0] = ElseState(t.lineno(1),find_column(input, t.slice[1]),t[3])

def p_instruccion_else_pro3(t):
    '''else_pro      : '''
    t[0] = None

############################################## WHILE ##############################################
def p_instruccion_while_pro(t):
    '''while_pro      : WHILE L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE'''
    t[0] = WhileState(t.lineno(1),find_column(input, t.slice[1]),t[3],t[6])

############################################## FOR ##############################################
def p_instruccion_for_pro(t):
    '''for_pro      : FOR L_PAREN declaration_instruction SEMI_COLON a SEMI_COLON assig_pro R_PAREN L_LLAVE instrucciones R_LLAVE
                    | FOR L_PAREN assig_pro SEMI_COLON a SEMI_COLON assig_pro R_PAREN L_LLAVE instrucciones R_LLAVE'''

    t[0] = ForState(t.lineno(1),find_column(input, t.slice[1]),t[3],t[5],t[7],t[10])

############################################## FOR EACH ##############################################

def p_instruccion_for_each_pro(t):
    '''for_each_pro : FOR L_PAREN for_each_dec R_PAREN L_LLAVE instrucciones R_LLAVE'''

def p_instruccion_fore_dec(t):
    '''for_each_dec : LET LITERAL OF a'''

def p_instruccion_fore_dec_type(t):
    '''for_each_dec : LET LITERAL COLON type OF a'''


############################################## CONSOLE.LOG ##############################################
def p_instruccion_console(t):
    '''console_pro      : CONSOLE PUNTO LOG L_PAREN expresion R_PAREN'''
    t[0] = ConsoleLog(t.lineno(1),find_column(input, t.slice[1]),t[5])
    print(f"""si encontre algo en la produccion console.log -> {t[5]} """)

def p_instruccion_expresion(t):
    '''expresion      : expresion COMA a'''
    t[0].append(t[3])
def p_instruccion_expresion2(t):
    '''expresion      : a'''
    t[0] = []
    t[0].append(t[1])

def p_instruccion_expresion3(t):
    '''a      : a OR b'''
    t[0] = BinaryOperation(t.lineno(1),find_column(input, t.slice[2]),t[1], t[3], OperationType.OR)
def p_instruccion_expresion4(t):
    '''a      : b'''
    t[0] = t[1]

def p_instruccion_expresion5(t):
    ''' b      : b AND c'''
    t[0] = BinaryOperation(t.lineno(1),find_column(input, t.slice[2]),t[1], t[3], OperationType.AND)

def p_instruccion_expresion6(t):
    ''' b      : c'''
    t[0] = t[1]

def p_instruccion_expresion7(t):
    ''' c      : NOT d'''
    t[0] = UnaryOperation(t.lineno(1),find_column(input, t.slice[2]),t[2], OperationType.NOT)

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
    t[0] = BinaryOperation(t.lineno(1),find_column(input, t.slice[2]),t[1], t[3], return_operation_type(t[2]))

def p_instruccion_expresion10(t):
    ''' d     : e '''
    t[0] = t[1]

def p_instruccion_expresion11(t):
    ''' e     : e MAS f
                | e MENOS f '''
    t[0] = BinaryOperation(t.lineno(1),find_column(input, t.slice[2]),t[1], t[3], return_operation_type(t[2]))

def p_instruccion_expresion12(t):
    ''' e     : f '''
    t[0] = t[1]

def p_instruccion_expresion13(t):
    ''' f     : f TIMES g
                | f DIVIDE g
                | f MOD g
                | f POTENCIA g'''
    t[0] = BinaryOperation(t.lineno(1),find_column(input, t.slice[2]),t[1], t[3], return_operation_type(t[2]))

def p_instruccion_expresion14(t):
    ''' f     : g '''
    t[0] = t[1]

def p_instruccion_expresion15(t):
    '''f    : g PUNTO nativeFun L_PAREN expresion R_PAREN'''

def p_instruccion_expresion16(t):
    ''' g     : ENTERO
              | DECIMAL
              | CADENA
              | LITERAL
              | interface_assi'''

    t[0] = t[1]
def p_instruccion_expresion17(t):
    ''' g     : L_PAREN a R_PAREN'''

    t[0] = t[2]

def p_instruccion_sumadores(t):
        ''' sumadores     : LITERAL MAS MAS
                          | LITERAL MENOS MENOS '''
        if(t[2] == "MAS"):
            t[0] = UnaryOperation(t.lineno(1),find_column(input, t.slice[2]),t[1], OperationType.INCREMENT)
        else:
            t[0] = UnaryOperation(t.lineno(1),find_column(input, t.slice[2]),t[1], OperationType.DECREMENT)
############################################## ASIGNAR INTERFACE ##############################################
def p_instruccion_interfaceAssi(t):
    '''interface_assi   : L_LLAVE atributos_assi R_LLAVE'''

############################################## ASIGNAR ATRIBUTOS INTERFACE ##############################################
def p_instruccion_inter_atributesAssi(t):
    '''atributos_assi   : atributos_assi COMA LITERAL COLON a'''

def p_instruccion_inter_atributesAssi2(t):
    '''atributos_assi   : LITERAL COLON a'''


############################################## NATIVAS ##############################################

def p_instruccion_nativas(t):
    '''nativeFun    : TOSTRING
                    | TOFIXED
                    | TOEXPONENTIAL
                    | TOLOWERCASE
                    | TOUPPERCASE
                    | SPLIT
                    | CONCAT'''
    t[0] = return_native_fun_type(t[1])



def p_error(t):
    print("Error sintáctico en '%s'" % t.value+" "+ t.type)

def test_lexer(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
import ply.yacc as yacc
def parse(inp):
    global parser
    global lexer
    lexer = lex.lex(reflags=re.IGNORECASE)
    parser= yacc.yacc()
    lexer.lineno = 1
    return parser.parse(inp)

lexer.input('''
console.log(3+5);''')
test_lexer(lexer)


instruccion : [Instruction] =parse("""
let edad: number, edad1 = 18;
edad= 19


let numero: number =10.toFixed(1);

if (edad < 18) {
    console.log("Eres menor de edad.");
} else if (edad >= 18 && edad < 60) {
    console.log("Eres adulto.");
} else {
    console.log("Eres un adulto mayor.");
};
while (contador <= 5) {
    console.log("Contador: " + contador);
    contador++;
};

console.log("todo  nice");

for (let i = 0; i < 10; i = i +1){
    console.log("a");
};

for (i = 0; i < 10; i = i +1){
    console.log("a");
    continue;
    
};

for(let letra:string of "hola mundo") {
    console.log("for each ezzzz");
};

for(let letra of cadena) {
    console.log("for each ezzzz");
    break;
};

interface Carro {
    placa: string;
    color: string;
};

let c1: Carro = {
    placa: "P0S22",
    color: "verde"
};

function suma(c: Carro){
    console.log("sumando algo...");
    return;
    
};

function suma(a:number, b){
    return a + b;
}

""")

for i in instruccion:
    print(str(type(i)).__str__())