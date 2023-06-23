import imp

from .Instruction import Instruction


class OnlyAssignment(Instruction):
    def node_name(self):
        return f'only_assign_{self.line}_{self.column}'

    def node_value(self):
        return f'assignment'

    def id_name(self):
        return f'id_{self.line}_{self.column}'

    def id_value(self):
        return f'{self.id}'

    def equals_name(self):
        return f'eq_{self.line}_{self.column}'

    def equals_value(self):
        return f'='

    def accept(self, visitor):
        return visitor.visit_only_assign(self)

    def __init__(self, line, column, id, type,value: Instruction):
        super().__init__(line, column)
        self.id = id
        self.type = type
        self.value = value

    def __str__(self):
        return f"""{{"OnlyAssignment": {self.id}, {self.type}, {self.value.__str__()}}}"""
