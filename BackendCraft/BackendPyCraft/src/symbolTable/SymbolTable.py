from ..models.SymbolType import SymbolType
from ..models.Variable import Variable

class SymbolTable:

    def __init__(self, *parent):
        self.symbols = []
        if parent:
            self.parent = parent
        else:
            self.parent = None

    def add_variable(self, variable: Variable):
        self.symbols.append(variable)

    # THIS METHOD CHECKS IF THE ID VARIABLE IS ALREADY DECLARED
    # IF IS DECLARED THEN RETURN IT.
    def find_var_by_id(self, id: str):
        current_table = self

        while current_table is not None:

            for symbol in current_table.symbols:
                if symbol.symbol_type == SymbolType.VARIABLE and symbol.id == id:
                    print("Variable encontrada: "+symbol.__str__())
                    return symbol

            current_table = current_table.parent

        return None

    #BOOLEAN METHOD, RETURN TRUE IF VARIABLE IS IN TABLE, IF NOT RETURN FALSE
    def var_in_table(self, id: str):
        return any( (var.id == id and var.symbol_type == SymbolType.VARIABLE) for var in self.symbols)

    # THIS METHOD CHECKS IF THE ID FUNCTION IS ALREADY DECLARED
    # IF IS DECLARED THEN RETURN IT.
    def find_fun_by_id(self, id: str):
        current_table = self

        while current_table is not None:
            for symbol in current_table.symbols:
                if symbol.symbol_type == SymbolType.FUNCTION and symbol.id == id:
                    print("Variable encontrada: "+symbol.__str__())
                    return symbol

            current_table = current_table.parent

        return None

    #BOOLEAN METHOD, RETURN TRUE IF FUNCTION IS IN TABLE, IF NOT RETURN FALSE
    def fun_in_table(self, id: str):
        return any( (var.id == id and var.symbol_type == SymbolType.FUNCTION) for var in self.symbols)

    def __str__(self):
        data = ""
        for symbol in self.symbols:
            data+= symbol.__str__()
        return f"""{{"SymbolTable": {data}}}"""