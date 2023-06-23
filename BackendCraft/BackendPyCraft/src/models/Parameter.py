from .Instruction import Instruction


class Parameter(Instruction):

    def node_name(self):
        return f'param_{self.line}_{self.column}'

    def node_value(self):
        return f'parameter'

    def id_name(self):
        return f'id_{self.line}_{self.column}'

    def id_value(self):
        return f'{self.id}'

    def type_name(self):
        return f'type_{self.line}_{self.column}'

    def type_value(self):
        return f'{self.type}'

    def accept(self, visitor):
       return visitor.visit_parameter(self)

    def __init__(self, line: int, column: int, id, variable_type, isAny):
        super().__init__(line, column)
        self.id = id
        self.type = variable_type
        self.isAny = isAny



