from datetime import datetime
class ExeptionPyType():
    def __init__(self, message, line, column, date_time=datetime.now()):
        self.message = message
        self.line = line
        self.column = column
        self.date_time = date_time

    def __str__(self):
        return f"""{{"ExeptionPyType": {self.message}, {self.line}, {self.column}}}"""