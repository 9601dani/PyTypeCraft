from .Instruction import Instruction


class ArrayAssign(Instruction):
    def node_name(self):
        return f'array_assign_{self.line}_{self.column}'

    def node_value(self):
        return f'assignment'

    def call_name(self):
        return f'call_array_{self.line}_{self.column}'

    def call_value(self):
        return f'call_array'

    def id_name(self):
        return f'id_{self.line}_{self.column}'

    def id_value(self):
        return f'{self.id}'

    def dim_name(self):
        return f'dim_{self.line}_{self.column}'

    def dim_value(self):
        return f'dimensions'

    def equals_name(self):
        return f'eq_{self.line}_{self.column}'

    def equals_value(self):
        return f'='

    def accept(self, visitor):
        return visitor.visit_array_assign(self)

    def __init__(self, line: int, column: int, id: str, dimensions: [Instruction], value: Instruction):
        super().__init__(line, column)
        self.id = id
        self.dimensions = dimensions
        self.value = value
