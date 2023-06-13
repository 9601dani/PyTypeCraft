from .Visitor import Visitor
from ..models import Assignment
from ..models import BinaryOperation
from ..models import Break
from ..models import CallFunction
from ..models import ConsoleLog
from ..models import Continue
from ..models import Declaration
from ..models import ElseState
from ..models import ForEachState
from ..models import ForState
from ..models import FunctionState
from ..models import IfState
from ..models import InterfaceState
from ..models import Instruction
from ..models import NativeFunction
from ..models import OnlyAssignment
from ..models import Parameter
from ..models import Return
from ..models import UnaryOperation
from ..models import WhileState
from ..models import Value
from ..models.Variable import Variable
from ..models.SymbolType import SymbolType
from ..symbolTable.SymbolTable import SymbolTable
from ..models.ValueType import ValueType
from ..models.VariableType import VariableType
import copy


class Debugger(Visitor):

    def __init__(self, symbol_table: SymbolTable, errors):
        super().__init__()
        self.symbol_table = symbol_table
        self.errors = errors

    def visit_assignment(self, i: Assignment):
        print("assignment debug")
        if i.value:
            i.value.accept(self)


    def visit_binary_op(self, i: BinaryOperation):
        print("binary debug")

    def visit_break(self, i: Break):
        print("break debug")

    def visit_call_fun(self, i: CallFunction):
        print("callFun debug")

    def visit_console(self, i: ConsoleLog):
        if i.value is None:
            print("ERROR EN CONSOLE LOG NO TIENE VALORES PARA IMPRIMIR.")
            pass

        for value in i.value:
            result = value.accept(self)
            if result is None:
                print("ERROR EN CONSOLE LOG NO TIENE VALORES PARA IMPRIMIR.")


    def visit_continue(self, i: Continue):
        print("continue debug")

    def visit_declaration(self, i: Declaration):
        print("declaration debug")
        for instruction in i.instructions:
            instruction.accept(self)

    def visit_else(self, i: ElseState):
        print("else debug")
        for instruction in i.bloque:
            instruction.accept(self)

    def visit_foreach(self, i: ForEachState):
        print("foreach debug")

    def visit_for(self, i: ForState):
        print("for debug")
        for instruction in i.instructions:
            instruction.accept(self)

    def visit_function(self, i: FunctionState):
        print("function debug")

    def visit_if(self, i: IfState):
        print("if debug")
        for instruction in i.bloque_verdadero:
            instruction.accept(self)

        if i.bloque_falso:
            i.bloque_falso.accept(self)

    def visit_interface(self, i: InterfaceState):
        print("interface debug")

    def visit_native(self, i: NativeFunction):
        print("native debug")

    def visit_only_assign(self, i: OnlyAssignment):
        print("only assig debug")

    def visit_parameter(self, i: Parameter):
        print("parameter debug")

    def visit_return(self, i: Return):
        print("return debug")

    def visit_unary_op(self, i: UnaryOperation):
        print("unary debug")

    def visit_while(self, i: WhileState):
        print("while debug")

    def visit_value(self, i: Value):
        result = Variable()
        if i.value_type == ValueType.CADENA:
            result.data_type = VariableType.buscar_type("STRING")
            result.value = str(i.value)
            return result
        elif i.value_type == ValueType.ENTERO:
            result.data_type = VariableType.buscar_type("NUMBER")
            result.value = int(i.value)
            return result
        elif i.value_type == ValueType.DECIMAL:
            result.data_type = VariableType.buscar_type("NUMBER")
            result.value = float(i.value)
            return result
        elif i.value_type == ValueType.BOOLEANO:
            result.data_type = VariableType.buscar_type("BOOLEAN")
            result.value = bool(i.value)
        elif i.value_type == ValueType.LITERAL:
            var_in_table = self.symbol_table.var_in_table(i.value)
            if var_in_table is None:
                print("NO SE ENCONTRÓ LA VARIABLE: "+i.value+" EN LA TABLA DE SIMBOLOS")
                return None

            result = copy.deepcopy(var_in_table)
            return result




