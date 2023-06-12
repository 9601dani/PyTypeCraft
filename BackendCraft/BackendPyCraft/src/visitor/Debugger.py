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


class Debugger(Visitor):

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
        print("console debug")

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
        print("value debug")
