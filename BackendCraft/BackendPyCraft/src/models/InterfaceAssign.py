from .Instruction import Instruction


class InterfaceAssign(Instruction):

    def node_name(self):
        return f'inter_assign_{self.line}_{self.column}'

    def node_value(self):
        return f'interface_assignment'

    def attrs_name(self):
        return f'attrs_{self.line}_{self.column}'

    def attrs_value(self):
        return f'attributes'

    def accept(self, visitor):
        return visitor.visit_interface_assign(self)

    def __init__(self, line: int, column: int, attributes: [Instruction]):
        super().__init__(line, column)
        self.attributes = attributes
