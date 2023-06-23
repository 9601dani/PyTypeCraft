from .Instruction import Instruction


class Return(Instruction):

    def node_name(self):
        return f'return_{self.line}_{self.column}'

    def node_value(self):
        return f'return_statement'

    def expr_name(self):
        return f'exp_{self.line}_{self.column}'

    def expr_value(self):
        return f'expression'

    def accept(self, visitor):
        return visitor.visit_return(self)

    def __init__(self, line, column, expression):
        super().__init__(line, column)
        self.expression = expression

    def __str__(self):
        return f"""{{"Return": {self.expression}}}"""
