from .Instruction import Instruction


class Value(Instruction):
    def __init__(self, line, column, value, value_type):
        super().__init__(line, column)
        self.value = value
        self.value_type = value_type

    def accept(self, visitor):
       return visitor.visit_value(self)

    def __str__(self):
        return f"""{{"Value": {self.value}, {self.value_type}}}"""