import pickle
class ModelResponse():
    def __init__(self,table, errors, console):
        self.table = table
        self.errors = errors
        self.console = console
    def __str__(self):
        return "ModelResponse" + str(self.table) + str(self.errors) + str(self.console)

    def __dict__(self):
        return {"table": self.table, "errors": self.errors, "console": self.console}

    def __getstate__(self):
        return {
            "table": self.table,
            "errors": self.errors,
            "console": self.console
        }

    def __setstate__(self, state):
        self.table = state["table"]
        self.errors = state["errors"]
        self.console = state["console"]