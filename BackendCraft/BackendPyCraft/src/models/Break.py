from .Instruction import Instruction


class Break(Instruction):
    def node_name(self):
        return f'break_{self.line}_{self.column}'

    def node_value(self):
        return f'Break_statement'

    def accept(self, visitor):
        return visitor.visit_break(self)

    def __init__(self, line, column):
        super().__init__(line, column)

    def __str__(self):
        return f"""{{"Break": }}"""