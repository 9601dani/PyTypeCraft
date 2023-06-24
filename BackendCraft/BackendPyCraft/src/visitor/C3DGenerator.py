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
import copy
from decimal import Decimal


class C3DGenerator(Visitor):
    def __init__(self, symbol_table: SymbolTable):
        #### Tabla de simbolos ####
        self.symbol_table = symbol_table
        #### Contadores C3D ####
        self.contadores_tmp = 0
        self.contadores_etiquetas = 0
        self.lista_tmp = []
        self.lista_nativas = []
        #### manejadores del texto final ####
        self.header = ""
        self.code = ""
        self.footer = ""
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
    ###### METODOS CODIGO 3D ########
    def set_import(self, lib):
        if lib in self.imports_default:
            self.imports_default.remove(lib)
        else:
            return

        self.imports.append(f'"{lib}"\n')

    #### CODIGO ####
    def get_header(self):
        code= '/*------HEADER------*/\n package main;\n\n'
        code+= 'import(\n'
        if len(self.imports) > 0:
            for temp in self.imports:
                code += temp
        code += ')\n'
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
        return f'{self.get_header()}\n func main() {{\n{self.code}\n}}'

    def add_comment(self, comment):
        self.code += f'/* {comment} */\n'

    def add_space(self):
        self.code += '\n'

    ##### MANAGE TMP #####
    def add_temp(self):
        temp = f't{self.contadores_tmp}'
        self.contadores_tmp += 1
        self.lista_tmp.append(temp)
        return temp

    # MANAGE ETIQUETAS  #
    def add_labels(self):
        pass
    # MANAGE GOTO#
    def add_goto(self):
        self.code += f'goto {label};\n'
    # IF#
    ##### EXPRESIONES #####
    def add_expression(self, result, left, right, op):
        self.code += f'{result} = {left} {op} {right};\n'

    def add_expression_unary(self, result, left, op):
        self.code += f'{result} = {op} {left};\n'

    def add_assig(self, result, left):
        self.code += f'{result} = {left};\n'
    ##### MANAGE STACK #####
    def add_stack(self, pos, value):
        self.code += f'stack[int({pos})] = {value};\n'

    def get_stack(self, place, pos):
        self.code += f'{place} = stack[int({pos})];\n'
    ###### MANAGE ENVIROMENT ######
    def new_env(self, size):
        self.code += '/*------NUEVO ENTORNO------*/\n'
        self.code += f'P = P + {size};\n'

    def ret_env(self, size):
        self.code += '/*------RETORNO ENTORNO------*/\n'
        self.code += f'P = P - {size};\n'

    def call_fun(self, id):
        self.code += f'/*------LLAMADA A FUNCION------*/\n'
        self.code += f'{id}();\n'
    ###### MANAGE HEAP ######
    def add_heap(self, pos, value):
        self.code += f'heap[int({pos})] = {value};\n'

    def get_heap(self, place, pos):
        #TODO: SE CONVIERTE A INT PORQUE ES EL INDICE DEL HEAP, PERO VIENE FLOAT ENTONCES SE CONVIERTE A INT
        self.code += f'{place} = heap[int({pos})];\n'
    ##### NEXT HEAP #####
    def next_heap(self):
        self.code += f'H = H + 1;\n'

    ##### INSTRUCCIONES #####
    def add_if(self, condition, label):
        self.code += f'if {condition} goto {label};\n'

    def add_print(self,type, value):
        self.code += f'/*------PRINT------*/\n'
        self.set_import('fmt')
        self.code += f'fmt.Printf("%{type}", {value});\n'



    ############################################# METODOS VISIT #############################################
    def visit_array_assign(self, i: ArrayAssign):
        pass

    def visit_assignment(self, i: Assignment):
        pass

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
        elif i.operator == OperationType.DIVISION:
            operator = '/'
            temporal = self.add_temp()
            self.add_expression(temporal, left.value, right.value, operator)
            return ReturnC3d(temporal,VariableType().buscar_type("NUMBER"), True)
        #TODO: FALTAN DEMAS OPERACIONES


    def visit_break(self, i: Break):
        pass

    def visit_call_arr(self, i: CallArray):
        pass

    def visit_call_attr(self, i: CallAttribute):
        pass

    def visit_call_fun(self, i: CallFunction):
        pass

    def visit_console(self, i: ConsoleLog):
        for val in i.value:
            result: ReturnC3d = val.accept(self)
            if result.get_tipo() == VariableType().buscar_type("NUMBER"):
                self.add_print('f', result.value)
            elif result.get_tipo() == VariableType().buscar_type("STRING"):
                self.add_print('s', result.value)
            elif result.get_tipo() == VariableType().buscar_type("BOOLEAN"):
                self.add_print('t', result.value)
            #TODO: FALTAN DEMAS TIPOS

    def visit_continue(self, i: Continue):
        pass

    def visit_declaration(self, i: Declaration):
        pass

    def visit_else(self, i: ElseState):
        pass

    def visit_foreach(self, i: ForEachState):
        pass

    def visit_for(self, i: ForState):
        pass

    def visit_function(self, i: FunctionState):
        pass

    def visit_if(self, i: IfState):
        pass

    def visit_interface_assign(self, i: InterfaceAssign):
        pass

    def visit_inter_attr_assign(self, i: InterAttributeAssign):
        pass

    def visit_interface(self, i: InterfaceState):
        pass

    def visit_native(self, i: NativeFunction):
        pass

    def visit_only_assign(self, i: OnlyAssignment):
        pass

    def visit_parameter(self, i: Parameter):
        pass

    def visit_return(self, i: Return):
        pass

    def visit_unary_op(self, i: UnaryOperation):
        pass

    def visit_while(self, i: WhileState):
        pass

    def visit_value(self, i: Value):
        return ReturnC3d(str(i.value),i.value_type, False)


