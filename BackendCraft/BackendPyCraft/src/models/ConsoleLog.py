from PyTypeCraft.BackendCraft.BackendPyCraft.src.models.Instruction import Instruction


class ConsoleLog(Instruction):
    def run(self, table):
        pass

    def accept(self, visitor):
        pass

    def __init__(self, line, column, value: []):
        super().__init__(line, column)
        self.value = value
        print("Constructor* "+self.value, self.line, self.column)

