from .Instruction import Instruction


class InterfaceAssign(Instruction):

    def node_name(self):
        pass

    def node_value(self):
        pass

    def accept(self, visitor):
        return visitor.visit_interface_assign(self)

    def __init__(self, line: int, column: int, attributes: [Instruction]):
        super().__init__(line, column)
        self.attributes = attributes
