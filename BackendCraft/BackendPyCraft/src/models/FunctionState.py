from .Instruction import Instruction
from .VariableType import VariableType


class FunctionState(Instruction):

    def node_name(self):
        return f'fun_{self.line}_{self.column}'

    def node_value(self):
        return f'function_statement'

    def id_name(self):
        return f'id_{self.line}_{self.column}'

    def id_value(self):
        return f'{self.id}'

    def params_name(self):
        return f'params_{self.line}_{self.column}'

    def params_value(self):
        return f'parameters'

    def body_name(self):
        return f'body_{self.line}_{self.column}'

    def body_value(self):
        return f'body'

    def return_name(self):
        return f'return_{self.line}_{self.column}'

    def return_value(self):
        return f'{self.return_type}'

    def accept(self, visitor):
        return visitor.visit_function(self)

    def __init__(self, line: int, column: int, id: str, isInTable: bool, parameters: [Instruction], instructions: [Instruction], return_type):
        super().__init__(line, column)
        self.id = id
        self.isInTable = isInTable
        self.parameters = parameters
        self.instructions = instructions
        self.return_type = return_type

    def __str__(self):
        return f"""{{"FunctionState": {self.id} {self.parameters} {self.instructions}}}"""
