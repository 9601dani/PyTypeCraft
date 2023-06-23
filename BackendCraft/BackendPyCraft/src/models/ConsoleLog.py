from .Instruction import Instruction


class ConsoleLog(Instruction):
    def node_name(self):
        return f'console_{self.line}_{self.column}'

    def node_value(self):
        return f'console_log'

    def content_name(self):
        return f'content_{self.line}_{self.column}'

    def content_value(self):
        return f'values'

    def accept(self, visitor):
       return visitor.visit_console(self)

    def __init__(self, line, column, value: [Instruction]):
        super().__init__(line, column)
        self.value = value


    def __str__(self):
        return f"""{{"console.log": {self.value.__str__()}}}"""

