from ..models.Instruction import Instruction


class CallAttribute(Instruction):

    def accept(self, visitor):
        return visitor.visit_call_attr(self)

    def __init__(self, line: int, column: int, id: Instruction, attr: str):
        super().__init__(line, column)
        self.id = id
        self.attr = attr
