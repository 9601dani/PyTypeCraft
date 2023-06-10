from .Instruction import Instruction


class ForState(Instruction):

    def accept(self, visitor):
        visitor.visit(self)

    def __init__(self, line: int,
                 column: int,
                 declaration: Instruction,
                 condition: Instruction,
                 increment: Instruction,
                 instructions: [Instruction]):
        super().__init__(line, column)
        self.declaration = declaration
        self.condition = condition
        self.increment = increment
        self.instructions = instructions

    def __str__(self):
        return f"""{{"ForState": {self.declaration} {self.condition} {self.increment} {self.instructions}}}"""