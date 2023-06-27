from .Visitor import Visitor
from ..models import Assignment, Parameter
from ..models import ArrayState, ArrayAssign
from ..models import BinaryOperation
from ..models import Break
from ..models import CallArray
from ..models import CallAttribute
from ..models import CallFunction
from ..models import ConsoleLog
from ..models import Continue
from ..models import Declaration
from ..models import ElseState
from ..models import ForEachState
from ..models import ForState
from ..models import FunctionState
from ..models import IfState
from ..models import InterfaceAssign
from ..models import InterAttributeAssign
from ..models import InterfaceState
from ..models import NativeFunction
from ..models import OnlyAssignment
from ..models import Return
from ..models import UnaryOperation
from ..models import WhileState
from ..models import Value
from ..models.Variable import Variable
from ..models.SymbolType import SymbolType
from ..symbolTable.SymbolTable import SymbolTable
from ..models.VariableType import VariableType
from ..models.ValueType import ValueType
from ..models.OperationType import OperationType
from ..models.NativeFunType import NativeFunType
from ..models.InterfaceState import InterfaceState
from ..symbolModel.InterfaceModel import InterfaceModel
from ..symbolModel.FunctionModel import FunctionModel
from ..symbolTable.ScopeType import ScopeType
from ..symbolModel.ArrayModel import ArrayModel
from ..models.Continue import Continue
from ..models.Break import Break
from ..models.Return import Return
from ..models.Value import Value
from ..models.ReturnC3d import ReturnC3d
from ..ObjectError.ExceptionPyType import ExceptionPyType
from ..symbolTable.TableC3d import TableC3d
import copy
from decimal import Decimal


class C3DGenerator(Visitor):
    def __init__(self, symbol_table: TableC3d):
        #### Tabla de simbolos ####
        super().__init__()
        self.symbol_table = symbol_table
        #### Contadores C3D ####
        self.contadores_tmp = 0
        self.contadores_etiquetas = 0
        self.lista_tmp = []
        self.lista_nativas =''
        #### manejadores del texto final ####
        self.header = ""
        self.code = ""
        self.footer = ""
        self.funcs = ''
        self.in_func = False
        self.in_natives = False
    ####### Metodos nativas #######
        self.print_string= False
        self.compare_string= False
        self.potencia= False
        self.length= False
        self.upper= False
        self.lower= False
        self.relacionales = ['>', '<', '>=', '<=']
        ### Los importes de go ####
        self.imports = []
        ### importe de fmt (console) y math (math) ####
        self.imports_default = ['fmt', 'math']

    def cleanAll(self):
        self.contadores_tmp = 0
        self.code = ""
        self.lista_tmp = []
        self.imports = []
        self.imports_default = ['fmt', 'math']
######## nativas ########
        self.print_string= False
        self.compare_string= False
        self.potencia= False
        self.length= False
        self.upper= False
        self.lower= False
    ###### METODOS CODIGO 3D ########
    def set_import(self, lib):
        if lib in self.imports_default:
            self.imports_default.remove(lib)
        else:
            return
        ret= f'import(\n\t"{lib}"\n)\n'
        self.imports.append(ret)

    ####  TODO: CODIGO ####
    def get_header(self):
        code= '/*------HEADER------*/\n package main;\n\n'
        if len(self.imports) > 0:
            for temp in self.imports:
                code += temp
        if len(self.lista_tmp) > 0:
            code += '\n/*------TEMPORALES------*/\n'
            code += 'var '
            for temp in self.lista_tmp:
                code += temp + ','
            code = code[:-1]
            code += ' float64;\n\n'
        ###### DECLARAMOS LOS APUNTADORES DE HEAP Y STACK ######
        code += '/*------APUNTADORES------*/\n'
        code += 'var P, H float64;\nvar stack [30101999] float64;\nvar heap [30101999] float64;\n\n'
        return code

    def get_code(self):
        code = '/*------CODE------*/\n'
        #TODO: Aun falta agregar las nativas aqui
        return f'{code+self.get_header()}{self.lista_nativas}\n{self.funcs}\n func main() {{\n{self.code}\n}}'

    def code_in(self, code, tab="\t"):
        if self.in_natives:
            if self.lista_nativas == '':
                self.lista_nativas= self.lista_nativas+ '/*------NATIVAS------*/\n'
            self.lista_nativas = self.lista_nativas + tab + code
        elif self.in_func:
            if self.funcs == '':
                self.funcs = self.funcs + '/*------FUNCIONES------*/\n'
            self.funcs = self.funcs + tab + code
        else:
            self.code = self.code + '\t' + code

    def add_comment(self, comment):
        self.code_in(f'/* {comment} */\n')

    def add_space(self):
        self.code_in("\n")

