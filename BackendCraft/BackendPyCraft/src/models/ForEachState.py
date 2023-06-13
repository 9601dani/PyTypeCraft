from .Instruction import Instruction


class ForEachState(Instruction):

    def accept(self, visitor):
       return visitor.visit_foreach(self)

    def __init__(self, line: int, column: int, declaration: Instruction, instructions: [Instruction]):
        super().__init__(line, column)
        self.declaration = declaration
        self.instructions = instructions

    def __str__(self):
        return f"""{{"ForEachState": {self.declaration} {self.instructions}}}"""
