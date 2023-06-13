from .Instruction import Instruction


class Parameter(Instruction):


    def accept(self, visitor):
       return visitor.visit_parameter(self)

    def __init__(self, line: int, column: int, id, variable_type, isAny):
        super().__init__(line, column)
        self.id = id
        self.type = variable_type
        self.isAny = isAny



