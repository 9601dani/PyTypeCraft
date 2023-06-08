class Variable:

    def __init__(self):
        self_id = None
        self_variable_type = None
        self_value = None
        self_type_modifier = None

    def __str__(self):
        return f"""{{"Variable": {self.self_id}, {self.self_variable_type}, {self.self_value}, {self.self_type_modifier}}}"""
