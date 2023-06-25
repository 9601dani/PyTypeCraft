class SymC3d:
    def __init__(self, symbolID, symbolType, position, globalVar, in_heap):
        self.id = symbolID
        self.type = symbolType
        self.pos = position
        self.is_global = globalVar
        self.in_heap = in_heap
        self.value = None
        self.tipo_aux = ''
        self.length = 0
        self.referencia = False
        self.params = None

    def get_tipo(self):
        return self.type
    def get_id(self):
        return self.id
    def get_pos(self):
        return self.pos
    def get_in_heap(self):
        return self.in_heap

    def get_params(self):
        return self.params

    def set_params(self, params):
        self.params = params

    def set_tipo(self, tipo):
        self.type = tipo
    def set_id(self, id):
        self.id = id
    def set_pos(self, pos):
        self.pos = pos
    def set_in_heap(self, value):
        self.in_heap = value

    def set_tipo_aux(self, tipo):
        self.tipo_aux = tipo

    def get_tipo_aux(self):
        return self.tipo_aux

    def set_length(self, length):
        self.length = length
    def get_length(self):
        return self.length

    def set_referencia(self, ref):
        self.referencia = ref
    def get_referencia(self):
        return self.referencia

    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value