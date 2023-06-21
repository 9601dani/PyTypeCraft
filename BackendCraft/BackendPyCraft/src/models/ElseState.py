from .Instruction import Instruction


class ElseState(Instruction):

    def node_name(self):
        pass

    def node_value(self):
        pass

    def accept(self, visitor):
        return visitor.visit_else(self)

    def __init__(self, line:int, column:int, bloque:[Instruction]):
        super().__init__(line, column)
        self.bloque = bloque

    def __str__(self):
        return f"""{{"ElseState": {self.bloque}}}"""
