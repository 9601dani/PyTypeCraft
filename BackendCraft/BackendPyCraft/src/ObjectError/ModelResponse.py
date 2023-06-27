import pickle
class ModelResponse():
    def __init__(self,table, errors, console, cst):
        self.table = table
        self.errors = errors
        self.console = console
        self.cst = cst
    def __str__(self):
        return "ModelResponse" + str(self.table) + str(self.errors) + str(self.console) + str(self.cst)

    def __dict__(self):
        return {"table": self.table, "errors": self.errors, "console": self.console, "cst": self.cst}

    def __getstate__(self):
        return {
            "table": [obj.__dict__ for obj in self.table],
            "errors": self.errors,
            "console": self.console,
            "cst": self.cst
        }

    def __setstate__(self, state):
        self.table = state["table"]
        self.errors = state["errors"]
        self.console = state["console"]
        self.cst = state["cst"]