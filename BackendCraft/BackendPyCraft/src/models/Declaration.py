from .Instruction import Instruction
class Declaration (Instruction):

    def accept(self, visitor):
        visitor.visit(self)

    def __init__(self, line: int, column: int, type: str, instructions: [Instruction]):
        super().__init__(line, column)
        self.type = type
        self.instructions = instructions

    def __str__(self):
        return f"""{{"Declaration": {self.type}, {self.instructions.__str__()}}}"""