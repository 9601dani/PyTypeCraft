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
        pass

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
        pass