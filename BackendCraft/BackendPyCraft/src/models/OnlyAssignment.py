from .Instruction import Instruction
from .VariableType import VariableType
class OnlyAssignment (Instruction):
    def accept(self, visitor):
        visitor.visit(self)

    def __init__(self, line, column, id, type,value: Instruction):
        super().__init__(line, column)
        self.id = id
        self.type = type
        self.value = value

    def __str__(self):
        return f"""{{"OnlyAssignment": {self.id}, {self.type}, {self.value.__str__()}}}"""