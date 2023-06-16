from ..models.SymbolType import SymbolType
from ..models.Variable import Variable
from ..symbolTable.ScopeType import ScopeType


class SymbolTable:

    def __init__(self, parent=None, scope=ScopeType.GLOBAL_SCOPE):
        self.symbols = []
        self.scope = scope
        if parent:
            self.parent = parent
        else:
            self.parent = None

    def add_variable(self, variable: Variable):
        self.symbols.append(variable)

    # THIS METHOD CHECKS IF THE ID VARIABLE IS ALREADY DECLARED
    # IF IS DECLARED THEN RETURN IT.
    def find_var_by_id(self, id: str):
        current_table: SymbolTable = self

        while current_table is not None:

            for symbol in current_table.symbols:
                if symbol.id == id and (symbol.symbol_type == SymbolType().VARIABLE or symbol.symbol_type == SymbolType().ARRAY):
                    # print("Variable encontrada: "+symbol.__str__())
                    return symbol

            current_table = current_table.parent

        return None

    # BOOLEAN METHOD, RETURN TRUE IF VARIABLE IS IN TABLE, IF NOT RETURN FALSE
    def var_in_table(self, id: str):
        return any((var.id == id and (var.symbol_type == SymbolType().VARIABLE or var.symbol_type == SymbolType().ARRAY)) for var in self.symbols)

    # THIS METHOD CHECKS IF THE ID FUNCTION IS ALREADY DECLARED
    # IF IS DECLARED THEN RETURN IT.
    def find_fun_by_id(self, id: str):
        current_table = self
        functions: [Variable] = []
        while current_table is not None:
            for symbol in current_table.symbols:
                if symbol.symbol_type == SymbolType().FUNCTION and symbol.id == id:
                    # print("Variable encontrada: "+symbol.__str__())
                    functions.append(symbol)

            current_table = current_table.parent

        return functions

    def find_interface_by_id(self, id: str):
        current_table = self

        while current_table is not None:
            for symbol in current_table.symbols:
                if symbol.symbol_type == SymbolType().INTERFACE and symbol.id == id:
                    # print("Variable encontrada: "+symbol.__str__())
                    return symbol

            current_table = current_table.parent

        return None

    # BOOLEAN METHOD, RETURN TRUE IF FUNCTION IS IN TABLE, IF NOT RETURN FALSE
    def fun_in_table(self, id: str):
        return any((var.id == id and var.symbol_type == SymbolType().FUNCTION) for var in self.symbols)

    def is_in_fun_scope(self):
        current_table = self

        if current_table.scope == ScopeType.GLOBAL_SCOPE:
            return False

        while current_table is not None:
            if current_table.scope == ScopeType.FUNCTION_SCOPE:
                return True

            current_table = current_table.parent

        return False

    def is_in_loop_scope(self):
        current_table = self

        if current_table.scope == ScopeType.GLOBAL_SCOPE:
            return False

        while current_table is not None:
            if current_table.scope == ScopeType.LOOP_SCOPE:
                return True

            current_table = current_table.parent

        return False

    def getAllFunctions(self):
        current_table = self
        functions = []

        while current_table is not None:
            for symbol in current_table.symbols:
                if symbol.symbol_type == SymbolType.FUNCTION:
                    functions.append(symbol)

            current_table = current_table.parent

        return functions
    def __str__(self):
        data = ""
        for symbol in self.symbols:
            data += symbol.__str__()
        return f"""{{"SymbolTable": {data}}}"""
