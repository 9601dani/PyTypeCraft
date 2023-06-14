class VariableType:

    _instance = None

    # singleton para llamar a la lista de variables
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(VariableType, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass

    lista_variables = {
        "NUMBER": "number",
        "STRING": "string",
        "BOOLEAN": "boolean",
        "ANY": "any",
        "NULL": "null",
        "ARRAY": "array",
        "DEFINIRLA": "definirla"
    }

    def buscar_type(self, tipo):
        for key, value in self.lista_variables.items():
            if key == tipo.upper():
                return value
        return self.lista_variables["DEFINIRLA"]

    def add_type(self, type):
        self.lista_variables[type.upper()] = type

    def type_declared(self, type):
        for key, value in self.lista_variables.items():
            if key == type.upper():
                return True
        return False
