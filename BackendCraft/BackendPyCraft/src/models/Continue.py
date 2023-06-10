from .Instruction import Instruction


class Continue(Instruction):
    def accept(self, visitor):
        visitor.visit(self)

    def __init__(self, line, column):
        super().__init__(line, column)

    def __str__(self):
        return f"""{{"Continue": }}"""
