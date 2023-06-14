from ..models.Variable import Variable
from ..models.Instruction import Instruction


class FunctionModel:

    def __init__(self, id: str, parameters: [Variable], instructions: [Instruction]):
        self.id = id
        self.parameters = parameters
        self.instructions = instructions
