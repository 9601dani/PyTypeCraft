import json
from ..ObjectError.ExceptionPyType import ExceptionPyType
class ExceptionPyTypeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ExceptionPyType):
            data = {
                "mensaje": str(obj.message),
                "linea": str(obj.line),
                "columna": str(obj.column),
                "date_time": str(obj.date_time)
            }

            return data

        return super().default(obj)