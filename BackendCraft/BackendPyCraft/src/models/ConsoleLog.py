from .Instruction import Instruction


class ConsoleLog(Instruction):
    def node_name(self):
        pass

    def node_value(self):
        pass

    def accept(self, visitor):
       return visitor.visit_console(self)

    def __init__(self, line, column, value: [Instruction]):
        super().__init__(line, column)
        self.value = value


    def __str__(self):
        return f"""{{"console.log": {self.value.__str__()}}}"""

