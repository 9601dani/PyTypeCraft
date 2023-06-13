import copy

from .Visitor import Visitor
from ..models import Assignment, Parameter
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
from ..models import NativeFunction
from ..models import OnlyAssignment
from ..models import Return
from ..models import UnaryOperation
from ..models import WhileState
from ..models import Value
from ..models.Variable import Variable
from ..models.VariableType import VariableType
from ..models.ValueType import ValueType


class Runner(Visitor):

    def __init__(self):
        super().__init__()

    def visit_assignment(self, i: Assignment):
        pass

    def visit_binary_op(self, i: BinaryOperation):
        pass

    def visit_break(self, i: Break):
        pass

    def visit_call_fun(self, i: CallFunction):
        pass

    def visit_console(self, i: ConsoleLog):
        array_datos = []
        if i.value is not None:
            dato: str = ""
            for value in i.value:
                vr = value.accept(self)
                if vr is not None:
                    dato += str(vr.value)
            if dato is not None:
                array_datos.append(dato)
            print(array_datos.__str__())
        else:
            pass
         #AÑADIR ERROR PORQUE EL VALOR DE CONSOLE ES NULL, NO HAY INSTRUCCIONES


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
        variable = Variable()
        if i.value_type == ValueType.CADENA:
            variable.data_type = VariableType().buscar_type("STRING")
            variable.value = str(i.value)
            return variable
        elif i.value_type == ValueType.ENTERO:
            variable.data_type = VariableType().buscar_type("NUMBER")
            variable.value = int(i.value)
            return variable
        elif i.value_type == ValueType.DECIMAL:
            variable.data_type = VariableType().buscar_type("NUMBER")
            variable.value = float(i.value)
            print("retorne numero float")
            return variable
        elif i.value_type == ValueType.BOOLEANO:
            variable.data_type = VariableType().buscar_type("BOOLEAN")
            variable.value = bool(i.value)
            return variable
        elif i.value_type == ValueType.LITERAL:
            var_in_table = self.table.get_variable(i.value)
            if var_in_table is None:
                print("Error: variable no declarada")
                # AÑADIR ERROR
                return None
            variable = copy.deepcopy(var_in_table)
            return variable


