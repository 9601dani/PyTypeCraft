from .Instruction import Instruction
from .NativeFunType import NativeFunType


class NativeFunction(Instruction):
    def node_name(self):
        return f'native_{self.line}_{self.column}'

    def node_value(self):
        return f'native_function'

    def var_name(self):
        return f'var_{self.line}_{self.column}'

    def var_value(self):
        return f'variable'

    def native_name(self):
        return f'nat_type_{self.line}_{self.column}'

    def native_value(self):
        return f'{self.type}'

    def arg_name(self):
        return f'arg_{self.line}_{self.column}'

    def arg_value(self):
        return f'argument'

    def accept(self, visitor):
        return visitor.visit_native(self)

    def __init__(self, line, column, variable, type: NativeFunType, parameter):
        super().__init__(line, column)
        self.variable = variable
        self.type = type
        self.parameter = parameter
    def __str__(self):
        return f"""{{"NativeFunction": {self.variable} {self.type} {self.parameter}}}"""