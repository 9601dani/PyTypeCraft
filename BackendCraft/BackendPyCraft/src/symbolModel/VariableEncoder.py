import json
from ..models.Variable import Variable
class ArrayModelEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Variable):
            data = {
               "id": str(obj.id),
                "data_type": str(obj.data_type),
                "symbol_type": str(obj.symbol_type),
                "value": str(obj.value),
                "type_modifier": str(obj.type_modifier),
                "isAny": str(obj.isAny)
            }

            return data

        return super().default(obj)
