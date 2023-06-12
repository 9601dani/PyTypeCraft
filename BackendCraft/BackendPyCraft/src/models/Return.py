from .Instruction import Instruction


class Return(Instruction):
    def accept(self, visitor):
        visitor.visit_return(self)

    def __init__(self, line, column, expression):
        super().__init__(line, column)
        self.expression = expression

    def __str__(self):
        return f"""{{"Return": {self.expression}}}"""