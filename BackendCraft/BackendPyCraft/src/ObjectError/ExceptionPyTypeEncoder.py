import json
from ..ObjectError.ExceptionPyType import ExceptionPyType
class ExceptionPyTypeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ExceptionPyType):
            data = {
                "message": str(obj.message),
                "line": str(obj.line),
                "column": str(obj.column),
                "date_time": str(obj.date_time)
            }

            return data

        return super().default(obj)
