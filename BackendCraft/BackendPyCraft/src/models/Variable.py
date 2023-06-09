class Variable:

    def __init__(self):
        self.id = None
        self.variable_type = None
        self.value = None
        self.type_modifier = None

    def __str__(self):
        return f"""{{"Variable": {self.id}, {self.variable_type}, {self.value}, {self.type_modifier}}}"""
