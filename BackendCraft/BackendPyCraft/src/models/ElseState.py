from .Instruction import Instruction
class ElseState (Instruction):

        def accept(self, visitor):
            visitor.visit_else(self)

        def __init__(self, line:int, column:int, instrucciones:[Instruction]):
            super().__init__(line, column)
            self.bloque = instrucciones

        def __str__(self):
            return f"""{{"ElseState": {self.bloque}}}"""