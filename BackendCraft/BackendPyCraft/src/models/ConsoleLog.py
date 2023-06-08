from .Instruction import Instruction


class ConsoleLog(Instruction):
    def accept(self, visitor):
        return visitor.visit_console_log(self)

    def __init__(self, line, column, value: []):
        super().__init__(line, column)
        self.value = value


    def __str__(self):
        return f"""{{"console.log": {self.value}}}"""

