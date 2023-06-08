from abc import ABC

from .Instruction import Instruction


class BinaryOperation(Instruction):
    def accept(self, visitor):
        pass

    def __init__(self, line, column, left_operator, right_operator, operator):
        super().__init__(line, column)
        self.left_operator = left_operator
        self.right_operator = right_operator
        self.operator = operator

    def __str__(self):
        return f"""{{"BinaryOperation": {self.left_operator} {self.operator} {self.right_operator}}}"""