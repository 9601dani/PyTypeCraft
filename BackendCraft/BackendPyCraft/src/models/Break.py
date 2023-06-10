from .Instruction import Instruction


class Break(Instruction):
    def accept(self, visitor):
        pass

    def __init__(self, line, column):
        super().__init__(line, column)

    def __str__(self):
        return f"""{{"Break": }}"""