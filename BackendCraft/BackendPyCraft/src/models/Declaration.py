import src.visitor.Visitor
from .Instruction import Instruction
from src.visitor import Visitor


class Declaration(Instruction):

    def node_name(self):
        return f'declaration_{self.line}_{self.column}'

    def node_value(self):
        return f'declaration'

    def let_name(self):
        return f'let_{self.line}_{self.column}'

    def let_value(self):
        return f'{self.type}'

    def assign_name(self):
        return f'assignment_list_{self.line}_{self.column}'

    def assign_value(self):
        return f'assignment_list'

    def accept(self, visitor: Visitor):
        # print(visitor)
        return visitor.visit_declaration(self)

    def __init__(self, line: int, column: int, type: str, instructions: [Instruction]):
        super().__init__(line, column)
        self.type = type
        self.instructions = instructions

    def __str__(self):
        return f"""{{"Declaration": {self.type}, {self.instructions.__str__()}}}"""