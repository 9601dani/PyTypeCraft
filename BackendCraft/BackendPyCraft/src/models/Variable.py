class Variable:

    def __init__(self):
        self.id = None
        self.data_type = None
        self.symbol_type = None
        self.value = None
        self.type_modifier = None
        self.isAny = None

    def __str__(self):
        return f"""{{"Variable": id: {self.id}, data_type: {self.data_type}, value: {self.value}, symbol_type: {self.symbol_type}, type_modifies: {self.type_modifier}, isAny?: {self.isAny}}}"""

    def get_value(self):
        return str(self.value)
