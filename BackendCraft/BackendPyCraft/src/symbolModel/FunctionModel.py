from ..models.Variable import Variable
from ..models.Instruction import Instruction


class FunctionModel:

    def __init__(self, id: str, parameters: [Variable], instructions: [Instruction], return_type):
        self.id = id
        self.parameters = parameters
        self.instructions = instructions
        self.isInTable = True
        self.return_type = return_type

    def __str__(self):
        return f"""{{"Function": id: {self.id}, parameters: {self.parameters}, instructions: {self.instructions}, return_type: {self.return_type}}}"""