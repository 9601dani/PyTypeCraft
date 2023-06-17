from .Visitor import Visitor
from ..models import Value, WhileState, UnaryOperation, Return, Parameter, OnlyAssignment, NativeFunction, \
    InterfaceState, InterAttributeAssign, InterfaceAssign, IfState, FunctionState, ForState, ForEachState, ElseState, \
    Declaration, Continue, ConsoleLog, CallFunction, CallAttribute, CallArray, Break, BinaryOperation, ArrayState, \
    Assignment


class CstDrawer(Visitor):
    def visit_assignment(self, i: Assignment):
        pass

    def visit_array_state(self, i: ArrayState):
        pass

    def visit_binary_op(self, i: BinaryOperation):
        pass

    def visit_break(self, i: Break):
        pass

    def visit_call_arr(self, i: CallArray):
        pass

    def visit_call_attr(self, i: CallAttribute):
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
        pass