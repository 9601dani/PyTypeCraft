from .Visitor import Visitor
from ..models import Value, WhileState, UnaryOperation, Return, Parameter, OnlyAssignment, NativeFunction, \
    InterfaceState, InterAttributeAssign, InterfaceAssign, IfState, FunctionState, ForState, ForEachState, ElseState, \
    Declaration, Continue, ConsoleLog, CallFunction, CallAttribute, CallArray, Break, BinaryOperation, ArrayState, \
    Assignment, ArrayAssign


class CstDrawer(Visitor):

    def visit_array_assign(self, i: ArrayAssign):
        return ""

    def visit_assignment(self, i: Assignment):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content = content + f'{i.id_name()} [label = "{i.id_value()}"]\n'
        content = content + f'{i.node_name()} -> {i.id_name()}\n\n'

        if i.type is not None:
            content = content + f'{i.type_name()} [label = "{i.type_value()}"]\n'
            content = content + f'{i.node_name()} -> {i.type_name()}\n\n'

        if i.value is not None:
            content = content + f'{i.node_name()} -> {i.value.node_name()}\n'
            content = content + i.value.accept(self)

        return content

    def visit_array_state(self, i: ArrayState):
        return ""

    def visit_binary_op(self, i: BinaryOperation):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content = content + f'{i.left_name()} [label = "{i.left_value()}"]\n'
        content = content + f'{i.node_name()} -> {i.left_name()}\n\n'
        content = content + f'{i.left_name()} -> {i.left_operator.node_name()}\n'
        content = content + i.left_operator.accept(self)

        content = content + f'{i.op_name()} [label = "{i.op_value()}"]\n'
        content = content + f'{i.node_name()} -> {i.op_name()}\n\n'

        content = content + f'{i.right_name()} [label = "{i.right_value()}"]\n'
        content = content + f'{i.node_name()} -> {i.right_name()}\n\n'
        content = content + f'{i.right_name()} -> {i.right_operator.node_name()}\n'

        content = content + i.right_operator.accept(self)

        return content

    def visit_break(self, i: Break):
        return ""

    def visit_call_arr(self, i: CallArray):
        return ""

    def visit_call_attr(self, i: CallAttribute):
        return ""

    def visit_call_fun(self, i: CallFunction):
        return ""

    def visit_console(self, i: ConsoleLog):
        return ""

    def visit_continue(self, i: Continue):
        return ""

    def visit_declaration(self, i: Declaration):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content = content + f'{i.let_name()} [label = "{i.let_value()}"]\n'
        content = content + f'{i.node_name()} -> {i.let_name()}\n\n'
        content = content + f'{i.assign_name()} [label = "{i.assign_value()}"]\n'
        content = content + f'{i.node_name()} -> {i.assign_name()}\n\n'

        for instruction in i.instructions:
            content = content + f'{i.assign_name()} -> {instruction.node_name()}\n'
            content = content + instruction.accept(self)

        return content

    def visit_else(self, i: ElseState):
        return ""

    def visit_foreach(self, i: ForEachState):
        return ""


    def visit_for(self, i: ForState):
        return ""


    def visit_function(self, i: FunctionState):
        return ""


    def visit_if(self, i: IfState):
        return ""


    def visit_interface_assign(self, i: InterfaceAssign):
        return ""


    def visit_inter_attr_assign(self, i: InterAttributeAssign):
        return ""


    def visit_interface(self, i: InterfaceState):
        return ""


    def visit_native(self, i: NativeFunction):
        return ""


    def visit_only_assign(self, i: OnlyAssignment):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content = content + f'{i.id_name()} [label = "{i.id_value()}"]\n'
        content = content + f'{i.node_name()} -> {i.id_name()}\n\n'

        content = content + f'{i.equals_name()} [label = "{i.equals_value()}"]\n'
        content = content + f'{i.node_name()} -> {i.equals_name()}\n\n'

        content = content + f'{i.node_name()} -> {i.value.node_name()}\n\n'

        content = content + i.value.accept(self)

        return content

    def visit_parameter(self, i: Parameter):
        return ""


    def visit_return(self, i: Return):
        return ""


    def visit_unary_op(self, i: UnaryOperation):
        return ""


    def visit_while(self, i: WhileState):
        return ""


    def visit_value(self, i: Value):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content = content + f'{i.child_name()} [label ="{i.child_value()}"]\n'
        content = content + f'{i.node_name()} -> {i.child_name()}\n\n'

        return content
