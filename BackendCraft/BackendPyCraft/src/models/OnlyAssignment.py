from .Instruction import Instruction
from .VariableType import VariableType
class OnlyAssignment (Instruction):
    def accept(self, visitor):
        pass

    def __init__(self, line, column, id, type: VariableType,value: Instruction):
        super().__init__(line, column)
        self.id = id
        self.type = type
        self.value = value