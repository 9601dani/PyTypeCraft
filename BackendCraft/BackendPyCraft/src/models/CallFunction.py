from .Instruction import Instruction


class CallFunction(Instruction):
    def node_name(self):
        pass

    def node_value(self):
        pass

    def accept(self, visitor):
        return visitor.visit_call_fun(self)

    def __init__(self, line, column, name, assignments: [Instruction]):
        super().__init__(line, column)
        self.name = name
        self.assignments = assignments

    def __str__(self):
        return f"""{{"CallFunction": {self.name}, "Assignments": {self.assignments}}}"""