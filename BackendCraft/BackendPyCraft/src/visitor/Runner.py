import copy

from .Visitor import Visitor
from ..models import Assignment, Parameter
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
from ..models import NativeFunction
from ..models import OnlyAssignment
from ..models import Return
from ..models import UnaryOperation
from ..models import WhileState
from ..models import Value
from ..models.Variable import Variable
from ..models.SymbolType import SymbolType
from ..symbolTable.SymbolTable import SymbolTable
from ..models.VariableType import VariableType
from ..models.ValueType import ValueType
from ..models.OperationType import OperationType
import copy


class Runner(Visitor):

    def __init__(self, symbol_table: SymbolTable, errors):
        super().__init__()
        self.symbol_table = symbol_table
        self.errors = errors

    def visit_assignment(self, i: Assignment):
        variable = Variable()
        if(self.symbol_table.var_in_table(i.id)):
            self.errors.append("LA VARIABLE YA ESTA DECLARADA")
            print("LA VARIABLE YA ESTA DECLARADA")
            return None
        else:
            if i.isAny is True:
                variable.isAny = True
            else:
                variable.isAny = False

            if i.value is None:
                variable.id = i.id
                if i.type == VariableType.lista_variables["NUMBER"]:
                    variable.data_type = VariableType().buscar_type("NUMBER")
                    variable.symbol_type = SymbolType().VARIABLE
                    variable.value = 0
                    return variable
                elif i.type == VariableType.lista_variables["STRING"]:
                    variable.data_type = VariableType().buscar_type("STRING")
                    variable.symbol_type = SymbolType().VARIABLE
                    variable.value = ""
                    return variable
                elif i.type == VariableType.lista_variables["BOOLEAN"]:
                    variable.data_type = VariableType().buscar_type("BOOLEAN")
                    variable.symbol_type = SymbolType().VARIABLE
                    variable.value = False
                    return variable
                elif i.type == VariableType.lista_variables["NULL"]:
                    variable.data_type = VariableType().buscar_type("NULL")
                    variable.symbol_type = SymbolType().VARIABLE
                    variable.value = ''
                    return variable
                elif i.type == VariableType.lista_variables["ANY"]:
                    variable.data_type = VariableType().buscar_type("ANY")
                    variable.symbol_type = SymbolType().VARIABLE
                    variable.value = None
                    return variable
                elif i.type is None:
                    variable.data_type = VariableType().buscar_type("STRING")
                    variable.symbol_type = SymbolType().VARIABLE
                    variable.value = ''
                    return variable
            else:
                value = Variable()
                value: Variable = i.value.accept(self)
                if value is not None:
                    if i.type == value.data_type:
                        variable.id = i.id
                        variable.data_type = value.data_type
                        variable.symbol_type = SymbolType().VARIABLE
                        variable.value = value.value
                        return variable
                    elif i.isAny:
                        variable.id = i.id
                        variable.data_type = value.data_type
                        variable.symbol_type = SymbolType().VARIABLE
                        variable.value = value.value
                        return variable
                    else:
                        self.errors.append("LA VARIABLE NO ES DEL MISMO TIPO")
                        print("LA VARIABLE NO ES DEL MISMO TIPO")
                        return None
                else:
                    print("NO EXISTE VALOR")
                    self.errors.append("NO EXISTE VALOR")
                    return None


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
                    print("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE VARIABLES DEL MISMO TIPO.")
                    self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE VARIABLES DEL MISMO TIPO.")
                    return None

                result.symbol_type = SymbolType.VARIABLE
                result.data_type = VariableType().buscar_type("NUMBER")
                result.value = left.value + right.value
                # result.type_modifier = False
                return result
            elif left.data_type == VariableType.lista_variables["STRING"]:
                if right.data_type != VariableType.lista_variables["STRING"]:
                    print("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE VARIABLES DEL MISMO TIPO.")
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
            result.value = left.value != right.value
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
        pass

    def visit_call_fun(self, i: CallFunction):
        pass

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
        pass

    def visit_declaration(self, i: Declaration):
        if i.instructions is None:
            self.errors.append("ERROR EN DECLARACION DE VARIABLE NO TIENE VALORES PARA ASIGNAR.")
            print("ERROR EN DECLARACION DE VARIABLE NO TIENE VALORES PARA ASIGNAR.")
            return None
        if i.type is None:
            self.errors.append("ERROR EN DECLARACION DE VARIABLE NO TIENE TIPO DE VARIABLE.")
            return None
        for elemento in i.instructions:
            vr1: Variable = Variable()
            vr1 = elemento.accept(self)
            if elemento is not None:
                asigment: Variable = elemento.accept(self)
                if asigment is not None:
                    vr1.type_modifier = i.type
                    vr1.id = asigment.id
                    vr1.value = asigment.value
                    vr1.data_type = asigment.data_type
                    vr1.symbol_type = SymbolType().VARIABLE
                    self.symbol_table.add_variable(vr1)
                    print("DECLARACION DE VARIABLE EXITOSA.")
                    print(self.symbol_table.__str__())
                else:
                    self.errors.append("ERROR EN DECLARACION DE VARIABLE NO SE PUDO ASIGNAR VALOR.")
                    print("ERROR EN DECLARACION DE VARIABLE NO SE PUDO ASIGNAR VALOR.")
                    return None


    def visit_else(self, i: ElseState):
        pass

    def visit_foreach(self, i: ForEachState):
        pass

    def visit_for(self, i: ForState):
        pass

    def visit_function(self, i: FunctionState):
        pass

    def visit_if(self, i: IfState):
        pass

    def visit_interface(self, i: InterfaceState):
        pass

    def visit_native(self, i: NativeFunction):
        pass

    def visit_only_assign(self, i: OnlyAssignment):
        pass

    def visit_parameter(self, i: Parameter):
        pass

    def visit_return(self, i: Return):
        pass

    def visit_unary_op(self, i: UnaryOperation):
        right = i.right_operator.accept(self)

        if right is None:
            self.errors.append("NO SE PUDO REALIZAR LA OPERACIÓN UNARIA.")
            return None
        result = Variable()
        if i.operator == OperationType.NEGATIVE:
            if right.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (-) UNARIO ENTRE VARIABLE DE TIPO NUMBER.")
                return None

            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = -right.value
            return result

        elif i.operator == OperationType.POSITIVE:
            if right.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) UNARIO ENTRE VARIABLE DE TIPO NUMBER.")
                return None

            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = right.value
            return result

        elif i.operator == OperationType.NOT:
            if right.data_type != VariableType.lista_variables["BOOLEAN"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (!) UNARIO ENTRE VARIABLE DE TIPO BOOLEAN.")
                return None

            result.data_type = VariableType().buscar_type("BOOLEAN")
            result.value = not right.value
            return result

        elif i.operator == OperationType.INCREMENTO:
            if right.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (++) UNARIO ENTRE VARIABLE DE TIPO NUMBER.")
                return None

            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = right.value + 1
            return result

        elif i.operator == OperationType.DECREMENTO:
            if right.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (--) UNARIO ENTRE VARIABLE DE TIPO NUMBER.")
                return None

            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = right.value - 1
            return result

    def visit_while(self, i: WhileState):
        pass

    def visit_value(self, i: Value):
        variable = Variable()
        if i.value_type == ValueType.CADENA:
            variable.data_type = VariableType().buscar_type("STRING")
            variable.value = str(i.value)
            return variable
        elif i.value_type == ValueType.ENTERO:
            variable.data_type = VariableType().buscar_type("NUMBER")
            variable.value = int(i.value)
            return variable
        elif i.value_type == ValueType.DECIMAL:
            variable.data_type = VariableType().buscar_type("NUMBER")
            variable.value = float(i.value)
            return variable
        elif i.value_type == ValueType.BOOLEANO:
            variable.data_type = VariableType().buscar_type("BOOLEAN")
            variable.value = True if i.value == "true" else False
            return variable
        elif i.value_type == ValueType.LITERAL:
            var_in_table = self.symbol_table.var_in_table(i.value)
            if var_in_table is None:
                print("NO SE ENCONTRÓ LA VARIABLE: " + i.value + " EN LA TABLA DE SIMBOLOS")
                return None

            variable = copy.deepcopy(var_in_table)
            return variable
