from .Instruction import Instruction


class InterfaceState(Instruction):

    def node_name(self):
        return f'interface_{self.line}_{self.column}'

    def node_value(self):
        return f'interface_statement'

    def id_name(self):
        return f'id_{self.line}_{self.column}'

    def id_value(self):
        return f'{self.id}'

    def attrs_name(self):
        return f'attrs_{self.line}_{self.column}'

    def attrs_value(self):
        return f'attributes'

    def accept(self, visitor):
        return visitor.visit_interface(self)

    def __init__(self, line: int, column: int, id: str, attributes: [Instruction]):
        super().__init__(line, column)
        self.id = id
        self.attributes = attributes

    def __str__(self):
        return f"""{{"InterfaceState": {self.id} {self.attributes}}}"""