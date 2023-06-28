from .Instruction import Instruction


class ArrayState(Instruction):

    def node_name(self):
        return f'array_stmt_{self.line}_{self.column}'

    def node_value(self):
        return f'array_statement'

    def vals_name(self):
        return f'values_{self.line}_{self.column}'

    def vals_value(self):
        return f'values'

    def accept(self, visitor):
        return visitor.visit_array_state(self)

    def __init__(self, line: int, column: int, values: [Instruction]):
        super().__init__(line, column)
        self.values = values
