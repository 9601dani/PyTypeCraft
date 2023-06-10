from .Instruction import Instruction


class CallFunction(Instruction):
    def accept(self, visitor):
        visitor.visit(self)

    def __init__(self, line, column, name, assignments: [Instruction]):
        super().__init__(line, column)
        self.name = name
        self.assignments = assignments

    def __str__(self):
        return f"""{{"CallFunction": {self.name}, "Assignments": {self.assignments}}}"""