from .Instruction import Instruction
from .VariableType import VariableType


class FunctionState(Instruction):

    def node_name(self):
        pass

    def node_value(self):
        pass

    def accept(self, visitor):
      return  visitor.visit_function(self)

    def __init__(self, line: int, column: int, id: str, isInTable: bool, parameters: [Instruction], instructions: [Instruction], return_type):
        super().__init__(line, column)
        self.id = id
        self.isInTable = isInTable
        self.parameters = parameters
        self.instructions = instructions
        self.return_type = return_type

    def __str__(self):
        return f"""{{"FunctionState": {self.id} {self.parameters} {self.instructions}}}"""
