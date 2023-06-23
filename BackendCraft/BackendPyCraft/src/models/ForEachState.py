from .Instruction import Instruction


class ForEachState(Instruction):

    def node_name(self):
        pass

    def node_value(self):
        pass

    def accept(self, visitor):
        return visitor.visit_foreach(self)

    def __init__(self, line: int, column: int, id: str, assignment: Instruction, instructions: [Instruction]):
        super().__init__(line, column)
        self.id = id
        self.assignment = assignment
        self.instructions = instructions

    def __str__(self):
        return f"""{{"ForEachState": {self.id} {self.assignment}  {self.instructions}}}"""
