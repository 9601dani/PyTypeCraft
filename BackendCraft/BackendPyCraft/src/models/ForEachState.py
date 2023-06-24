from .Instruction import Instruction


class ForEachState(Instruction):

    def node_name(self):
        return f'for_each_{self.line}_{self.column}'

    def node_value(self):
        return f'for_each_statement'

    def id_name(self):
        return f'id_{self.line}_{self.column}'

    def id_value(self):
        return f'{self.id}'

    def assign_name(self):
        return f'assign_{self.line}_{self.column}'

    def assign_value(self):
        return f'assignment'

    def of_name(self):
        return f'of_{self.line}_{self.column}'

    def of_value(self):
        return f'of'

    def body_name(self):
        return f'body_{self.line}_{self.column}'

    def body_value(self):
        return f'body'

    def accept(self, visitor):
        return visitor.visit_foreach(self)

    def __init__(self, line: int, column: int, id: str, assignment: Instruction, instructions: [Instruction]):
        super().__init__(line, column)
        self.id = id
        self.assignment = assignment
        self.instructions = instructions

    def __str__(self):
        return f"""{{"ForEachState": {self.id} {self.assignment}  {self.instructions}}}"""
