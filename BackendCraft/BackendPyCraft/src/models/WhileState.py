from .Instruction import Instruction


class WhileState(Instruction):

    def node_name(self):
        return f'while_{self.line}_{self.column}'

    def node_value(self):
        return f'While_statement'

    def condition_name(self):
        return f'condition_{self.line}_{self.column}'

    def condition_value(self):
        return f'condition'

    def body_name(self):
        return f'body_{self.line}_{self.column}'

    def body_value(self):
        return f'body'

    def accept(self, visitor):
        return visitor.visit_while(self)

    def __init__(self, line: int, column: int, condition: Instruction, instructions: [Instruction]):
        super().__init__(line, column)
        self.condition = condition
        self.instructions = instructions

    def __str__(self):
        return f"""{{"WhileState": {self.condition} {self.instructions.__str__()}}}"""
