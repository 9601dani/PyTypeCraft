from .Instruction import Instruction


class UnaryOperation(Instruction):
    def accept(self, visitor):
        pass

    def __init__(self, line, column, right_operator, operator):
        super().__init__(line, column)
        self.right_operator = right_operator
        self.operator = operator

    def __str__(self):
        return f"""{{"UnaryOperation": {self.operator} {self.right_operator}}}"""