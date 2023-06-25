from .SymC3d import SymC3d
class TableC3d:
    def __init__(self, anterior=None):
        self.tabla = {}
        self.anterior = anterior

        self.break_lbl = ''
        self.continue_lbl = ''
        self.return_lbl = ''
        self.rec_temps = False
        self.size = 0
        if anterior != None:
            self.size = anterior.size

    def set_tabla(self, id, tipo, inHeap, find = True):
        if find:
            tablaActual = self
            while tablaActual != None:
                if id in tablaActual.tabla:
                    tablaActual.tabla[id].setTipo(tipo)
                    tablaActual.tabla[id].setInHeap(inHeap)
                    return tablaActual.tabla[id]
                else:
                    tablaActual = tablaActual.anterior

        if id in self.tabla:
            self.tabla[id].setTipo(tipo)
            self.tabla[id].setInHeap(inHeap)
            return self.tabla[id]
        else:
            simbolo = SymC3d(id, tipo, self.size, self.anterior == None, inHeap)
            self.size += 1
            self.tabla[id] = simbolo
            return self.tabla[id]

    def find_tabla(self, id):
        tablaActual = self
        while tablaActual != None:
            if id in tablaActual.tabla:
                return True
            else:
                tablaActual = tablaActual.anterior
        return False

    def get_symbol_by_id(self, id: str):
        current_table = self
        while current_table is not None:
            if id in current_table.tabla:
                return current_table.tabla[id]
            current_table = current_table.anterior

        return None

    def get_tabla(self, ide):
        tablaActual = self
        while tablaActual != None:
            if ide in tablaActual.tabla:
                return tablaActual.tabla[ide]
            tablaActual = tablaActual.anterior
        return None

    def update_tabla(self,id, tipo, inHeap):
        tablaActual = self
        while tablaActual != None:
            if id in tablaActual.tabla:
                tablaActual.tabla[id].setTipo(tipo)
                tablaActual.tabla[id].setInHeap(inHeap)
                return tablaActual.tabla[id]
            else:
                tablaActual = tablaActual.anterior
        return None

    def get_global(self):
        tablaActual = self
        while tablaActual.anterior != None:
            tablaActual = tablaActual.anterior
        return tablaActual

    def __str__(self):
        return f"""{{"Tabla": {str(self.tabla)}}}"""
