from .Instruction import Instruction
from .VariableType import VariableType
class Assignment (Instruction):
    def accept(self, visitor):
        pass

    def __init__(self, line, column, id, type,value: Instruction, isAny):
        super().__init__(line, column)
        self.id = id
        self.type = type
        self.value = value
        self.isAny= isAny