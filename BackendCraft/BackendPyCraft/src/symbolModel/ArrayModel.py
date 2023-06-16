from ..models.Variable import Variable


class ArrayModel:

    def __init__(self, var: Variable):
        self.var = var
        self.isAny = False
        self.len = 1
        self.next = None
