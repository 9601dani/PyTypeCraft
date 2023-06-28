from .Instruction import Instruction


class ForState(Instruction):

    def node_name(self):
        return f'for_{self.line}_{self.column}'

    def node_value(self):
        return f'for_statement'

    def dec_name(self):
        return f'declaration_{self.line}_{self.column}'

    def dec_value(self):
        return f'declaration_block'

    def con_name(self):
        return f'condition_{self.line}_{self.column}'

    def con_value(self):
        return f'condition_block'

    def inc_name(self):
        return f'increment_{self.line}_{self.column}'

    def inc_value(self):
        return f'increment_block'

    def body_name(self):
        return f'body_{self.line}_{self.column}'

    def body_value(self):
        return f'body'

    def accept(self, visitor):
        return visitor.visit_for(self)

    def __init__(self, line: int,
                 column: int,
                 declaration: Instruction,
                 condition: Instruction,
                 increment: Instruction,
                 instructions: [Instruction]):
        super().__init__(line, column)
        self.declaration = declaration
        self.condition = condition
        self.increment = increment
        self.instructions = instructions

    def __str__(self):
        return f"""{{"ForState": {self.declaration} {self.condition} {self.increment} {self.instructions}}}"""