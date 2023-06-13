from .Instruction import Instruction


class FunctionState(Instruction):

    def accept(self, visitor):
      return  visitor.visit_function(self)

    def __init__(self, line: int, column: int, id: str, isInTable: bool, parameters: [Instruction], instructions: [Instruction]):
        super().__init__(line, column)
        self.id = id
        self.isInTable = isInTable
        self.parameters = parameters
        self.instructions = instructions

    def __str__(self):
        return f"""{{"FunctionState": {self.id} {self.parameters} {self.instructions}}}"""
