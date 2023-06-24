from .Instruction import Instruction


class CallArray(Instruction):
    def node_name(self):
        pass

    def node_value(self):
        pass

    def accept(self, visitor):
        return  visitor.visit_call_arr(self)

    def __init__(self, line: int, column: int, id: str, dimensions: [Instruction]):
        super().__init__(line, column)
        self.id = id
        self.dimensions = dimensions