from .Instruction import Instruction


class InterfaceState(Instruction):

    def accept(self, visitor):
        pass

    def __init__(self, line: int, column: int, id: str, attributes: [Instruction]):
        super().__init__(line, column)
        self.id = id
        self.attributes = attributes

    def __str__(self):
        return f"""{{"ForState": {self.id} {self.attributes}}}"""