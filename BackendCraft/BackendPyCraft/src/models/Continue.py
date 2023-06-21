from .Instruction import Instruction


class Continue(Instruction):
    def node_name(self):
        pass

    def node_value(self):
        pass

    def accept(self, visitor):
        return visitor.visit_continue(self)

    def __init__(self, line, column):
        super().__init__(line, column)

    def __str__(self):
        return f"""{{"Continue": }}"""
