from .Instruction import Instruction


class CallArray(Instruction):
    def node_name(self):
        return f'call_array_{self.line}_{self.column}'

    def node_value(self):
        return f'call_array'

    def id_name(self):
        return f'id_{self.line}_{self.column}'

    def id_value(self):
        return f'{self.id}'

    def dim_name(self):
        return f'dim_{self.line}_{self.column}'

    def dim_value(self):
        return f'dimensions'

    def accept(self, visitor):
        return  visitor.visit_call_arr(self)

    def __init__(self, line: int, column: int, id: str, dimensions: [Instruction]):
        super().__init__(line, column)
        self.id = id
        self.dimensions = dimensions
