
# Create the class Ast
class Ast:
    # instance from singleton
    _instance = None

    # singleton
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Ast, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    # Constructor, this method is called before the __new__ method
    def __init__(self):
        self.arbol_ast = list()
