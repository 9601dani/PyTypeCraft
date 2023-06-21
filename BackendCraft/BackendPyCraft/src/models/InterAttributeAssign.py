from .Instruction import Instruction


class InterAttributeAssign(Instruction):

    def node_name(self):
        pass

    def node_value(self):
        pass

    def accept(self, visitor):
        return visitor.visit_inter_attr_assign(self)

    def __init__(self, line: int, column: int, interAttribute: Instruction, value: Instruction):
        super().__init__(line, column)
        self.interAttribute = interAttribute
        self.value = value
