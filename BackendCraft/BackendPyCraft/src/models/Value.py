from .Instruction import Instruction


class Value(Instruction):
    def node_name(self):
        return f'value_{self.line}_{self.column}'

    def node_value(self):
        return "value"

    def child_name(self):
        return f'child_{self.line}_{self.column}'

    def child_value(self):
        return f'{self.value}'

    def __init__(self, line, column, value, value_type):
        super().__init__(line, column)
        self.value = value
        self.value_type = value_type

    def accept(self, visitor):
        return visitor.visit_value(self)

    def __str__(self):
        return f"""{{"Value": {self.value}, {self.value_type}}}"""