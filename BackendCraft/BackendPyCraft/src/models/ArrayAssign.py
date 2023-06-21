from .Instruction import Instruction


class ArrayAssign(Instruction):
    def node_name(self):
        pass

    def node_value(self):
        pass

    def accept(self, visitor):
        return visitor.visit_array_assign(self)

    def __init__(self, line: int, column: int, id: str, dimensions: [Instruction], value: Instruction):
        super().__init__(line, column)
        self.id = id
        self.dimensions = dimensions
        self.value = value
