from .Instruction import Instruction


class CallFunction(Instruction):
    def node_name(self):
        return f'call_fn_{self.line}_{self.column}'

    def node_value(self):
        return f'call_function'

    def id_name(self):
        return f'id_{self.line}_{self.column}'

    def id_value(self):
        return f'{self.name}'

    def args_name(self):
        return f'args_{self.line}_{self.column}'

    def args_value(self):
        return f'arguments'

    def accept(self, visitor):
        return visitor.visit_call_fun(self)

    def __init__(self, line, column, name, assignments: [Instruction]):
        super().__init__(line, column)
        self.name = name
        self.assignments = assignments

    def __str__(self):
        return f"""{{"CallFunction": {self.name}, "Assignments": {self.assignments}}}"""