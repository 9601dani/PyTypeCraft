class ReturnC3d:
    def __init__(self, value,type, isTemp, auxType="", length=0, referencia=""):
        self.value = value
        self.type = type
        self.isTemp = isTemp
        self.auxType = auxType
        self.length = length
        self.referencia = referencia
        self.trueLb1 = ""
        self.falseLb1 = ""

    def get_value(self):
        return self.value

    def get_tipo(self):
        return self.type

    def get_tipo_aux(self):
        return self.auxType

    def get_length(self):
        return self.length

    def get_referencia(self):
        return self.referencia

    def get_true_lb1(self):
        return self.trueLb1

    def get_false_lb1(self):
        return self.falseLb1

    def set_value(self,value):
        self.value = value

    def set_tipo(self,type):
        self.type = type

    def set_tipo_aux(self,auxType):
        self.auxType = auxType

    def set_length(self,length):
        self.length = length

    def set_referencia(self,referencia):
        self.referencia = referencia

    def set_true_lb1(self,trueLb1):
        self.trueLb1 = trueLb1

    def set_false_lb1(self,falseLb1):
        self.falseLb1 = falseLb1

    def get_isTemp(self):
        return self.isTemp

    def set_isTemp(self,isTemp):
        self.isTemp = isTemp


