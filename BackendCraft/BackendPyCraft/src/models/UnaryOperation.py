from .Instruction import Instruction


class UnaryOperation(Instruction):
    def node_name(self):
        pass

    def node_value(self):
        pass

    def accept(self, visitor):
       return visitor.visit_unary_op(self)

    def __init__(self, line, column, right_operator, operator):
        super().__init__(line, column)
        self.right_operator = right_operator
        self.operator = operator

    def __str__(self):
        return f"""{{"UnaryOperation": {self.operator} {self.right_operator}}}"""
