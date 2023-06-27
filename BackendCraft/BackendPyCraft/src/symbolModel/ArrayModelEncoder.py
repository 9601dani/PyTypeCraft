import json
from ..symbolModel.ArrayModel import ArrayModel
class ArrayModelEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ArrayModel):
            data = {
                "var": str(obj.var),
                "isAny": str(obj.isAny),
                "len": str(obj.len),
                "next": str(obj.next)
            }

            return data

        return super().default(obj)
