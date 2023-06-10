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
from ..models import NativeFunction
from ..models import OnlyAssignment
from ..models import Return
from ..models import UnaryOperation
from ..models import WhileState
from ..models import Value


class DebugRun(Visitor):

    def visit(self, i: Assignment):
        pass

    def visit(self, i: BinaryOperation):
        pass

    def visit(self, i: Break):
        pass

    def visit(self, i: CallFunction):
        pass

    def visit(self, i: ConsoleLog):
        pass

    def visit(self, i: Continue):
        pass

    def visit(self, i: Declaration):
        pass

    def visit(self, i: ElseState):
        pass

    def visit(self, i: ForEachState):
        pass

    def visit(self, i: ForState):
        pass

    def visit(self, i: FunctionState):
        pass

    def visit(self, i: IfState):
        pass

    def visit(self, i: InterfaceState):
        pass

    def visit(self, i: NativeFunction):
        pass

    def visit(self, i: OnlyAssignment):
        pass

    def visit(self, i: Return):
        pass

    def visit(self, i: UnaryOperation):
        pass

    def visit(self, i: WhileState):
        pass

    def visit(self, i: Value):
        pass
