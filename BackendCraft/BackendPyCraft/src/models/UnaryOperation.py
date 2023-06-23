from .Instruction import Instruction
from .OperationType import OperationType


class UnaryOperation(Instruction):
    def node_name(self):
        return f'unary_{self.line}_{self.column}'

    def node_value(self):
        return f'unary_operation'

    def right_name(self):
        return f'right_{self.line}_{self.column}'

    def right_value(self):
        return f'right'

    def op_name(self):
        return f'op_{self.line}_{self.column}'

    def op_value(self):
        if self.operator == OperationType.NOT:
            return "!"
        elif self.operator == OperationType.INCREMENT:
            return "++"
        elif self.operator == OperationType.DECREMENT:
            return "--"
        elif self.operator == OperationType.POSITIVE:
            return "+"
        elif self.operator == OperationType.NEGATIVE:
            return "-"

    def accept(self, visitor):
       return visitor.visit_unary_op(self)

    def __init__(self, line, column, right_operator, operator):
        super().__init__(line, column)
        self.right_operator = right_operator
        self.operator = operator

    def __str__(self):
        return f"""{{"UnaryOperation": {self.operator} {self.right_operator}}}"""
