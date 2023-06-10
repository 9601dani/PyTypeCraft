from abc import ABC, abstractmethod
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


class Visitor(ABC):
    @abstractmethod
    def visit(self, i: Assignment):
        pass

    @abstractmethod
    def visit(self, i: BinaryOperation):
        pass

    @abstractmethod
    def visit(self, i: Break):
        pass

    @abstractmethod
    def visit(self, i: CallFunction):
        pass

    @abstractmethod
    def visit(self, i: ConsoleLog):
        pass

    @abstractmethod
    def visit(self, i: Continue):
        pass

    @abstractmethod
    def visit(self, i: Declaration):
        pass

    @abstractmethod
    def visit(self, i: ElseState):
        pass

    @abstractmethod
    def visit(self, i: ForEachState):
        pass

    @abstractmethod
    def visit(self, i: ForState):
        pass

    @abstractmethod
    def visit(self, i: FunctionState):
        pass

    @abstractmethod
    def visit(self, i: IfState):
        pass

    @abstractmethod
    def visit(self, i: InterfaceState):
        pass

    @abstractmethod
    def visit(self, i: NativeFunction):
        pass

    @abstractmethod
    def visit(self, i: OnlyAssignment):
        pass

    @abstractmethod
    def visit(self, i: Return):
        pass

    @abstractmethod
    def visit(self, i: UnaryOperation):
        pass

    @abstractmethod
    def visit(self, i: WhileState):
        pass

    @abstractmethod
    def visit(self, i: Value):
        pass