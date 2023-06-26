import pickle
class ModelResponse():
    def __init__(self,table, errors, console, cst, c3d):
        self.table = table
        self.errors = errors
        self.console = console
        self.cst = cst
        self.c3d= c3d
    def __str__(self):
        return "ModelResponse" + str(self.table) + str(self.errors) + str(self.console) + str(self.cst) + str(self.c3d)

    def __dict__(self):
        return {"table": self.table, "errors": self.errors, "console": self.console, "cst": self.cst, "c3d": self.c3d}

    def __getstate__(self):
        return {
            "table": self.table,
            "errors": self.errors,
            "console": self.console,
            "cst": self.cst,
            "c3d": self.c3d
        }

    def __setstate__(self, state):
        self.table = state["table"]
        self.errors = state["errors"]
        self.console = state["console"]
        self.cst = state["cst"]
        self.c3d = state["c3d"]