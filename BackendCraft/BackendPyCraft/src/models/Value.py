from .Instruction import Instruction


class Value(Instruction):
    def __init__(self, line, column, value, value_type):
        super().__init__(line, column)
        self.value = value
        self.type = value_type

    def accept(self, visitor):
        pass