#####  TODO: MANAGE TMP #####
    def add_temp(self):
        temp = f't{self.contadores_tmp}'
        self.contadores_tmp += 1
        self.lista_tmp.append(temp)
        return temp

########  TODO: MANAGE ETIQUETAS ########
    def new_label(self):
        label = f'L{self.contadores_etiquetas}'
        self.contadores_etiquetas += 1
        return label

    def put_label(self, label):
        self.code_in(f'{label}:\n')

    def add_ident(self):
        self.code_in("")

######  TODO: MANAGE GOTO ######
    def add_goto(self, label):
        self.code_in(f'goto {label};\n')

#########  TODO: MANAGE IF #########
    def add_if(self, left, right, op, label):
        self.code_in(f'if {left} {op} {right} {{goto {label};}}\n')

#####  TODO: EXPRESIONES #####
    def add_expression(self, result, left, right, op):
        self.code_in(f'{result} = {left} {op} {right};\n')

    def add_expression_unary(self, result, left, op):
        self.code_in(f'{result} = {op} {left};\n')

    def add_potencia(self, result, left, right):
        self.code_in(f'{result} = math.Pow({left}, {right});\n')

    def add_mod(self, result, left, right):
        self.code_in(f'{result} = math.Mod({left}, {right});\n')

    def add_assig(self, result, left):
        self.code_in(f'{result} = {left};\n')
#####  TODO: FUNCIONES #####
    def add_begin_func(self, id):
        if not self.in_natives:
            self.in_func = True
        self.code_in(f'func {id}(){{\n', '')

    def add_end_func(self):
        self.code_in('return;\n}\n')
        if not self.in_natives:
            self.in_func = False
#####  TODO: MANAGE STACK #####
    def set_stack(self, pos, value):
        self.code_in(f'stack[int({pos})] = {value};\n')

    def get_stack(self, place, pos):
        self.code_in(f'{place} = stack[int({pos})];\n')
###### TODO: MANAGE ENVIROMENT ######
    def new_env(self, size):
        self.code += '/*------NUEVO ENTORNO------*/\n'
        self.code += f'P = P + {size};\n'

    def ret_env(self, size):
        self.code += '/*------RETORNO ENTORNO------*/\n'
        self.code += f'P = P - {size};\n'

    def call_fun(self, id):
        self.code += f'/*------LLAMADA A FUNCION------*/\n'
        self.code += f'{id}();\n'
    ######  TODO: MANAGE HEAP ######
    def set_heap(self, pos, value):
        self.code += f'heap[int({pos})] = {value};\n'

    def get_heap(self, place, pos):
        #TODO: SE CONVIERTE A INT PORQUE ES EL INDICE DEL HEAP, PERO VIENE FLOAT ENTONCES SE CONVIERTE A INT
        self.code += f'{place} = heap[int({pos})];\n'
    ##### NEXT HEAP #####
    def next_heap(self):
        self.code += f'H = H + 1;\n'

    #####  TODO: INSTRUCCIONES #####
    def add_print(self,type, value):
        self.code += f'/*------PRINT------*/\n'
        self.set_import('fmt')
        self.code += f'fmt.Printf("%{type}", {value});\n'

    def print_float(self, type,value):
        self.code += f'/*------PRINT------*/\n'
        self.set_import('fmt')
        self.code += f'fmt.Printf("%{type}", {value});\n'

    def print_true(self):
        self.set_import('fmt')
        self.add_ident()
        self.add_print("c", "116")
        self.add_ident()
        self.add_print("c", "114")
        self.add_ident()
        self.add_print("c", "117")
        self.add_ident()
        self.add_print("c", "101")

    def print_false(self):
        self.set_import('fmt')
        self.add_ident()
        self.add_print("c", "102")
        self.add_ident()
        self.add_print("c", "97")
        self.add_ident()
        self.add_print("c", "108")
        self.add_ident()
        self.add_print("c", "115")
        self.add_ident()
        self.add_print("c", "101")

