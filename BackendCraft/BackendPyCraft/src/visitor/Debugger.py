from .Visitor import Visitor
from ..models import Assignment
from ..models import BinaryOperation
from ..models import Break
from ..models import CallFunction
from ..models import ConsoleLog
from ..models import Continue
from ..models import Declaration
from ..models import ElseState
from ..models import ForEachState
from ..models import ForState
from ..models import FunctionState
from ..models import IfState
from ..models import InterfaceState
from ..models import Instruction
from ..models import NativeFunction
from ..models import OnlyAssignment
from ..models import Parameter
from ..models import Return
from ..models import UnaryOperation
from ..models import WhileState
from ..models import Value
from ..models.Variable import Variable
from ..models.SymbolType import SymbolType
from ..symbolTable.SymbolTable import SymbolTable
from ..models.ValueType import ValueType
from ..models.VariableType import VariableType
from ..models.OperationType import OperationType
import copy


class Debugger(Visitor):

    def __init__(self, symbol_table: SymbolTable, errors):
        super().__init__()
        self.symbol_table = symbol_table
        self.errors = errors

    def visit_assignment(self, i: Assignment):
        result = Variable()
        print("isAny:" + str(i.isAny))
        result.id = i.id
        # print("VARIABLE EN ASSIGNMENT: ",i.id)

        if i.value is None:
            if i.type == VariableType().buscar_type("NUMBER"):
                result.data_type = VariableType().buscar_type("NUMBER")
                result.symbol_type = SymbolType().VARIABLE
                result.isAny = False

                result.value = 0
                return result
            elif i.type == VariableType().buscar_type("STRING"):
                result.data_type = VariableType().buscar_type("STRING")
                result.symbol_type = SymbolType().VARIABLE
                result.isAny = False

                result.value = ""
                return result
            elif i.type == VariableType().buscar_type("BOOLEAN"):
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.symbol_type = SymbolType().VARIABLE
                result.isAny = False

                result.value = True
                return result
            elif i.type == VariableType().buscar_type("NULL"):
                result.data_type = VariableType().buscar_type("NULL")
                result.symbol_type = SymbolType().VARIABLE
                result.isAny = False

                result.value = None
                return result
            elif i.type == VariableType().buscar_type("STRING"):
                result.data_type = VariableType().buscar_type("STRING")
                result.symbol_type = SymbolType().VARIABLE
                result.isAny = False

                result.value = ''
                return result
            elif i.type is None or i.type == VariableType().buscar_type("ANY"):
                result.data_type = VariableType().buscar_type("STRING")
                result.symbol_type = SymbolType().VARIABLE
                result.isAny = False

                result.value = ''
                return result

        else:
            value: Variable = i.value.accept(self)
            # print(i.type)
            if value is None:
                self.errors.append("NO SE PUDO REALIZAR LA ASIGNACIÓN")
                print("NO SE PUDO REALIZAR LA ASIGNACIÓN")
                return None

            if i.type is None or i.type == VariableType().buscar_type("ANY"):
                # print("VALUE ASSIG: "+value.data_type)
                result.data_type = value.data_type
                result.symbol_type = SymbolType().VARIABLE
                result.value = value.value
                result.isAny = True
                return result

            if i.type != value.data_type:
                print(str(value.data_type))
                self.errors.append("LA VARIABLE NO ES DEL MISMO TIPO")
                print("LA VARIABLE NO ES DEL MISMO TIPO")
                return None

            result.data_type = value.data_type
            result.symbol_type = SymbolType().VARIABLE
            result.isAny = False
            result.value = value.value
            return result

    def visit_binary_op(self, i: BinaryOperation):
        left = i.left_operator.accept(self)
        right = i.right_operator.accept(self)

        if left is None or right is None:
            self.errors.append("NO SE PUDO REALIZAR LA OPERACIÓN")
            return None

        result = Variable()

        if i.operator == OperationType.MAS:
            if left.data_type == VariableType.lista_variables["NUMBER"]:
                if right.data_type != VariableType.lista_variables["NUMBER"]:
                    # print("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE VARIABLES DEL MISMO TIPO.")
                    self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE VARIABLES DEL MISMO TIPO.")
                    return None

                result.symbol_type = SymbolType.VARIABLE
                result.data_type = VariableType().buscar_type("NUMBER")
                result.value = left.value + right.value
                # result.type_modifier = False
                return result
            elif left.data_type == VariableType.lista_variables["STRING"]:
                if right.data_type != VariableType.lista_variables["STRING"]:
                    # print("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE VARIABLES DEL MISMO TIPO.")
                    self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE VARIABLES DEL MISMO TIPO.")
                    return None

                result.symbol_type = SymbolType.VARIABLE
                result.data_type = VariableType().buscar_type("STRING")
                result.value = left.value + right.value
                # result.type_modifier = False
                return result

            else:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE NUMBER Y STRING.")




        elif i.operator == OperationType.MENOS:
            if left.data_type != VariableType.lista_variables["NUMBER"] or right.data_type != \
                    VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (-) ENTRE NUMBER.")
                return None

            result.symbol_type = SymbolType.VARIABLE
            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = left.value - right.value
            # result.type_modifier = False
            return result

        elif i.operator == OperationType.TIMES:
            if left.data_type != VariableType.lista_variables["NUMBER"] or right.data_type != \
                    VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (*) ENTRE NUMBER.")
                return None

            result.symbol_type = SymbolType.VARIABLE
            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = left.value * right.value
            # result.type_modifier = False
            return result

        elif i.operator == OperationType.DIVIDE:
            if left.data_type != VariableType.lista_variables["NUMBER"] or right.data_type != \
                    VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (/) ENTRE NUMBER.")
                return None

            if right.value == 0:
                print("NO PUEDE DIVIDIR ENTRE CERO.")
                self.errors.append("NO PUEDE DIVIDIR ENTRE CERO.")
                return None

            result.symbol_type = SymbolType.VARIABLE
            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = left.value / right.value
            # result.type_modifier = False
            return result

        elif i.operator == OperationType.MOD:
            if left.data_type != VariableType.lista_variables["NUMBER"] or right.data_type != \
                    VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (%) ENTRE NUMBER.")
                return None

            result.symbol_type = SymbolType.VARIABLE
            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = left.value % right.value
            # result.type_modifier = False
            return result

        elif i.operator == OperationType.POTENCIA:
            if left.data_type != VariableType.lista_variables["NUMBER"] or right.data_type != \
                    VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (^) ENTRE NUMBER.")
                return None

            result.symbol_type = SymbolType.VARIABLE
            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = left.value ** right.value
            # result.type_modifier = False
            return result

        elif i.operator == OperationType.MAYOR_QUE:
            if left.data_type == VariableType.lista_variables["NUMBER"]:
                if right.data_type != VariableType.lista_variables["NUMBER"]:
                    self.errors.append(
                        "SOLO PUEDE REALIZAR OPERACIONES TIPO (>) ENTRE VARIABLE DE TIPO NUMBER O STRING.")
                    return None

                result.symbol_type = SymbolType.VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value > right.value
                # result.type_modifier = False
                return result
            elif left.data_type == VariableType.lista_variables["STRING"]:
                if right.data_type != VariableType.lista_variables["STRING"]:
                    print("SOLO PUEDE REALIZAR OPERACIONES TIPO (>) ENTRE VARIABLE DE TIPO NUMBER O STRING.")
                    self.errors.append(
                        "SOLO PUEDE REALIZAR OPERACIONES TIPO (>) ENTRE VARIABLE DE TIPO NUMBER O STRING.")

                    return None

                result.symbol_type = SymbolType.VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value > right.value
                # result.type_modifier = False
                return result

            else:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (>) ENTRE VARIABLES DE TIPO NUMBER O STRING.")


        elif i.operator == OperationType.MENOR_QUE:
            if left.data_type == VariableType.lista_variables["NUMBER"]:
                if right.data_type != VariableType.lista_variables["NUMBER"]:
                    self.errors.append(
                        "SOLO PUEDE REALIZAR OPERACIONES TIPO (<) ENTRE VARIABLE DE TIPO NUMBER O STRING.")
                    return None

                result.symbol_type = SymbolType.VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value < right.value
                # result.type_modifier = False
                return result
            elif left.data_type == VariableType.lista_variables["STRING"]:
                if right.data_type != VariableType.lista_variables["STRING"]:
                    print("SOLO PUEDE REALIZAR OPERACIONES TIPO (<) ENTRE VARIABLE DE TIPO NUMBER O STRING.")
                    self.errors.append(
                        "SOLO PUEDE REALIZAR OPERACIONES TIPO (<) ENTRE VARIABLE DE TIPO NUMBER O STRING.")

                    return None

                result.symbol_type = SymbolType.VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value < right.value
                # result.type_modifier = False
                return result

            else:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (<) ENTRE VARIABLES DE TIPO NUMBER O STRING.")


        elif i.operator == OperationType.MAYOR_IGUAL_QUE:
            if left.data_type == VariableType.lista_variables["NUMBER"]:
                if right.data_type != VariableType.lista_variables["NUMBER"]:
                    self.errors.append(
                        "SOLO PUEDE REALIZAR OPERACIONES TIPO (>=) ENTRE VARIABLE DE TIPO NUMBER O STRING.")
                    return None

                result.symbol_type = SymbolType.VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value >= right.value
                # result.type_modifier = False
                return result
            elif left.data_type == VariableType.lista_variables["STRING"]:
                if right.data_type != VariableType.lista_variables["STRING"]:
                    print("SOLO PUEDE REALIZAR OPERACIONES TIPO (>=) ENTRE VARIABLE DE TIPO NUMBER O STRING.")
                    self.errors.append(
                        "SOLO PUEDE REALIZAR OPERACIONES TIPO (>=) ENTRE VARIABLE DE TIPO NUMBER O STRING.")

                    return None

                result.symbol_type = SymbolType.VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value >= right.value
                # result.type_modifier = False
                return result

            else:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (>=) ENTRE VARIABLES DE TIPO NUMBER O STRING.")


        elif i.operator == OperationType.MENOR_IGUAL_QUE:
            if left.data_type == VariableType.lista_variables["NUMBER"]:
                if right.data_type != VariableType.lista_variables["NUMBER"]:
                    self.errors.append(
                        "SOLO PUEDE REALIZAR OPERACIONES TIPO (<=) ENTRE VARIABLE DE TIPO NUMBER O STRING.")
                    return None

                result.symbol_type = SymbolType.VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value <= right.value
                # result.type_modifier = False
                return result
            elif left.data_type == VariableType.lista_variables["STRING"]:
                if right.data_type != VariableType.lista_variables["STRING"]:
                    print("SOLO PUEDE REALIZAR OPERACIONES TIPO (<=) ENTRE VARIABLE DE TIPO NUMBER O STRING.")
                    self.errors.append(
                        "SOLO PUEDE REALIZAR OPERACIONES TIPO (<=) ENTRE VARIABLE DE TIPO NUMBER O STRING.")

                    return None

                result.symbol_type = SymbolType.VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value <= right.value
                # result.type_modifier = False
                return result

            else:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (<=) ENTRE VARIABLES DE TIPO NUMBER O STRING.")


        elif i.operator == OperationType.TRIPLE_IGUAL:

            result.data_type = VariableType().buscar_type("BOOLEAN")
            result.value = left.data_type == right.data_type and left.value == right.value
            return result

        elif i.operator == OperationType.DISTINTO_QUE:
            result.data_type = VariableType().buscar_type("BOOLEAN")
            result.value = left.data_type != right.data_type and left.value != right.value
            return result

        elif i.operator == OperationType.OR:
            if left.data_type != VariableType.lista_variables["BOOLEAN"] or right.data_type != \
                    VariableType.lista_variables["BOOLEAN"]:
                print("SOLO PUEDE REALIZAR OPERACIONES TIPO (||) ENTRE VARIABLE DE TIPO BOOLEAN.")
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (||) ENTRE VARIABLE DE TIPO BOOLEAN.")
                return None

            result.data_type = VariableType().buscar_type("BOOLEAN")
            result.value = left.value or right.value
            return result

        elif i.operator == OperationType.AND:
            if left.data_type != VariableType.lista_variables["BOOLEAN"] or right.data_type != \
                    VariableType.lista_variables["BOOLEAN"]:
                print("SOLO PUEDE REALIZAR OPERACIONES TIPO (&&) ENTRE VARIABLE DE TIPO BOOLEAN.")
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (&&) ENTRE VARIABLE DE TIPO BOOLEAN.")
                return None

            result.data_type = VariableType().buscar_type("BOOLEAN")
            result.value = left.value and right.value

            return result

    def visit_break(self, i: Break):
        print("break debug")

    def visit_call_fun(self, i: CallFunction):
        print("callFun debug")

    def visit_console(self, i: ConsoleLog):
        if i.value is None:
            print("ERROR EN CONSOLE LOG NO TIENE VALORES PARA IMPRIMIR.")
            return None

        content = ""
        for value in i.value:
            result = value.accept(self)
            if result is None:
                print("NO SE PUDO REALIZAR LA OPERACIÓN.")
                continue

            content = content + " " + str(result.value)

        print(content)

    def visit_continue(self, i: Continue):
        print("continue debug")

    def visit_declaration(self, i: Declaration):
        if i.type is None:
            self.errors.append("ERROR EN DECLARACION DE VARIABLE NO TIENE TIPO DE VARIABLE.")

            return None
        for instruction in i.instructions:
            variable: Variable = instruction.accept(self)

            if variable is None:
                self.errors.append("NO SE PUDO DECLARAR LA VARIABLE.")
                return None

            if self.symbol_table.var_in_table(variable.id):
                self.errors.append("VARIABLE YA DECLARADA.")
                return None

            self.symbol_table.add_variable(variable)
            # print(variable.data_type)
            # print("DECLARACION DE VARIABLE EXITOSA.")
            print(self.symbol_table.__str__())

    def visit_else(self, i: ElseState):
        temporal_table = SymbolTable(self.symbol_table)
        self.symbol_table = temporal_table
        for instruction in i.bloque:
            instruction.accept(self)

        self.symbol_table = self.symbol_table.parent
        return None

    def visit_foreach(self, i: ForEachState):
        print("foreach debug")

    def visit_for(self, i: ForState):
        print("for debug")
        for instruction in i.instructions:
            instruction.accept(self)

    def visit_function(self, i: FunctionState):
        print("function debug")

    def visit_if(self, i: IfState):
        condition: Variable = i.condition.accept(self)

        if condition is None:
            self.errors.append("NO SE PUDO REALIZAR LA OPERACIÓN")

        else:

            if condition.data_type != VariableType().buscar_type("BOOLEAN"):
                self.errors.append("LA CONDICIÓN DEBE SER TIPO BOOLEAN")

        temporal_table = SymbolTable(self.symbol_table)
        self.symbol_table = temporal_table

        for instruction in i.bloque_verdadero:
            instruction.accept(self)

        self.symbol_table = self.symbol_table.parent

        if i.bloque_falso:
            i.bloque_falso.accept(self)

    def visit_interface(self, i: InterfaceState):
        print("interface debug")

    def visit_native(self, i: NativeFunction):
        print("native debug")

    def visit_only_assign(self, i: OnlyAssignment):
        variable: Variable = self.symbol_table.find_var_by_id(i.id)

        if variable is None:
            self.errors.append("NO SE ENCONTRÓ LA VARIABLE")
            return None

        value: Variable = i.value.accept(self)

        if value is None:
            self.errors.append("NO SE PUDO REALIZAR LA ASIGNACIÓN")
            return None

        if variable.isAny:
            variable.data_type = value.data_type
            variable.value = value.value
            return None

        if variable.data_type != value.data_type:
            self.errors.append("LOS TIPOS NO COINCIDEN")
            return None

        variable.value = value.value
        return None

    def visit_parameter(self, i: Parameter):
        print("parameter debug")

    def visit_return(self, i: Return):
        print("return debug")

    def visit_unary_op(self, i: UnaryOperation):
        right = i.right_operator.accept(self)

        if right is None:
            self.errors.append("NO SE PUDO REALIZAR LA OPERACIÓN UNARIA.")
            return None

        result = Variable()

        if i.operator == OperationType.NEGATIVE:
            if right.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO SE PUEDE REALIZAR OPERACIONES TIPO (-) ENTRE VARIABLES TIPO NUMBER")
                return None

            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = -right.value
            return result
        if i.operator == OperationType.POSITIVE:
            if right.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO SE PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE VARIABLES TIPO NUMBER")
                return None

            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = right.value
            return result
        if i.operator == OperationType.NOT:
            if right.data_type != VariableType.lista_variables["BOOLEAN"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (!) UNARIO ENTRE VARIABLES TIPO BOOLEAN.")
                return None

            result.data_type = VariableType().buscar_type("BOOLEAN")
            result.value = not right.value
            return result
        if i.operator == OperationType.INCREMENT:
            if right.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (++) UNARIO ENTRE VARIABLE DE TIPO NUMBER.")
                return None

            var = self.symbol_table.find_var_by_id(right.id)

            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = right.value + 1
            var.value = result.value
            return result
        if i.operator == OperationType.DECREMENT:
            if right.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (--) UNARIO ENTRE VARIABLE DE TIPO NUMBER.")
                return None

            var = self.symbol_table.find_var_by_id(right.id)

            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = right.value - 1
            var.value = result.value
            return result

    def visit_while(self, i: WhileState):
        condition: Variable = i.condition.accept(self)

        if condition is None:
            self.errors.append("NO SE PUDO REALIZAR LA OPERACIÓN BOOLEANA")

        else:

            if condition.data_type != VariableType().buscar_type("BOOLEAN"):
                self.errors.append("LA CONDICIÓN DEBE DE SER TIPO BOOLEAN")

        temporal_table = SymbolTable(self.symbol_table)
        self.symbol_table = temporal_table
        for instruction in i.instructions:
            instruction.accept(self)

        self.symbol_table = self.symbol_table.parent

    def visit_value(self, i: Value):
        result = Variable()
        if i.value_type == ValueType.CADENA:
            result.data_type = VariableType().buscar_type("STRING")
            result.value = str(i.value)
            return result
        elif i.value_type == ValueType.ENTERO:
            result.data_type = VariableType().buscar_type("NUMBER")
            # print("VALUE DESDE VALUE: "+result.data_type)

            result.value = int(i.value)
            return result
        elif i.value_type == ValueType.DECIMAL:
            result.data_type = VariableType().buscar_type("NUMBER")
            # print("VALUE DESDE VALUE: "+result.data_type)
            result.value = float(i.value)
            return result
        elif i.value_type == ValueType.BOOLEANO:
            result.data_type = VariableType().buscar_type("BOOLEAN")
            result.value = True if i.value == "true" else False
            return result
        elif i.value_type == ValueType.LITERAL:
            var_in_table = self.symbol_table.find_var_by_id(str(i.value))
            if var_in_table is None:
                self.errors.append("NO SE ENCONTRÓ LA VARIABLE: " + i.value + " EN LA TABLA DE SIMBOLOS")
                return None

            result = copy.deepcopy(var_in_table)
            return result
