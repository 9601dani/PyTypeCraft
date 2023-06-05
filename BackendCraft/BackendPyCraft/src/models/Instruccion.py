from abc import ABC, abstractmethod
class Instruccion(ABC):
    def __init__(self,line, column):
        self.line = line
        self.column = column
        super().__init__()

    @abstractmethod
    def run(self,table):
        pass
    @abstractmethod
    def accept(self, visitor):
        pass