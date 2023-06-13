from ..models.SymbolType import SymbolType
from ..models.Variable import Variable
from ..symbolTable.SymbolTable import SymbolTable

class SymbolTable:

    def __init__(self, *parent: SymbolTable):
        self.symbols = []
        if parent:
            self.parent = parent

    def add_variable(self, variable: Variable):
        self.symbols.append(variable)

    # THIS METHOD CHECKS IF THE ID VARIABLE IS ALREADY DECLARED
    # IF IS DECLARED THEN RETURN IT.
    def find_var_by_id(self, id: str):
        current_table = self

        while current_table is not None:
            var_in_table = filter(lambda var: (var.id == id and var.symbol_type == SymbolType.VARIABLE), self.symbols)

            if var_in_table is not None:
                return var_in_table

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
            fun_in_table = filter(lambda var: (var.id == id and var.symbol_type == SymbolType.FUNCTION), self.symbols)

            if fun_in_table is not None:
                return fun_in_table

            current_table = current_table.parent

        return None

    #BOOLEAN METHOD, RETURN TRUE IF FUNCTION IS IN TABLE, IF NOT RETURN FALSE
    def fun_in_table(self, id: str):
        return any( (var.id == id and var.symbol_type == SymbolType.FUNCTION) for var in self.symbols)
