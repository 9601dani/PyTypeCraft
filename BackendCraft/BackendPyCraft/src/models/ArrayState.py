from .Instruction import Instruction


class ArrayState(Instruction):

    def accept(self, visitor):
        return visitor.visit_array_state(self)

    def __init__(self, line: int, column: int, values: [Instruction]):
        super().__init__(line, column)
        self.values = values