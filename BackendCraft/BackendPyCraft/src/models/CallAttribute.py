from ..models.Instruction import Instruction


class CallAttribute(Instruction):

    def node_name(self):
        return f'call_attr_{self.line}_{self.column}'

    def node_value(self):
        return f'call_attribute'

    def id_name(self):
        return f'id_{self.line}_{self.column}'

    def id_value(self):
        return f'id'

    def attr_name(self):
        return f'attr_{self.line}_{self.column}'

    def attr_value(self):
        return f'{self.attr}'

    def accept(self, visitor):
        return visitor.visit_call_attr(self)

    def __init__(self, line: int, column: int, id: Instruction, attr: str):
        super().__init__(line, column)
        self.id = id
        self.attr = attr
