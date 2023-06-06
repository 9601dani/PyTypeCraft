
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
    'for ' : 'FOR',
    'while' : 'WHILE',
    'continue' : 'CONTINUE',
    'break' : 'BREAK',
    # Natives Functions
    '.toString' : 'TOSTRING',
    '.tofixed' : 'TOFIXED',
    '.toExponential' : 'TOEXPONENTIAL',
    '.toLowercase' : 'TOLOWERCASE',
    '.toUppercase' : 'TOUPPERCASE',
    '.split' : 'SPLIT',
    '.concat' : 'CONCAT',
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
    'DOBLE_IGUAL',
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
    'IGUAL',
    # Signos de Puntuacion
    'PUNTO',
    'COLON',
    'SEMI_COLON',
    'COMA',
    'CADENA',
    'LITERAL',
] + list(reservadas.values())

# Tokens
t_DOBLE_IGUAL = r'=='
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
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += t.value.count('\n')

# Expresion Regular para comentarios simple
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# ignorar espacios
t_ignore = " \t"
# Manejo de Linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de columna
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def t_error(t):
    errores.append(Excepcion("Lexico","Error léxico." + t.value[0] , t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

# Se construye el analizador lexico
import ply.lex as lex
lexer = lex.lex(reflags= re.IGNORECASE)

##GRAMATICA "CUP"
import os
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
    '''instruccion      : console_pro'''
    t[0] = t[1]

def p_instruccion_console(t):
    '''console_pro      : CONSOLE PUNTO LOG L_PAREN expresion R_PAREN SEMI_COLON '''
    #t[0] = ConsoleLog(t.lineno(1),find_column(input, t.slice[1]),t[3])
    print(f"""si encontre algo en la produccion console.log -> {t[5]} """)

def p_instruccion_expresion(t):
    '''expresion      : CADENA
                      | LITERAL'''
    t[0] = t[1]
def p_error(t):
    print("Error sintáctico en '%s'" % t.value+" "+ t.type)

def test_lexer(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
import ply.yacc as yacc
def parse(input):
    parser= yacc.yacc()
    lexer.lineno = 1
    return parser.parse(input)
"""
lexer.input('console.log')
test_lexer(lexer)
"""

#parse('console.log("hola");')