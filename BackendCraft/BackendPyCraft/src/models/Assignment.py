from .Instruction import Instruction


class Assignment(Instruction):
    def node_name(self):
        return f'assignment_{self.line}_{self.column}'

    def node_value(self):
        return f'assignment'

    def id_name(self):
        return f'id_{self.line}_{self.column}'

    def id_value(self):
        return f'{self.id}'

    def type_name(self):
        return f'type_{self.line}_{self.column}'

    def type_value(self):
        return f'{self.type}'

    def accept(self, visitor):
        return visitor.visit_assignment(self)

    def __init__(self, line, column, id, type,value: Instruction, isAny):
        super().__init__(line, column)
        self.id = id
        self.type = type
        self.value = value
        self.isAny= isAny
        
    def __str__(self):
        return f"""{{"Assignment": {self.id}, {self.type}, {self.value.__str__()}, {self.isAny}}}"""
