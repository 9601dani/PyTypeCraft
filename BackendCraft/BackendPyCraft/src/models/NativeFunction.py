from .Instruction import Instruction
from .NativeFunType import NativeFunType


class NativeFunction(Instruction):
    def node_name(self):
        pass

    def node_value(self):
        pass

    def accept(self, visitor):
        return visitor.visit_native(self)

    def __init__(self, line, column, variable, type: NativeFunType, parameter):
        super().__init__(line, column)
        self.variable = variable
        self.type = type
        self.parameter = parameter
    def __str__(self):
        return f"""{{"NativeFunction": {self.variable} {self.type} {self.parameter}}}"""