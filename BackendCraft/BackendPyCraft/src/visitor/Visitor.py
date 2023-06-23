from abc import ABC, abstractmethod
from ..models import ArrayAssign
from ..models import Assignment
from ..models import ArrayState
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
from ..models import Parameter


class Visitor(ABC):

    def __init__(self):
        print("")

    @abstractmethod
    def visit_assignment(self, i: Assignment):
        pass

    @abstractmethod
    def visit_array_assign(self, i: ArrayAssign):
        pass

    @abstractmethod
    def visit_array_state(self, i: ArrayState):
        pass

    @abstractmethod
    def visit_binary_op(self, i: BinaryOperation):
        pass

    @abstractmethod
    def visit_break(self, i: Break):
        pass

    @abstractmethod
    def visit_call_arr(self, i: CallArray):
        pass

    @abstractmethod
    def visit_call_attr(self, i: CallAttribute):
        pass

    @abstractmethod
    def visit_call_fun(self, i: CallFunction):
        pass

    @abstractmethod
    def visit_console(self, i: ConsoleLog):
        pass

    @abstractmethod
    def visit_continue(self, i: Continue):
        pass

    @abstractmethod
    def visit_declaration(self, i: Declaration):
        pass

    @abstractmethod
    def visit_else(self, i: ElseState):
        pass

    @abstractmethod
    def visit_foreach(self, i: ForEachState):
        pass

    @abstractmethod
    def visit_for(self, i: ForState):
        pass

    @abstractmethod
    def visit_function(self, i: FunctionState):
        pass

    @abstractmethod
    def visit_if(self, i: IfState):
        pass

    @abstractmethod
    def visit_interface_assign(self, i: InterfaceAssign):
        pass

    @abstractmethod
    def visit_inter_attr_assign(self, i: InterAttributeAssign):
        pass

    @abstractmethod
    def visit_interface(self, i: InterfaceState):
        pass

    @abstractmethod
    def visit_native(self, i: NativeFunction):
        pass

    @abstractmethod
    def visit_only_assign(self, i: OnlyAssignment):
        pass

    @abstractmethod
    def visit_parameter(self, i: Parameter):
        pass

    @abstractmethod
    def visit_return(self, i: Return):
        pass

    @abstractmethod
    def visit_unary_op(self, i: UnaryOperation):
        pass

    @abstractmethod
    def visit_while(self, i: WhileState):
        pass

    @abstractmethod
    def visit_value(self, i: Value):
        pass