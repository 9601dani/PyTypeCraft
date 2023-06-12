class Variable:

    def __init__(self):
        self.id = None
        self.data_type = None
        self.symbol_type = None
        self.value = None
        self.type_modifier = None

    def __str__(self):
        return f"""{{"Variable": {self.id}, {self.data_type}, {self.value}, {self.type_modifier}}}"""