########## TODO: MANAGE NATIVAS ##########
    def f_to_string(self):
        self.in_natives = True
        self.add_begin_func('toString')
        self.in_natives = False
    def add_print_char(self, value):
        self.set_import('fmt')
        self.code_in(f'fmt.Printf("%c", int({value}));\n')
    def f_print_string(self):
        self.set_import('fmt')
        if self.print_string:
            return
        self.print_string = True
        self.in_natives = True

        self.add_begin_func('printString')
        return_lbl = self.new_label()
        compare_lbl = self.new_label()
        temp_p = self.add_temp()
        temp_h = self.add_temp()
        self.add_expression(temp_p, 'P', '1', '+')
        self.get_stack(temp_h, temp_p)
        temp_c = self.add_temp()
        self.put_label(compare_lbl)
        self.add_ident()
        self.get_heap(temp_c, temp_h)
        self.add_ident()
        self.add_if(f'heap[int({temp_h})]', '-1', '==', return_lbl)
        self.add_ident()
        self.add_print_char(f'heap[int({temp_h})]')
        self.add_ident()
        self.add_expression(temp_h, temp_h, '1', '+')
        self.add_ident()
        self.add_goto(compare_lbl)
        self.put_label(return_lbl)
        self.add_end_func()
        self.in_natives = False

    def f_length(self):
        if self.length:
            return
        self.length = True
        self.in_natives = True
        self.add_begin_func('length')
        lbl_return = self.new_label()
        ## tmp del punteo del stack
        temp = self.add_temp()
        ## tmp del puntero del heap
        temp_h = self.add_temp()
        ## tmp del resultado
        temp_r = self.add_temp()

        # SE BUSCA LA POSICION EN STACK
        self.add_expression(temp, 'P', '1', '+')

        # SE OBTIENE EL VALOR DE LA POSICION EN STACK
        self.get_stack(temp_h, temp)
        self.get_heap(temp_r, temp_h)
        self.set_heap('P', temp_r)

        self.add_goto(lbl_return)
        self.put_label(lbl_return)
        self.add_end_func()
        self.in_natives = False

    def f_upper_case(self):
        if self.upper:
            return
        self.upper = True
        self.in_natives = True
        self.add_begin_func('upperCase')

        t1= self.add_temp()
        t2= self.add_temp()
        t3= self.add_temp()

        lbl0= self.new_label()
        lbl1= self.new_label()
        lbl2= self.new_label()

        self.add_assig(t1,'H')
        self.add_expression(t2,'P','1','+')
        self.get_stack(t2,t2)
        self.put_label(lbl0)

        self.get_heap(t3,t2)
        self.add_if(t3, '-1', '==', lbl2)
        self.add_if(t3, '97', '<', lbl1)
        self.add_if(t3, '122', '>', lbl1)
        self.add_expression(t3,t3,'32','-')
        self.put_label(lbl1)

        self.set_heap('H',t3)
        self.next_heap()
        self.add_expression(t2,t2,'1','+')
        self.add_goto(lbl0)

        self.put_label(lbl2)
        self.set_heap('H','-1')
        self.next_heap()
        self.set_stack('P',t1)
        self.add_end_func()
        self.in_natives = False

    def f_lower_case(self):
        if self.upper:
            return
        self.upper = True
        self.in_natives = True

        self.add_begin_func('lowerCase')

        t1= self.add_temp()
        t2= self.add_temp()
        t3= self.add_temp()

        lbl0= self.new_label()
        lbl1= self.new_label()
        lbl2= self.new_label()

        self.add_assig(t1,'H')
        self.add_expression(t2,'P','1','+')
        self.get_stack(t2,t2)
        self.put_label(lbl0)

        self.get_heap(t3,t2)
        self.add_if(t3, '-1', '==', lbl2)
        self.add_if(t3, '65', '<', lbl1)
        self.add_if(t3, '90', '>', lbl1)
        self.add_expression(t3,t3,'32','+')
        self.put_label(lbl1)

        self.set_heap('H',t3)
        self.next_heap()
        self.add_expression(t2,t2,'1','+')
        self.add_goto(lbl0)

        self.put_label(lbl2)
        self.set_heap('H','-1')
        self.next_heap()
        self.set_stack('P',t1)
        self.add_end_func()
        self.in_natives = False

    def f_compare_string(self):
        if self.compare_string:
            return
        self.compare_string = True
        self.in_natives = True
        self.add_begin_func('compareString')
        return_lbl = self.new_label()

        t2 = self.add_temp()
        self.add_expression(t2, 'P', '1', '+')
        t3= self.add_temp()
        self.get_stack(t3, t2)
        self.add_expression(t2, t2, '1', '+')
        t4= self.add_temp()
        self.get_stack(t4, t2)

        l1 = self.new_label()
        l2 = self.new_label()
        l3 = self.new_label()
        self.put_label(l1)

        t5 = self.add_temp()
        self.add_ident()
        self.get_heap(t5, t3)

        t6 = self.add_temp()
        self.add_ident()
        self.get_heap(t6, t4)

        self.add_ident()
        self.add_if(t5, t6, '!=', l3)
        self.add_ident()
        self.add_if(t5, '-1', '==', l2)

        self.add_ident()
        self.add_expression(t3, t3, '1', '+')
        self.add_ident()
        self.add_expression(t4, t4, '1', '+')
        self.add_ident()
        self.add_goto(l1)

        self.put_label(l2)
        self.add_ident()
        self.set_stack('P', '1')
        self.add_ident()
        self.add_goto(return_lbl)
        self.put_label(l3)
        self.add_ident()
        self.set_stack('P', '0')
        self.put_label(return_lbl)
        self.add_end_func()
        self.in_natives = False

    def f_potencia(self):
        if self.potencia:
            return
        self.potencia = True
        self.in_natives = True
        self.add_begin_func('potencia')

        lbl0 = self.new_label()
        lbl1 = self.new_label()
        lbl2 = self.new_label()
        lbl3 = self.new_label()

        t1 = self.add_temp()
        t2 = self.add_temp()
        t3 = self.add_temp()
        t4 = self.add_temp()

        self.add_expression(t2, 'P', '1', '+')
        self.get_stack(t1, t2)
        self.add_expression(t3, t1, '','')
        self.add_expression(t4, t1, '', '')
        self.add_expression(t2, 'P', '2', '+')
        self.get_stack(t1, t2)
        self.add_if(t1, '0', '==', lbl1)
        self.put_label(lbl2)
        self.add_ident()
        self.add_if(t1, '1', '<=', lbl0)
        self.add_ident()
        self.add_expression(t3, t3,t4,'*')
        self.add_ident()
        self.add_expression(t1,t1,'1', '-')
        self.add_ident()
        self.add_goto(lbl2)
        self.put_label(lbl0)
        self.add_ident()
        self.set_stack('P', t3)
        self.add_ident()
        self.add_goto(lbl3)
        self.put_label(lbl1)
        self.add_ident()
        self.set_stack('P', '1')
        self.put_label(lbl3)
        self.add_end_func()
        self.add_space()
        self.in_natives = False

    def f_relational_string(self, op):
        if op in self.relacionales:
            self.relacionales.remove(op)
        else:
            return

        if op == '>':
            self.addBeginFunc('relationalStringM')
        elif op == '<':
            self.addBeginFunc('relationalStringm')
        elif op == '>=':
            self.addBeginFunc('relationalStringMI')
        elif op == '<=':
            self.addBeginFunc('relationalStringmI')


        t2 = self.add_temp()
        t3 = self.add_temp()
        t4 = self.add_temp()
        t5 = self.add_temp()
        t6 = self.add_temp()
        t7 = self.add_temp()
        t8 = self.add_temp()

        Lbl1 = self.new_label()
        Lbl2 = self.new_label()
        Lbl3 = self.new_label()
        Lbl4 = self.new_label()
        Lbl5 = self.new_label()
        Lbl6 = self.new_label()

        self.add_expression(t2, 'P', '1','+')
        self.get_stack(t3, t2)
        self.add_expression(t2, t2,'1','+')
        self.get_stack(t4, t2)
        self.add_expression(t5,'0','','')
        self.add_expression(t7,'0','','')


        self.put_label(Lbl1)
        self.add_ident()
        self.get_heap(t6, t3)
        self.add_ident()
        self.add_if(t6, '-1','==', Lbl2)
        self.add_ident()
        self.add_expression(t5, t5, t6, '+')
        self.add_ident()
        self.add_expression(t3, t3,'1','+')
        self.add_ident()
        self.add_goto(Lbl1)


        self.put_label(Lbl2)
        self.add_ident()
        self.get_heap(t8,t4)
        self.add_ident()
        self.add_if(t8,'-1','==', Lbl3)
        self.add_ident()
        self.add_expression(t7,t7,t8,'+')
        self.add_ident()
        self.add_expression(t4,t4,'1','+')
        self.add_ident()
        self.add_goto(Lbl2)

        self.put_label(Lbl3)
        self.add_ident()
        self.add_if(t5, t7,op, Lbl4)
        self.add_ident()
        self.add_goto(Lbl5)

        self.put_label(Lbl4)
        self.add_ident()
        self.set_stack('P', '1')
        self.add_ident()
        self.add_goto(Lbl6)

        self.put_label(Lbl5)
        self.add_ident()
        self.set_stack('P', '0')

        self.put_label(Lbl6)
        self.add_end_func()
        self.add_space()

        self.inNatives = False

    ############################################# METODOS VISIT #############################################
    def visit_array_assign(self, i: ArrayAssign):
        pass

    def visit_assignment(self, i: Assignment):
        if i.value is not None:
            if i.type is not None:
                self.add_comment('Asignacion de variable')
                val = i.value.accept(self)
                if val is None:
                    self.add_comment('Error al asignar la variable 1')
                    print("Error al asignar la variable 1")
                    return None

                if val.get_tipo() != VariableType().buscar_type(i.type):
                    self.add_comment('Error al asignar la variable, tipos son distintos')
                    return None

                if val.get_tipo() == VariableType().buscar_type('STRING'):
                    simbolo = self.symbol_table.set_tabla(i.id, val.get_tipo(), True, i.find)
                    simbolo.set_tipo_aux(val.get_tipo_aux())
                    simbolo.set_length(val.get_length())
                    simbolo.set_referencia(True)
                else:
                    # Guardado y obtencion de variable. Esta tiene la posicion, lo que nos sirve para asignarlo en el heap
                    simbolo = self.symbol_table.set_tabla(i.id, val.get_tipo(), (val.type == VariableType().buscar_type("STRING") or val.type == VariableType().buscar_type("STRUCT") or val.type == VariableType().buscar_type("ARRAY")), i.find)

                # Obtencion de posicion de la variable
                temp_pos = simbolo.get_pos()
                if not simbolo.is_global:
                    temp_pos = self.add_temp()
                    self.add_expression(temp_pos, 'P', simbolo.get_pos(), "+")

                if(val.type == VariableType().buscar_type("BOOLEAN")):
                    # temp_lbl = self.new_label()
                    #
                    # self.put_label(val.true_lbl)
                    # self.set_stack(temp_pos, "1")
                    #
                    # self.add_goto(temp_lbl)
                    #
                    # self.put_label(val.false_lbl)
                    # self.set_stack(temp_pos, "0")
                    #
                    # self.put_label(temp_lbl)

                    if val.value:
                        self.set_stack(temp_pos, "1")
                    else:
                        self.set_stack(temp_pos, "0")

                else:
                    self.set_stack(temp_pos, val.value)
                self.add_comment("Fin de valor de variable")
                self.add_space()

            else:
                self.add_comment("Compilacion de valor de variable")
                # Compilacion de valor que estamos asignando
                val = i.value.accept(self)
                #if isinstance(val, Excepcion): return val

                if val.get_tipo() == VariableType().buscar_type("ARRAY"):
                    simbolo = self.symbol_table.set_tabla(i.id, val.get_tipo(), True, i.find)
                    simbolo.set_tipo_aux(val.get_tipo_aux())
                    simbolo.set_length(val.get_length())
                    simbolo.set_referencia(val.get_referencia())
                elif val.get_tipo() == VariableType().buscar_type('STRING'):
                    simbolo = self.symbol_table.set_tabla(i.id, val.get_tipo(), True, i.find)
                    simbolo.set_tipo_aux(val.get_tipo_aux())
                    simbolo.set_length(val.get_length())
                    simbolo.set_referencia(True)

                else:
                    # Guardado y obtencion de variable. Esta tiene la posicion, lo que nos sirve para asignarlo en el heap
                    in_heap = val.type == VariableType().buscar_type("STRING") or val.type == VariableType().buscar_type("ARRAY")
                    simbolo = self.symbol_table.set_tabla(i.id, val.get_tipo(), in_heap, i.find)
                    print("simbolo: ",simbolo)
                # Obtencion de posicion de la variable
                temp_pos = simbolo.get_pos()
                if not simbolo.is_global:
                    temp_pos = self.add_temp()
                    self.add_expression(temp_pos, 'P', simbolo.pos, "+")

                if(val.type == VariableType().buscar_type("BOOLEAN")):
                    if val.value:
                        self.set_stack(temp_pos, "1")
                    else:
                        self.set_stack(temp_pos, "0")

                else:
                    self.set_stack(temp_pos, val.value)
                self.add_comment("Fin de valor de variable")
                self.add_space()
                return temp_pos
        else:
            self.add_comment("Compilacion de valor de variable")
            if not i.type:
                simbolo = self.symbol_table.set_tabla(i.id, VariableType().buscar_type("STRING"), True)
            else:
                simbolo = self.symbol_table.set_tabla(i.id, i.type, True)

            temp_pos = simbolo.get_pos()
            if not simbolo.is_global:
                temp_pos = self.add_temp()
                self.add_expression(temp_pos, 'P', simbolo.pos, "+")

            self.set_stack(temp_pos, i.gosth)
            self.addComment("Fin de valor de variable")

            return temp_pos

    def visit_array_state(self, i: ArrayState):
        pass

    def visit_binary_op(self, i: BinaryOperation):
        temporal= ''
        operator= ''
        left= ''
        right= ''

        left = i.left_operator.accept(self)
        right = i.right_operator.accept(self)

        if i.operator == OperationType.MAS:
            operator = '+'
            temporal = self.add_temp()
            self.add_expression(temporal, left.value, right.value, operator)
            return ReturnC3d(temporal,VariableType().buscar_type("NUMBER"), True)
        elif i.operator == OperationType.MENOS:
            operator = '-'
            temporal = self.add_temp()
            self.add_expression(temporal,left.value, right.value, operator)
            return ReturnC3d(temporal,VariableType().buscar_type("NUMBER"), True)
        elif i.operator == OperationType.TIMES:
            operator = '*'
            temporal = self.add_temp()
            self.add_expression(temporal,left.value, right.value, operator)
            return ReturnC3d(temporal,VariableType().buscar_type("NUMBER"), True)
        elif i.operator == OperationType.DIVIDE:
            operator = '/'
            temporal = self.add_temp()
            self.add_expression(temporal, left.value, right.value, operator)
            return ReturnC3d(temporal,VariableType().buscar_type("NUMBER"), True)
        #TODO: FALTAN DEMAS OPERACIONES
        elif i.operator == OperationType.MOD:
            temporal= self.add_temp()
            self.set_import('math')
            self.add_mod(temporal, left.value, right.value)
            return ReturnC3d(temporal,VariableType().buscar_type("NUMBER"), True)
        elif i.operator == OperationType.POTENCIA:
            #temp = self.add_temp()
            #self.f_potencia()
            #t5= self.add_temp()

            #self.add_expression(t5, 'P', self.symbol_table.get_size(),'+' )
            #self.add_expression(t5,t5, '1', '+')

            #self.set_stack(t5, left.value)
            #self.add_expression(t5, t5, '1', '+')
            #self.set_stack(t5, right.value)

            #self.new_env(self.symbol_table.get_size())
            #self.call_fun('potencia')
            #self.get_stack(temp, 'P')
            #self.ret_env(self.symbol_table.get_size())

            #return ReturnC3d(temp,VariableType().buscar_type("NUMBER"), True)
            temporal= self.add_temp()
            self.set_import('math')
            self.add_potencia(temporal, left.value, right.value)
            return ReturnC3d(temporal,VariableType().buscar_type("NUMBER"), True)

        elif i.operator == OperationType.MENOR_QUE:
            temporal = self.add_temp()
            value = 1 if left.value < right.value else 0
            self.add_expression(temporal, value, '', '')
            return ReturnC3d(temporal, VariableType().buscar_type("BOOLEAN"), True)
        elif i.operator == OperationType.MAYOR_QUE:
            temporal = self.add_temp()
            value = 1 if left.value > right.value else 0
            self.add_expression(temporal, value, '', '')
            return ReturnC3d(temporal, VariableType().buscar_type("BOOLEAN"), True)
        elif i.operator == OperationType.MENOR_IGUAL_QUE:
            temporal = self.add_temp()
            value = 1 if left.value <= right.value else 0
            self.add_expression(temporal, value, '', '')
            return ReturnC3d(temporal, VariableType().buscar_type("BOOLEAN"), True)
        elif i.operator == OperationType.MAYOR_IGUAL_QUE:
            temporal = self.add_temp()
            value = 1 if left.value >= right.value else 0
            self.add_expression(temporal, value, '', '')
            return ReturnC3d(temporal, VariableType().buscar_type("BOOLEAN"), True)
        elif i.operator == OperationType.TRIPLE_IGUAL:
            temporal = self.add_temp()
            value = 1 if left.value == right.value else 0
            self.add_expression(temporal, value, '', '')
            return ReturnC3d(temporal, VariableType().buscar_type("BOOLEAN"), True)
        elif i.operator == OperationType.DISTINTO_QUE:
            temporal = self.add_temp()
            value = 1 if left.value != right.value else 0
            self.add_expression(temporal, value, '', '')
            return ReturnC3d(temporal, VariableType().buscar_type("BOOLEAN"), True)
        elif i.operator == OperationType.AND:
            temporal = self.add_temp()
            value = 1 if left.value and right.value else 0
            self.add_expression(temporal, value, '', '')
            return ReturnC3d(temporal, VariableType().buscar_type("BOOLEAN"), True)
        elif i.operator == OperationType.OR:
            temporal = self.add_temp()
            value = 1 if left.value or right.value else 0
            self.add_expression(temporal, value, '', '')
            return ReturnC3d(temporal, VariableType().buscar_type("BOOLEAN"), True)

    def visit_break(self, i: Break):
        self.add_goto(self.symbol_table.break_lbl)

    def visit_call_arr(self, i: CallArray):
        pass

    def visit_call_attr(self, i: CallAttribute):
        pass

    def visit_call_fun(self, i: CallFunction):
        pass

    def visit_console(self, i: ConsoleLog):
        for val in i.value:
            print(val)
            result = val.accept(self)
            print(str(result))
            if result is None:
                continue

            if result.type == VariableType().buscar_type("NUMBER"):
                self.add_print('f', result.value)
            elif result.type == VariableType().buscar_type("STRING"):

                self.f_print_string()
                param_temp= self.add_temp()

                self.add_expression(param_temp, 'P', self.symbol_table.size, '+')
                self.add_expression(param_temp, param_temp, '1', '+')
                self.set_stack(param_temp, result.value)

                self.new_env(self.symbol_table.size)
                self.call_fun('printString')

                temp= self.add_temp()
                self.get_stack(temp, 'P')
                self.ret_env(self.symbol_table.size)

            elif result.type == VariableType().buscar_type("BOOLEAN"):
                true_label = self.new_label()
                lbl = self.new_label()
                self.add_if(result.value, '0', '!=', true_label)
                self.print_false()
                self.add_goto(lbl)
                self.put_label(true_label)
                self.print_true()
                self.put_label(lbl)
                # self.add_print('t', f'{result.value} != 0')
            #TODO: FALTAN DEMAS TIPOS

        self.add_print('s', '\"\\n\"')

    def visit_continue(self, i: Continue):
        self.add_goto(self.symbol_table.continue_lbl)

    def visit_declaration(self, i: Declaration):
        if i.type is None:
            # self.errors.append(ExceptionPyType("ERROR EN DECLARACION DE VARIABLE NO TIENE TIPO DE VARIABLE.", i.line, i.column))
            return None
        for instruction in i.instructions:
            variable = instruction.accept(self)
            if variable is None:
                self.add_comment('Error en declaracion de variable')
                #self.errors.append(ExceptionPyType("ERROR EN DECLARACION DE VARIABLE NO SE PUDO DECLARAR LA VARIABLE DEBIDO QUE ES NULA", i.line, i.column))
                return None

            #if variable.data_type != i.type:
             #   self.add_comment('Error en declaracion de variable')
              #  return None


    def visit_else(self, i: ElseState):
        self.symbol_table = TableC3d(self.symbol_table)
        self.symbol_table.break_lbl = self.symbol_table.anterior.break_lbl
        self.symbol_table.continue_lbl = self.symbol_table.anterior.continue_lbl
        for instruction in i.bloque:
            instruction.accept(self)
        self.symbol_table = self.symbol_table.anterior

    def visit_foreach(self, i: ForEachState):
        pass

    def visit_for(self, i: ForState):
        self.symbol_table = TableC3d(self.symbol_table)
        i.declaration.accept(self)
        loop_label = self.new_label()
        self.put_label(loop_label)

        left = ''
        right = ''
        op = ''

        if i.condition.left_operator is not None:
            left = i.condition.left_operator.accept(self)

        if i.condition.right_operator is not None:
            right = i.condition.right_operator.accept(self)

        if i.condition.operator is not None:
            op = i.condition.op_value()

        true_label = self.new_label()

        self.add_if(left.value, right.value, op, true_label)
        false_label = self.new_label()
        self.add_goto(false_label)

        self.put_label(true_label)
        self.symbol_table.break_lbl = false_label
        self.symbol_table.continue_lbl = loop_label
        for instruction in i.instructions:
            instruction.accept(self)
        i.increment.accept(self)
        self.add_goto(loop_label)
        self.put_label(false_label)
        self.symbol_table = self.symbol_table.anterior

    def visit_function(self, i: FunctionState):
        pass

    def visit_if(self, i: IfState):
        left = ''
        right = ''
        op = ''

        if i.condition.left_operator is not None:
            left = i.condition.left_operator.accept(self)

        if i.condition.right_operator is not None:
            right = i.condition.right_operator.accept(self)

        if i.condition.operator is not None:
            op = i.condition.op_value()

        true_label = self.new_label()

        self.add_if(left.value, right.value, op,true_label)

        if i.bloque_falso is not None:
            i.bloque_falso.accept(self)

        lbl = self.new_label()
        self.add_goto(lbl)

        self.put_label(true_label)
        self.symbol_table = TableC3d(self.symbol_table)
        self.symbol_table.break_lbl = self.symbol_table.anterior.break_lbl
        self.symbol_table.continue_lbl = self.symbol_table.anterior.continue_lbl
        for instruction in i.bloque_verdadero:
            instruction.accept(self)
        self.put_label(lbl)
        self.symbol_table = self.symbol_table.anterior

    def visit_interface_assign(self, i: InterfaceAssign):
        pass

    def visit_inter_attr_assign(self, i: InterAttributeAssign):
        pass

    def visit_interface(self, i: InterfaceState):
        pass

    def visit_native(self, i: NativeFunction):
        pass

    def visit_only_assign(self, i: OnlyAssignment):
        result = self.symbol_table.get_symbol_by_id(i.id)

        if result is None:
            return None

        val = i.value.accept(self)

        if val.type == VariableType().buscar_type("BOOLEAN"):
            if val.isTemp:
                self.set_stack(result.pos, val.value)
            else:
                value = 1 if val.value is True else 0
                self.set_stack(result.pos, value)

        elif val.type == VariableType().buscar_type("STRING"):
            self.set_stack(result.pos, val.value)
        else:
            self.set_stack(result.pos, val.value)

    def visit_parameter(self, i: Parameter):
        pass

    def visit_return(self, i: Return):
        pass

    def visit_unary_op(self, i: UnaryOperation):
        right = i.right_operator.accept(self)
        if right is None:
            self.add_comment('El operador es nulo')
            return None

        if i.operator == OperationType.NEGATIVE:
            operator = '-'
            temporal = self.add_temp()
            self.add_expression_unary(temporal, right.value, operator)


            return ReturnC3d(temporal, VariableType().buscar_type("NUMBER"), True)


        elif i.operator == OperationType.POSITIVE:
            operator = '+'
            temporal = self.add_temp()
            self.add_expression_unary(temporal, right.value, operator)
            return ReturnC3d(temporal,VariableType().buscar_type("NUMBER"), True)

        elif i.operator == OperationType.NOT:
            if right.data_type != VariableType.lista_variables["BOOLEAN"]:
                # self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (!) UNARIO ENTRE VARIABLE DE TIPO BOOLEAN.", i.line, i.column))
                return None

            # result.data_type = VariableType().buscar_type("BOOLEAN")
            # result.value = not right.value
            # result.symbol_type = SymbolType().VARIABLE
            # result.isAny = False
            # return result

        elif i.operator == OperationType.INCREMENT:
            operator = '+'
            temporal = self.add_temp()
            self.add_expression(temporal, right.value, 1, operator)
            right_symbol = self.symbol_table.get_symbol_by_id(i.right_operator.value)

            self.set_stack(right_symbol.pos, temporal)
            return ReturnC3d(temporal,VariableType().buscar_type("NUMBER"), True)

        elif i.operator == OperationType.DECREMENT:
            operator = '-'
            temporal = self.add_temp()
            self.add_expression(temporal, right.value, 1, operator)
            right_symbol = self.symbol_table.get_symbol_by_id(i.right_operator.value)
            self.set_stack(right_symbol.pos, temporal)

            return ReturnC3d(temporal,VariableType().buscar_type("NUMBER"), True)

    def visit_while(self, i: WhileState):
        loop_label = self.new_label()
        self.put_label(loop_label)
        left = ''
        right = ''
        op = ''

        if i.condition.left_operator is not None:
            left = i.condition.left_operator.accept(self)

        if i.condition.right_operator is not None:
            right = i.condition.right_operator.accept(self)

        if i.condition.operator is not None:
            op = i.condition.op_value()

        true_label = self.new_label()
        self.add_if(left.value, right.value, op, true_label)
        false_label = self.new_label()
        self.add_goto(false_label)

        self.put_label(true_label)
        self.symbol_table = TableC3d(self.symbol_table)
        self.symbol_table.break_lbl = false_label
        self.symbol_table.continue_lbl = loop_label
        for instruction in i.instructions:
            instruction.accept(self)
        self.add_goto(loop_label)
        self.put_label(false_label)
        self.symbol_table = self.symbol_table.anterior

    def visit_value(self, i: Value):
        # tipo=None
        if i.value_type == ValueType.CADENA:
            # tipo= VariableType().buscar_type("STRING")
            temporal = self.add_temp()
            self.add_assig(temporal, 'H')

            for char in str(i.value):
                self.set_heap('H', ord(char))
                self.next_heap()
            self.set_heap('H', -1)
            self.next_heap()

            return ReturnC3d(temporal, VariableType().buscar_type("STRING"), True)

        elif i.value_type == ValueType.ENTERO:
            # tipo= VariableType().buscar_type("NUMBER")
            return ReturnC3d(i.value/1, VariableType().buscar_type("NUMBER"), False)

        elif i.value_type == ValueType.DECIMAL:
            # tipo= VariableType().buscar_type("NUMBER")
            return ReturnC3d(i.value/1, VariableType().buscar_type("NUMBER"), False)
        elif i.value_type == ValueType.BOOLEANO:
            # tipo= VariableType().buscar_type("BOOLEAN")
            return ReturnC3d(True if i.value == "true" else False, VariableType().buscar_type("BOOLEAN"), False)

        elif i.value_type == ValueType.LITERAL:
            var_in_table = self.symbol_table.get_symbol_by_id(str(i.value))
            if var_in_table is None:
                self.add_comment("Variable no encontrada en la tabla de simbolos")
                print("Variable no encontrada en la tabla de simbolos")
                return None

            if var_in_table.type == VariableType().buscar_type("STRING"):
                return ReturnC3d(f'stack[int({var_in_table.pos})]', var_in_table.type, True)

            return ReturnC3d(f'stack[int({var_in_table.pos})]', var_in_table.type, False)

        # return ReturnC3d(str(i.value),tipo, False)

"""
    Creditos: 
        Diego Obin - Repositorio del Curso
        Se utilizo como una base para generador de c3d
        Erick Morales/ Levi Hernandez - Desarrolladores
"""
