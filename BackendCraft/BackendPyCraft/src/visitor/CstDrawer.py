from .Visitor import Visitor
from ..models import Value, WhileState, UnaryOperation, Return, Parameter, OnlyAssignment, NativeFunction, \
    InterfaceState, InterAttributeAssign, InterfaceAssign, IfState, FunctionState, ForState, ForEachState, ElseState, \
    Declaration, Continue, ConsoleLog, CallFunction, CallAttribute, CallArray, Break, BinaryOperation, ArrayState, \
    Assignment, ArrayAssign


class CstDrawer(Visitor):

    def visit_array_assign(self, i: ArrayAssign):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content += f'{i.call_name()} [label = "{i.call_value()}"]\n'
        content += f'{i.id_name()} [label = "{i.id_value()}"]\n'
        content += f'{i.dim_name()} [label = "{i.dim_value()}"]\n'
        content += f'{i.equals_name()} [label = "{i.equals_value()}"]\n'
        content += f'{i.node_name()} -> {i.call_name()}\n\n'
        content += f'{i.node_name()} -> {i.equals_name()}\n\n'
        content += f'{i.call_name()} -> {i.id_name()}\n\n'
        content += f'{i.call_name()} -> {i.dim_name()}\n\n'

        for dimension in i.dimensions:
            content += f'{i.dim_name()} -> {dimension.node_name()}\n\n'
            content += dimension.accept(self)

        content += f'{i.node_name()} -> {i.value.node_name()}\n\n'
        content += i.value.accept(self)

        return content

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
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content += f'{i.vals_name()} [label = "{i.vals_value()}"]\n'

        content += f'{i.node_name()} -> {i.vals_name()}\n\n'


        for value in i.values:
            content += f'{i.vals_name()} -> {value.node_name()}\n\n'
            content += value.accept(self)

        return content

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
        return f'{i.node_name()} [label = "{i.node_value()}"]\n'

    def visit_call_arr(self, i: CallArray):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content += f'{i.id_name()} [label = "{i.id_value()}"]\n'
        content += f'{i.dim_name()} [label = "{i.dim_value()}"]\n'
        content += f'{i.node_name()} -> {i.id_name()}\n\n'
        content += f'{i.node_name()} -> {i.dim_name()}\n\n'

        for dimension in i.dimensions:
            content += f'{i.dim_name()} -> {dimension.node_name()}\n\n'
            content += dimension.accept(self)

        return content

    def visit_call_attr(self, i: CallAttribute):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content += f'{i.id_name()} [label = "{i.id_value()}"]\n'
        content += f'{i.node_name()} -> {i.id_name()}\n\n'

        content += f'{i.id_name()} -> {i.id.node_name()}\n\n'
        content += i.id.accept(self)

        content += f'{i.attr_name()} [label = "{i.attr_value()}"]\n'
        content += f'{i.node_name()} -> {i.attr_name()}\n\n'

        return content

    def visit_call_fun(self, i: CallFunction):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content += f'{i.id_name()} [label = "{i.id_value()}"]\n'
        content += f'{i.node_name()} -> {i.id_name()}\n\n'

        if len(i.assignments) > 0:
            content += f'{i.args_name()} [label = "{i.args_value()}"]\n'
            content += f'{i.node_name()} -> {i.args_name()}\n\n'

            for assignment in i.assignments:
                content += f'{i.args_name()} -> {assignment.node_name()}\n\n'
                content += assignment.accept(self)

        return content

    def visit_console(self, i: ConsoleLog):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content += f'{i.content_name()} [label = "{i.content_value()}"]\n'
        content += f'{i.node_name()} -> {i.content_name()}\n\n'

        for instruction in i.value:
            content += f'{i.content_name()} -> {instruction.node_name()}\n\n'
            content += instruction.accept(self)

        return content

    def visit_continue(self, i: Continue):
        return f'{i.node_name()} [label = "{i.node_value()}"]\n'

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
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'

        for instruction in i.bloque:
            content = content + f'{i.node_name()} -> {instruction.node_name()}\n\n'
            content = content + instruction.accept(self)

        return content

    def visit_foreach(self, i: ForEachState):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content += f'{i.id_name()} [label = "{i.id_value()}"]\n'
        content += f'{i.of_name()} [label = "{i.of_value()}"]\n'
        content += f'{i.assign_name()} [label = "{i.assign_value()}"]\n'
        content += f'{i.body_name()} [label = "{i.body_value()}"]\n'
        content += f'{i.node_name()} -> {i.id_name()}\n\n'
        content += f'{i.node_name()} -> {i.of_name()}\n\n'
        content += f'{i.node_name()} -> {i.assign_name()}\n\n'
        content += f'{i.node_name()} -> {i.body_name()}\n\n'

        content += f'{i.assign_name()} -> {i.assignment.node_name()}\n\n'
        content += i.assignment.accept(self)

        for instruction in i.instructions:
            content += f'{i.body_name()} -> {instruction.node_name()}\n\n'
            content += instruction.accept(self)

        return content

    def visit_for(self, i: ForState):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content += f'{i.dec_name()} [label = "{i.dec_value()}"]\n'
        content += f'{i.con_name()} [label = "{i.con_value()}"]\n'
        content += f'{i.inc_name()} [label = "{i.inc_value()}"]\n'
        content += f'{i.body_name()} [label = "{i.body_value()}"]\n'
        content += f'{i.node_name()} -> {i.dec_name()}\n\n'
        content += f'{i.node_name()} -> {i.con_name()}\n\n'
        content += f'{i.node_name()} -> {i.inc_name()}\n\n'
        content += f'{i.node_name()} -> {i.body_name()}\n\n'
        content += f'{i.dec_name()} -> {i.declaration.node_name()}\n\n'
        content += f'{i.con_name()} -> {i.condition.node_name()}\n\n'
        content += f'{i.inc_name()} -> {i.increment.node_name()}\n\n'

        content += i.declaration.accept(self)
        content += i.condition.accept(self)
        content += i.increment.accept(self)

        for instruction in i.instructions:
            content += f'{i.body_name()} -> {instruction.node_name()}\n\n'
            content += instruction.accept(self)

        return content

    def visit_function(self, i: FunctionState):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'

        content += f'{i.id_name()} [label = "{i.id_value()}"]\n'
        content += f'{i.node_name()} -> {i.id_name()}\n\n'

        if i.parameters is not None:
            content += f'{i.params_name()} [label = "{i.params_value()}"]\n'
            content += f'{i.node_name()} -> {i.params_name()}\n\n'

            for param in i.parameters:
                content += f'{i.params_name()} -> {param.node_name()}\n\n'
                content += param.accept(self)

        if i.return_type is not None:
            content += f'{i.return_name()} [label = "{i.return_value()}"]\n'
            content += f'{i.node_name()} -> {i.return_name()}\n\n'

        content += f'{i.body_name()} [label = "{i.body_value()}"]\n'
        content += f'{i.node_name()} -> {i.body_name()}\n\n'

        for instruction in i.instructions:
            content += f'{i.body_name()} -> {instruction.node_name()}\n\n'
            content += instruction.accept(self)

        return content

    def visit_if(self, i: IfState):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content = content + f'{i.condition_name()} [label = "{i.condition_value()}"]\n'
        content = content + f'{i.node_name()} -> {i.condition_name()}\n\n'

        content = content + f'{i.condition_name()} -> {i.condition.node_name()}\n\n'

        content = content + i.condition.accept(self)

        content = content + f'{i.true_name()} [label = "{i.true_value()}"]\n'
        content = content + f'{i.node_name()} -> {i.true_name()}\n\n'

        for instruction in i.bloque_verdadero:
            content = content + f'{i.true_name()} -> {instruction.node_name()}\n\n'
            content = content + instruction.accept(self)

        if i.bloque_falso is not None:
            content = content + f'{i.false_name()} [label = "{i.false_value()}"]\n'
            content = content + f'{i.node_name()} -> {i.false_name()}\n\n'
            content = content + f'{i.false_name()} -> {i.bloque_falso.node_name()}\n\n'
            content = content + i.bloque_falso.accept(self)

        return content

    def visit_interface_assign(self, i: InterfaceAssign):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content += f'{i.attrs_name()} [label = "{i.attrs_value()}"]\n'
        content += f'{i.node_name()} -> {i.attrs_name()}\n\n'

        for attribute in i.attributes:
            content += f'{i.attrs_name()} -> {attribute.node_name()}\n\n'
            content += attribute.accept(self)

        return content

    def visit_inter_attr_assign(self, i: InterAttributeAssign):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content += f'{i.node_name()} -> {i.interAttribute.node_name()}\n\n'
        content += i.interAttribute.accept(self)

        content += f'{i.equals_name()} [label = "{i.equals_value()}"]\n'
        content += f'{i.node_name()} -> {i.equals_name()}\n\n'

        content += f'{i.node_name()} -> {i.value.node_name()}\n\n'
        content += i.value.accept(self)

        return content

    def visit_interface(self, i: InterfaceState):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content += f'{i.id_name()} [label = "{i.id_value()}"]\n'
        content += f'{i.node_name()} -> {i.id_name()}\n\n'

        content += f'{i.attrs_name()} [label = "{i.attrs_value()}"]\n'
        content += f'{i.node_name()} -> {i.attrs_name()}\n\n'
        for attribute in i.attributes:
            content += f'{i.attrs_name()} -> {attribute.node_name()}\n\n'
            content += attribute.accept(self)

        return content

    def visit_native(self, i: NativeFunction):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content += f'{i.var_name()} [label = "{i.var_value()}"]\n'
        content += f'{i.node_name()} -> {i.var_name()}\n\n'
        content += f'{i.var_name()} -> {i.variable.node_name()}\n\n'
        content += i.variable.accept(self)
        content += f'{i.native_name()} [label = "{i.native_value()}"]\n'
        content += f'{i.node_name()} -> {i.native_name()}\n\n'

        if len(i.parameter) > 0:
            content += f'{i.arg_name()} [label = "{i.arg_value()}"]\n'
            content += f'{i.node_name()} -> {i.arg_name()}\n\n'
            content += f'{i.arg_name()} -> {i.parameter[0].node_name()}\n\n'
            content += i.parameter[0].accept(self)

        return content

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
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content += f'{i.id_name()} [label = "{i.id_value()}"]\n'
        content += f'{i.node_name()} -> {i.id_name()}\n\n'

        if i.type is not None:
            content += f'{i.type_name()} [label = "{i.type_value()}"]\n'
            content += f'{i.node_name()} -> {i.type_name()}\n\n'

        return content

    def visit_return(self, i: Return):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        if i.expression is not None:
            content += f'{i.expr_name()} [label = "{i.expr_value()}"]\n'
            content += f'{i.node_name()} -> {i.expr_name()}\n\n'
            content += f'{i.expr_name()} -> {i.expression.node_name()}\n\n'
            content += i.expression.accept(self)

        return content

    def visit_unary_op(self, i: UnaryOperation):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content += f'{i.op_name()} [label = "{i.op_value()}"]\n'
        content += f'{i.node_name()} -> {i.op_name()}\n\n'

        content += f'{i.right_name()} [label = "{i.right_value()}"]\n'
        content += f'{i.node_name()} -> {i.right_name()}\n\n'
        content += f'{i.right_name()} -> {i.right_operator.node_name()}\n\n'
        content += i.right_operator.accept(self)

        return content

    def visit_while(self, i: WhileState):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content = content + f'{i.condition_name()} [label = "{i.condition_value()}"]\n'
        content = content + f'{i.node_name()} -> {i.condition_name()}\n\n'

        content = content + f'{i.condition_name()} -> {i.condition.node_name()}\n\n'

        content = content + i.condition.accept(self)

        content = content + f'{i.body_name()} [label = "{i.body_value()}"]\n'
        content = content + f'{i.node_name()} -> {i.body_name()}\n\n'

        for instruction in i.instructions:
            content = content + f'{i.body_name()} -> {instruction.node_name()}\n\n'
            content = content + instruction.accept(self)

        return content

    def visit_value(self, i: Value):
        content = f'{i.node_name()} [label = "{i.node_value()}"]\n'
        content = content + f'{i.child_name()} [label ="{i.child_value()}"]\n'
        content = content + f'{i.node_name()} -> {i.child_name()}\n\n'

        return content
