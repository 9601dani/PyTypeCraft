from .Instruction import Instruction


class InterAttributeAssign(Instruction):

    def node_name(self):
        return f'only_assign_{self.line}_{self.column}'

    def node_value(self):
        return f'assignment'

    def equals_name(self):
        return f'eq_{self.line}_{self.column}'

    def equals_value(self):
        return f'='

    def accept(self, visitor):
        return visitor.visit_inter_attr_assign(self)

    def __init__(self, line: int, column: int, interAttribute: Instruction, value: Instruction):
        super().__init__(line, column)
        self.interAttribute = interAttribute
        self.value = value
