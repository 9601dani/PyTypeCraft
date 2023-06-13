from .Instruction import Instruction
class IfState (Instruction):

        def accept(self, visitor):
           return visitor.visit_if(self)

        def __init__(self, line, column, condition, bloque_verdadero, bloque_falso):
            super().__init__(line, column)
            self.condition = condition
            self.bloque_verdadero = bloque_verdadero
            self.bloque_falso = bloque_falso

        def __str__(self):
            return f"""{{"IfState": {self.condition}, {self.bloque_verdadero}, {self.bloque_falso}}}"""
