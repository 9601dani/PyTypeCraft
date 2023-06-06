# Import from abc to create abstract classes
from abc import ABC, abstractmethod


# Create the abstract class Instruction
class Instruction(ABC):
    # Constructor
    def __init__(self, line, column):
        self.line = line
        self.column = column
        super().__init__()

    # Methods to be implemented Visitor
    @abstractmethod
    def run(self, table):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass
