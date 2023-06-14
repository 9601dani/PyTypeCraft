from ..models.Variable import Variable


class InterfaceModel:

    def __init__(self, id: str, attributes: [Variable]):
        self.id = id
        self.attributes = attributes

    def __str__(self):
        return f"""{{"InterfaceModel": {self.id} {self.attributes}}}"""
