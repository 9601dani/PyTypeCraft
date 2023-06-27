from ..models.Variable import Variable


class ArrayModel:

    def __init__(self, var: Variable):
        self.var = var
        self.isAny = False
        self.len = 1
        self.next = None

    def __str__(self):
        return f"""{{"ArrayModel": {self.var}}}"""

    def get_value(self):
        return self.var.value