from .Instruction import Instruction


class WhileState(Instruction):
    def accept(self, visitor):
        visitor.visit_while(self)

    def __init__(self, line: int, column: int, condition: Instruction, instructions: [Instruction]):
        super().__init__(line, column)
        self.condition = condition
        self.instructions = instructions

    def __str__(self):
        return f"""{{"WhileState": {self.condition} {self.instructions.__str__()}}}"""
