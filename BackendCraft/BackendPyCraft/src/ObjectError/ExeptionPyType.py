
class ExeptionPyType():
    def __init__(self, message, line, column):
        self.message = message
        self.line = line
        self.column = column

    def __str__(self):
        return f"""{{"ExeptionPyType": {self.message}, {self.line}, {self.column}}}"""