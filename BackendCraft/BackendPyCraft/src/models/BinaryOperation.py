from .Instruction import Instruction
from .OperationType import OperationType


class BinaryOperation(Instruction):
    def node_name(self):
        return f'binary_{self.line}_{self.column}'

    def node_value(self):
        return f'binary_operation'

    def left_name(self):
        return f'left_{self.line}_{self.column}'

    def left_value(self):
        return f'left'

    def right_name(self):
        return f'right_{self.line}_{self.column}'

    def right_value(self):
        return f'right'

    def op_name(self):
        return f'op_{self.line}_{self.column}'

    def op_value(self):
        if self.operator == OperationType.OR:
            return "||"
        elif self.operator == OperationType.AND:
            return "&&"
        elif self.operator == OperationType.MENOR_IGUAL_QUE:
            return "<="
        elif self.operator == OperationType.MAYOR_IGUAL_QUE:
            return ">="
        elif self.operator == OperationType.MENOR_QUE:
            return "<"
        elif self.operator == OperationType.MAYOR_QUE:
            return ">"
        elif self.operator == OperationType.DISTINTO_QUE:
            return "!="
        elif self.operator == OperationType.TRIPLE_IGUAL:
            return "=="
        elif self.operator == OperationType.MAS:
            return "+"
        elif self.operator == OperationType.MENOS:
            return "-"
        elif self.operator == OperationType.MOD:
            return "%"
        elif self.operator == OperationType.DIVIDE:
            return "/"
        elif self.operator == OperationType.TIMES:
            return "*"
        elif self.operator == OperationType.POTENCIA:
            return "^"

    def accept(self, visitor):
        return visitor.visit_binary_op(self)

    def __init__(self, line, column, left_operator, right_operator, operator):
        super().__init__(line, column)
        self.left_operator = left_operator
        self.right_operator = right_operator
        self.operator = operator

    def __str__(self):
        return f"""{{"BinaryOperation": {self.left_operator} {self.operator} {self.right_operator}}}"""