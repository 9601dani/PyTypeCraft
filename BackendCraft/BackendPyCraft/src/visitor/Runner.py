from .Visitor import Visitor
from ..models import Assignment, Parameter
from ..models import ArrayState, ArrayAssign
from ..models import BinaryOperation
from ..models import Break
from ..models import CallArray
from ..models import CallAttribute
from ..models import CallFunction
from ..models import ConsoleLog
from ..models import Continue
from ..models import Declaration
from ..models import ElseState
from ..models import ForEachState
from ..models import ForState
from ..models import FunctionState
from ..models import IfState
from ..models import InterfaceAssign
from ..models import InterAttributeAssign
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
from ..models.NativeFunType import NativeFunType
from ..models.InterfaceState import InterfaceState
from ..symbolModel.InterfaceModel import InterfaceModel
from ..symbolModel.FunctionModel import FunctionModel
from ..symbolTable.ScopeType import ScopeType
from ..symbolModel.ArrayModel import ArrayModel
from ..models.Continue import Continue
from ..models.Break import Break
from ..models.Return import Return
from ..models.Value import Value
from ..ObjectError.ExceptionPyType import ExceptionPyType
import copy
from decimal import Decimal


class Runner(Visitor):

    def __init__(self, symbol_table: SymbolTable, errors, console):
        super().__init__()
        self.symbol_table = symbol_table
        self.errors = errors
        self.console = console

    def visit_assignment(self, i: Assignment):
        result = Variable()
        # print("isAny:" + str(i.isAny))
        result.id = i.id
        # print("VARIABLE EN ASSIGNMENT: ",i.id)

        if i.value is None:
            if i.type == VariableType().buscar_type("NUMBER"):
                result.data_type = VariableType().buscar_type("NUMBER")
                result.symbol_type = SymbolType().VARIABLE
                result.isAny = False
                result.value = 0
                return result
            elif i.isAny:
                result.data_type = VariableType().buscar_type("STRING")
                result.symbol_type = SymbolType().VARIABLE
                result.isAny = True
                result.value = ""
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
                # print("ENTRANDO EN", i.id)
                result.data_type = VariableType().buscar_type(i.id)
                result.symbol_type = SymbolType().VARIABLE
                result.isAny = False

                result.value = None
                return result

        else:
            value: Variable = i.value.accept(self)
            # print(i.type)
            if value is None:
                self.errors.append(ExceptionPyType("El valor de la asignación no es válido", i.line, i.column))
                # print("NO SE PUDO REALIZAR LA ASIGNACIÓN")
                return None

            if value.symbol_type == SymbolType().ARRAY:
                # print("DECLARANDO UN ARREGLO",value.data_type)
                if i.type is None or i.type == VariableType().buscar_type("ANY"):
                    result.data_type = value.data_type
                    result.symbol_type = SymbolType().ARRAY
                    result.isAny = True
                    result.value = value.value
                    return result

                if value.isAny:
                    self.errors.append(ExceptionPyType("NO SE PUEDE ASIGNAR UN ARREGLO ANY A UNA VARIABLE QUE NO LO ES", i.line, i.column))
                    return None

                if i.type != value.data_type:
                    self.errors.append(ExceptionPyType("LOS TIPOS DE DATO NO COINCIDEN", i.line, i.column))
                    return None

                result.data_type = value.data_type
                result.symbol_type = SymbolType().ARRAY
                result.isAny = False
                result.value = value.value
                return result

            if i.type is None or i.type == VariableType().buscar_type("ANY"):
                # print("VALUE ASSIG: "+value.data_type)
                result.data_type = value.data_type
                result.symbol_type = SymbolType().VARIABLE
                result.value = value.value
                result.isAny = True
                return result

            if value.data_type == VariableType().buscar_type("DEFINIRLA"):
                if not VariableType().type_declared(i.type):
                    self.errors.append(ExceptionPyType("No se encontro la variable de la interfaz", i.line, i.column))
                    return None

                interface = self.symbol_table.find_interface_by_id(i.type)

                if interface is None:
                    self.errors.append(ExceptionPyType("NO SE ENCONTRÓ LA INTERFAZ", i.line, i.column))
                    return None

                model: InterfaceModel = interface.value
                valueModel: InterfaceModel = value.value

                if len(model.attributes) != len(valueModel.attributes):
                    self.errors.append(ExceptionPyType("EL NÚMERO DE ATRIBUTOS NO COINCIDE", i.line, i.column))
                    return None

                for attr in model.attributes:
                    attrInValue = None
                    for valueAttr in valueModel.attributes:
                        if attr.id == valueAttr.id:
                            attrInValue = valueAttr
                            break

                    if attrInValue is None:
                        self.errors.append(ExceptionPyType("NO SE ENCONTRÓ EL ATRIBUTO: " + attr.id, i.line, i.column))
                        return None

                    if attr.data_type != attrInValue.data_type:
                        self.errors.append(ExceptionPyType("LOS TIPOS DE ATRIBUTOS NO COINCIDEN", i.line, i.column))
                        return None

                result.data_type = i.type
                result.symbol_type = SymbolType().VARIABLE
                result.value = valueModel
                result.isAny = False

                return result

            if i.type != value.data_type:
                # print(str(value.data_type))
                self.errors.append(ExceptionPyType("LA VARIABLE NO ES DEL MISMO TIPO", i.line, i.column))
                # print("LA VARIABLE NO ES DEL MISMO TIPO")
                return None

            result.data_type = value.data_type
            result.symbol_type = SymbolType().VARIABLE
            result.isAny = False
            result.value = value.value
            return result

    def visit_array_assign(self, i: ArrayAssign):
        variable: Variable = self.symbol_table.find_var_by_id(i.id)

        if variable is None:
            self.errors.append(ExceptionPyType("NO SE ENCONTRO EL ARRAY"+i.id,i.line,i.column))
            return None

        if variable.symbol_type != SymbolType().ARRAY:
            self.errors.append(ExceptionPyType("LA VARIABLE NO ES UN ARRAY",i.line,i.column))
            return None

        current_var = variable

        for dimension in i.dimensions:
            index: Variable = dimension.accept(self)

            if index is None:
                self.errors.append(ExceptionPyType("NO SE PUDO REALIZAR LA OPERACIÓN, EL INDICE ES NULO",i.line,i.column))
                return None

            if index.data_type != VariableType().buscar_type("NUMBER"):
                self.errors.append(ExceptionPyType("EL ÍNDICE DEBE SER TIPO NUMBER",i.line,i.column))
                return None

            if current_var.symbol_type != SymbolType().ARRAY:
                self.errors.append(ExceptionPyType("DIMENSIÓN NO ENCONTRADA",i.line,i.column))
                return None

            current_model: ArrayModel = current_var.value

            if int(index.value) > current_model.len-1:
                self.errors.append(ExceptionPyType("INDICE FUERA DE LOS LÍMITES SE ESPERABA: "+str(current_model.len-1)+" PERO SE OBTUVO:"+str(index.value),i.line,i.column))
                return None

            for ind in range(int(index.value)):
                current_model = current_model.next

            current_var = current_model.var

        value: Variable = i.value.accept(self)

        if value is None:
            self.errors.append(ExceptionPyType("NO SE PUDO REALIZAR LA OPERACIÓN",i.line,i.column))
            return None

        if variable.isAny:
            current_var.value = value.value
            return current_var

        if variable.data_type != value.data_type:
            self.errors.append(ExceptionPyType("INCOMPATIBILIDAD DE TIPOS",i.line,i.column))
            return None

        current_var.value = value.value
        return current_var

    def visit_array_state(self, i: ArrayState):
        first_node = None
        result = Variable()
        result.symbol_type = SymbolType.ARRAY
        result.isAny = False

        for value in i.values:
            var:Variable = value.accept(self)

            if var is None:
                self.errors.append(ExceptionPyType("NO SE PUDO REALIZAR LA OPERACION, ES NULA", i.line, i.column))
                return None

            current_node = ArrayModel(var)

            if first_node is None:
                first_node = current_node
                result.data_type = var.data_type
                #print("AGREGANDO PRIMER NODO")
            else:
                next_node: ArrayModel = first_node

                while next_node.next is not None:
                    next_node = next_node.next

                next_node.next = current_node
                first_node.len = first_node.len + 1
                #print("AGREGANDO OTRO NODO RUN")

                if result.data_type != var.data_type:
                    first_node.isAny = True

        result.value = first_node
        return result

    def visit_binary_op(self, i: BinaryOperation):
        left = i.left_operator.accept(self)
        right = i.right_operator.accept(self)

        if left is None or right is None:
            self.errors.append(ExceptionPyType("NO SE PUDO REALIZAR LA OPERACIÓN", i.line, i.column))
            return None

        if left.symbol_type == SymbolType().ARRAY or right.symbol_type == SymbolType().ARRAY or left.symbol_type == SymbolType().INTERFACE or right.symbol_type == SymbolType().INTERFACE:
            self.errors.append(ExceptionPyType("SOLO PUEDES REALIZAR OPERACIONES ENTRE VARIABLES", i.line, i.column))
            return None

        result = Variable()

        if left.symbol_type == SymbolType().FUNCTION:
            return self.assignDefaultValue(right.data_type)
        elif right.symbol_type == SymbolType().FUNCTION:
            return self.assignDefaultValue(left.data_type)

        if i.operator == OperationType.MAS:
            if left.data_type == VariableType().buscar_type("NUMBER"):
                if right.data_type != VariableType().buscar_type("NUMBER"):
                    # print("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE VARIABLES DEL MISMO TIPO.")
                    self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE NUMBER.", i.line, i.column))
                    return None

                result.symbol_type = SymbolType().VARIABLE
                result.data_type = VariableType().buscar_type("NUMBER")
                result.value = Decimal(left.value) + Decimal(right.value)
                result.isAny = False

                # result.type_modifier = False
                return result
            elif left.data_type == VariableType().buscar_type("STRING"):
                if right.data_type != VariableType().buscar_type("STRING"):
                    # print("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE VARIABLES DEL MISMO TIPO.")
                    self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE STRING.", i.line, i.column))
                    return None

                result.symbol_type = SymbolType().VARIABLE
                result.data_type = VariableType().buscar_type("STRING")
                result.value = left.value + right.value
                result.isAny = False

                # result.type_modifier = False
                return result

            else:
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE NUMBER Y STRING.", i.line, i.column))


        elif i.operator == OperationType.MENOS:
            if left.data_type != VariableType().buscar_type("NUMBER") or right.data_type != \
                    VariableType().buscar_type("NUMBER"):
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (-) ENTRE NUMBER.", i.line, i.column))
                return None

            result.symbol_type = SymbolType().VARIABLE
            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = left.value - right.value
            result.isAny = False
            # result.type_modifier = False
            return result

        elif i.operator == OperationType.TIMES:
            if left.data_type != VariableType().buscar_type("NUMBER") or right.data_type != \
                    VariableType().buscar_type("NUMBER"):
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (*) ENTRE NUMBER.", i.line, i.column))
                return None

            result.symbol_type = SymbolType().VARIABLE
            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = left.value * right.value
            result.isAny = False

            # result.type_modifier = False
            return result

        elif i.operator == OperationType.DIVIDE:
            if left.data_type != VariableType().buscar_type("NUMBER") or right.data_type != \
                    VariableType().buscar_type("NUMBER"):
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (/) ENTRE NUMBER.", i.line, i.column))
                return None

            if right.value == 0:
                # print("NO PUEDE DIVIDIR ENTRE CERO.")
                self.errors.append(ExceptionPyType("NO PUEDE DIVIDIR ENTRE CERO.", i.line, i.column))
                return None

            result.symbol_type = SymbolType().VARIABLE
            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = left.value / right.value
            result.isAny = False
            # result.type_modifier = False
            return result

        elif i.operator == OperationType.MOD:
            if left.data_type != VariableType().buscar_type("NUMBER") or right.data_type != \
                    VariableType().buscar_type("NUMBER"):
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (%) ENTRE NUMBER.", i.line, i.column))
                return None

            result.symbol_type = SymbolType().VARIABLE
            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = left.value % right.value
            result.isAny = False

            # result.type_modifier = False
            return result

        elif i.operator == OperationType.POTENCIA:
            if left.data_type != VariableType().buscar_type("NUMBER") or right.data_type != \
                    VariableType().buscar_type("NUMBER"):
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (^) ENTRE NUMBER.", i.line, i.column))
                return None

            result.symbol_type = SymbolType().VARIABLE
            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = left.value ** right.value
            result.isAny = False

            # result.type_modifier = False
            return result

        elif i.operator == OperationType.MAYOR_QUE:
            if left.data_type == VariableType().buscar_type("NUMBER"):
                if right.data_type != VariableType().buscar_type("NUMBER"):
                    self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (>) ENTRE VARIABLE DE TIPO NUMBER O STRING.", i.line, i.column))
                    return None

                result.symbol_type = SymbolType().VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value > right.value
                result.isAny = False

                # result.type_modifier = False
                return result
            elif left.data_type == VariableType().buscar_type("STRING"):
                if right.data_type != VariableType().buscar_type("STRING"):
                    # print("SOLO PUEDE REALIZAR OPERACIONES TIPO (>) ENTRE VARIABLE DE TIPO NUMBER O STRING.")
                    self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (>) ENTRE VARIABLE DE TIPO NUMBER O STRING.", i.line, i.column))
                    return None

                result.symbol_type = SymbolType().VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value > right.value
                result.isAny = False

                # result.type_modifier = False
                return result

            else:
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (>) ENTRE VARIABLE DE TIPO NUMBER O STRING.", i.line, i.column))


        elif i.operator == OperationType.MENOR_QUE:
            if left.data_type == VariableType().buscar_type("NUMBER"):
                if right.data_type != VariableType().buscar_type("NUMBER"):
                    self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (<) ENTRE VARIABLE DE TIPO NUMBER O STRING.", i.line, i.column))
                    return None

                result.symbol_type = SymbolType().VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value < right.value
                result.isAny = False

                # result.type_modifier = False
                return result
            elif left.data_type == VariableType().buscar_type("STRING"):
                if right.data_type != VariableType().buscar_type("STRING"):
                    # print("SOLO PUEDE REALIZAR OPERACIONES TIPO (<) ENTRE VARIABLE DE TIPO NUMBER O STRING.")
                    self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (<) ENTRE VARIABLE DE TIPO NUMBER O STRING.", i.line, i.column))
                    return None

                result.symbol_type = SymbolType().VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value < right.value
                result.isAny = False

                # result.type_modifier = False
                return result

            else:
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (<) ENTRE VARIABLES DE TIPO NUMBER O STRING.", i.line, i.column))


        elif i.operator == OperationType.MAYOR_IGUAL_QUE:
            if left.data_type == VariableType().buscar_type("NUMBER"):
                if right.data_type != VariableType().buscar_type("NUMBER"):
                    self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (>=) ENTRE VARIABLE DE TIPO NUMBER O STRING.", i.line, i.column))
                    return None

                result.symbol_type = SymbolType().VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value >= right.value
                result.isAny = False

                # result.type_modifier = False
                return result
            elif left.data_type == VariableType().buscar_type("STRING"):
                if right.data_type != VariableType().buscar_type("STRING"):
                    # print("SOLO PUEDE REALIZAR OPERACIONES TIPO (>=) ENTRE VARIABLE DE TIPO NUMBER O STRING.")
                    self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (>=) ENTRE VARIABLE DE TIPO NUMBER O STRING.", i.line, i.column))
                    return None

                result.symbol_type = SymbolType().VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value >= right.value
                result.isAny = False

                # result.type_modifier = False
                return result

            else:
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (>=) ENTRE VARIABLES DE TIPO NUMBER O STRING.", i.line, i.column))


        elif i.operator == OperationType.MENOR_IGUAL_QUE:
            if left.data_type == VariableType().buscar_type("NUMBER"):
                if right.data_type != VariableType().buscar_type("NUMBER"):
                    self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (<=) ENTRE VARIABLE DE TIPO NUMBER O STRING.", i.line, i.column))
                    return None

                result.symbol_type = SymbolType().VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value <= right.value
                result.isAny = False

                # result.type_modifier = False
                return result
            elif left.data_type == VariableType().buscar_type("STRING"):
                if right.data_type != VariableType().buscar_type("STRING"):
                    # print("SOLO PUEDE REALIZAR OPERACIONES TIPO (<=) ENTRE VARIABLE DE TIPO NUMBER O STRING.")
                    self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (<=) ENTRE VARIABLE DE TIPO NUMBER O STRING.", i.line, i.column))

                    return None

                result.symbol_type = SymbolType().VARIABLE
                result.data_type = VariableType().buscar_type("BOOLEAN")
                result.value = left.value <= right.value
                result.isAny = False

                # result.type_modifier = False
                return result

            else:
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (<=) ENTRE VARIABLES DE TIPO NUMBER O STRING.", i.line, i.column))


        elif i.operator == OperationType.TRIPLE_IGUAL:

            result.data_type = VariableType().buscar_type("BOOLEAN")
            result.value = left.data_type == right.data_type and left.value == right.value
            result.symbol_type = SymbolType().VARIABLE
            result.isAny = False
            return result

        elif i.operator == OperationType.DISTINTO_QUE:
            result.data_type = VariableType().buscar_type("BOOLEAN")
            result.value = left.value != right.value
            result.symbol_type = SymbolType().VARIABLE
            result.isAny = False
            return result

        elif i.operator == OperationType.OR:
            if left.data_type != VariableType().lista_variables("BOOLEAN") or right.data_type != \
                    VariableType().lista_variables("BOOLEAN"):
                # print("SOLO PUEDE REALIZAR OPERACIONES TIPO (||) ENTRE VARIABLE DE TIPO BOOLEAN.")
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (||) ENTRE VARIABLE DE TIPO BOOLEAN.",i.line,i.column))
                return None

            result.data_type = VariableType().buscar_type("BOOLEAN")
            result.value = left.value or right.value
            result.symbol_type = SymbolType().VARIABLE
            result.isAny = False
            return result

        elif i.operator == OperationType.AND:
            if left.data_type != VariableType().lista_variables("BOOLEAN") or right.data_type != \
                    VariableType().lista_variables("BOOLEAN"):
                # print("SOLO PUEDE REALIZAR OPERACIONES TIPO (&&) ENTRE VARIABLE DE TIPO BOOLEAN.")
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (&&) ENTRE VARIABLE DE TIPO BOOLEAN.",i.line,i.column))
                return None

            result.data_type = VariableType().buscar_type("BOOLEAN")
            result.value = left.value and right.value
            result.symbol_type = SymbolType().VARIABLE
            result.isAny = False

            return result


    def visit_break(self, i: Break):
        if self.symbol_table.parent is None:
            self.errors.append(ExceptionPyType("BREAK FUERA DE CICLO", i.line, i.column))
            return None
        else:
            return i

    def visit_call_arr(self, i: CallArray):
        variable: Variable = self.symbol_table.find_var_by_id(i.id)

        if variable is None:
            self.errors.append(ExceptionPyType("NO SE ENCONTRÓ EL ARRAY: "+i.id, i.line, i.column))
            return None

        if variable.symbol_type != SymbolType().ARRAY:
            self.errors.append(ExceptionPyType("LA VARIABLE NO ES UN ARRAY", i.line, i.column))
            return None

        current_var = variable

        for dimension in i.dimensions:
            index: Variable = dimension.accept(self)

            if index is None:
                self.errors.append(ExceptionPyType("NO SE PUDO REALIZAR LA OPERACIÓN EL INDEX NO ES VALIDO", i.line, i.column))
                return None

            if index.data_type != VariableType().buscar_type("NUMBER"):
                self.errors.append(ExceptionPyType("EL ÍNDICE DEBE SER TIPO NUMBER", i.line, i.column))
                return None

            if current_var.symbol_type != SymbolType().ARRAY:
                self.errors.append(ExceptionPyType("DIMENSION NO ENCONTRADA", i.line, i.column))
                return None

            current_model: ArrayModel = current_var.value

            if int(index.value) > current_model.len-1:
                self.errors.append(ExceptionPyType("INDICE FUERA DE LOS LÍMITES SE ESPERABA: "+str(current_model.len-1)+" PERO SE OBTUVO: "+str(index.value), i.line, i.column))
                return None

            for i in range(int(index.value)):
                current_model = current_model.next

            current_var = current_model.var

        return current_var

    def visit_call_attr(self, i: CallAttribute):
        value: Variable = i.id.accept(self)

        if value is None:
            self.errors.append(ExceptionPyType("NO SE ENCONTRÓ LA VARIABLE", i.line, i.column))
            return None

        if not isinstance(value.value, InterfaceModel):
            self.errors.append(ExceptionPyType("LA VARIABLE NO ES DE TIPO INTERFACE", i.line, i.column))
            return None

        model: InterfaceModel = value.value

        for attribute in model.attributes:
            if attribute.id == i.attr:
                return attribute
        self.errors.append(ExceptionPyType("NO SE ENCONTRÓ EL ATRIBUTO: "+i.attr, i.line, i.column))
        return None

    def visit_call_fun(self, i: CallFunction):
        #TODO: PRUEBA DE MODIFICACIÓN EN CALL_FUN

        arguments = []

        for argument in i.assignments:
            value = argument.accept(self)

            if value is None:
                self.errors.append(ExceptionPyType("ERROR EN ASIGNACIÓN DE VALORES EN FUNCIÓN.", i.line, i.column))
                return None

            arguments.append(value)
            # print("AGREGANDO ARGUMENTO: "+value.__str__())

        if i.name == "typeof":
            if len(arguments) != 1:
                self.errors.append(ExceptionPyType("LA FUNCIÓN TYPEOF ESPERABA SOLO UN ARGUMENTO", i.line, i.column))
                return None

            result = Variable()
            result.symbol_type = SymbolType().VARIABLE
            result.value = arguments[0].data_type
            result.data_type = VariableType().buscar_type("STRING")
            result.isAny = False
            return result

        elif i.name == "toString":
            if len(arguments) != 1:
                self.errors.append(ExceptionPyType("LA FUNCIÓN TOSTRING ESPERABA SOLO UN ARGUMENTO", i.line, i.column))
                return None

            result = Variable()
            result.symbol_type = SymbolType().VARIABLE
            result.value = str(arguments[0].value)
            result.data_type = VariableType().buscar_type("STRING")
            result.isAny = False
            return result

        match_fun:FunctionModel = self.get_fun(i.name, arguments)

        if match_fun is None:
            self.errors.append(ExceptionPyType("NO SE ENCONTRÓ LA FUNCIÓN, REVISA EL TIPO DE PARAMETROS", i.line, i.column))
            return None

        #print("FUNCIÓN: "+match_fun.id)
        # CREANDO NUEVO SCOPE PARA LA FUNCIÓN
        temp_table = SymbolTable(self.symbol_table, ScopeType.FUNCTION_SCOPE)
        self.symbol_table = temp_table
        # AGREGANDO LOS ARGUMENTOS CON SUS PARÁMETROS A LA TABLA DE SIMBOLOS
        for i in range(len(match_fun.parameters)):
            match_fun.parameters[i].value = arguments[i].value
            match_fun.parameters[i].symbol_type = arguments[i].symbol_type
            match_fun.parameters[i].data_type = arguments[i].data_type
            print(f'####### AGREGANDO -> {match_fun.parameters[i].__str__()}###############')
            self.symbol_table.add_variable(match_fun.parameters[i])

        for instruction in match_fun.instructions:
            #print("EJECUTANDO INSTRUCCIONES EN CALLFUNCTION")
            result = instruction.accept(self)
            if result is not None:
                if result.__class__.__name__ == "Return":
                    vr_return:Variable = result.expression.accept(self)
                    self.symbol_table = self.symbol_table.parent
                    if(vr_return is not None):
                        vr_return.isAny = True

                        #print("RETORNANDO VALOR: "+vr_return.__str__() )
                        if match_fun.return_type is not None:
                            if match_fun.return_type != vr_return.data_type:
                                if(type(i)== int):
                                    print(i)
                                    self.errors.append(ExceptionPyType("EL TIPO DE RETORNO NO COINCIDE CON EL TIPO DE LA FUNCIÓN: "+match_fun.id, 1))
                                    return None
                                else:
                                    self.errors.append(ExceptionPyType("EL TIPO DE RETORNO NO COINCIDE CON EL TIPO DE LA FUNCIÓN", i.line, i.column))
                                    return None

                        return vr_return
                    else:
                        return None
        self.symbol_table = self.symbol_table.parent
        return None

    def visit_console(self, i: ConsoleLog):
        if i.value is None:
            self.errors.append(ExceptionPyType("ERROR EN CONSOLE LOG NO TIENE VALORES PARA IMPRIMIR.", i.line, i.column))
            return None

        content = ""
        for value in i.value:
            result = value.accept(self)
            if result is None:
                self.errors.append(ExceptionPyType("ERROR EN CONSOLE LOG NO SE PUDO IMPRIMIR EL VALOR.", i.line, i.column))
                continue

            content = content + " " + str(result.value)

        #print(content)
        self.console.append(content)

    def visit_continue(self, i: Continue):
        if self.symbol_table.parent is None:
            self.errors.append(ExceptionPyType("ERROR EN CONTINUE NO ESTA DENTRO DE UN CICLO.", i.line, i.column))
            return None
        else:
            return i

    def visit_declaration(self, i: Declaration):
        if i.type is None:
            self.errors.append(ExceptionPyType("ERROR EN DECLARACION DE VARIABLE NO TIENE TIPO DE VARIABLE.", i.line, i.column))
            return None
        for instruction in i.instructions:
            variable: Variable = instruction.accept(self)

            if variable is None:
                self.errors.append(ExceptionPyType("ERROR EN DECLARACION DE VARIABLE NO SE PUDO DECLARAR LA VARIABLE DEBIDO QUE ES NULA", i.line, i.column))
                return None

            if self.symbol_table.var_in_table(variable.id):
                self.errors.append(ExceptionPyType("VARIABLE YA EXISTE."+variable.id, i.line, i.column))
                return None

            self.symbol_table.add_variable(variable)
            #print("DECLARANDO VARIABLE: "+variable.id+ "valor "+variable.value.__str__())
            # print(variable.data_type)
            # print("DECLARACION DE VARIABLE EXITOSA.")
            # print(self.symbol_table.__str__())

    def visit_else(self, i: ElseState):
        if i.bloque is not None:
            tmp_if: SymbolTable = SymbolTable(self.symbol_table, ScopeType.ELSE_SCOPE)
            self.symbol_table = tmp_if
            for elemento in i.bloque:
                result = elemento.accept(self)
                if result is not None:
                    if result.__class__.__name__ == "Return":
                        return_element: Return = result
                        self.symbol_table = self.symbol_table.parent
                        return return_element
                    elif result.__class__.__name__ == "Continue":
                        continue_element: Continue = Continue(i.line, i.column)
                        self.symbol_table = self.symbol_table.parent
                        return continue_element
                    elif result.__class__.__name__ == "Break":
                        break_element: Break = Break(i.line, i.column)
                        self.symbol_table = self.symbol_table.parent
                        return break_element

            self.symbol_table = self.symbol_table.parent
            return None
        else:
            return None

    def visit_foreach(self, i: ForEachState):
        assignment: Variable = i.assignment.accept(self)

        if assignment is None:
            self.errors.append(ExceptionPyType("NO SE PUDO REALIZAR LA ASIGNACION EN FOR.", i.line, i.column))
            return None

        # TODO: FOR EACH PARA LAS VARIABLES
        if assignment.symbol_type == SymbolType().VARIABLE:
            var = Variable()
            var.id = i.id
            var.data_type = assignment.data_type
            var.isAny = assignment.isAny
            var.symbol_type = SymbolType().VARIABLE

            # TODO: FOR EACH PARA STRING
            if assignment.data_type == VariableType().buscar_type("STRING"):
                self.symbol_table = SymbolTable(self.symbol_table, ScopeType.LOOP_SCOPE)
                self.symbol_table.add_variable(var)
                for value in assignment.value:
                    var.value = value
                    for instruction in i.instructions:
                        instruction.accept(self)

                self.symbol_table = self.symbol_table.parent

            # TODO: FOR EACH PARA NUMBER
            elif assignment.data_type == VariableType().buscar_type("NUMBER"):
                self.symbol_table = SymbolTable(self.symbol_table, ScopeType.LOOP_SCOPE)
                self.symbol_table.add_variable(var)

                for value in range(assignment.value):
                    var.value = value
                    for instruction in i.instructions:
                        instruction.accept(self)

                self.symbol_table = self.symbol_table.parent
            else:
                self.errors.append(ExceptionPyType("SOLO PUEDE ITERAR VARIABLES TIPO STRING O NUMBER", i.line, i.column))
                return None

            return None

        # TODO: FOR EACH PARA LOS ARREGLOS
        elif assignment.symbol_type == SymbolType().ARRAY:
            arrayModel = assignment.value

            variable = Variable()
            variable.id = i.id

            self.symbol_table = SymbolTable(self.symbol_table, ScopeType.LOOP_SCOPE)
            self.symbol_table.add_variable(variable)

            while arrayModel is not None:
                current_var: Variable = arrayModel.var
                variable.data_type = current_var.data_type
                variable.symbol_type = current_var.symbol_type
                variable.isAny = current_var.isAny
                variable.value = current_var.value

                for instruction in i.instructions:
                    instruction.accept(self)

                arrayModel = arrayModel.next

            self.symbol_table = self.symbol_table.parent
            return None


    def visit_for(self, i: ForState):
        if i.declaration is None:
            self.errors.append(ExceptionPyType("EL FOR NO TIENE DECLARACION DE VARIABLE PARA ITERAR.", i.line, i.column))
            return None
        if i.condition is None:
            self.errors.append(ExceptionPyType("EL FOR NO TIENE CONDICION.", i.line, i.column))
            return None
        if i.increment is None:
            self.errors.append(ExceptionPyType("EL FOR NO TIENE INCREMENTO.", i.line, i.column))
            return None
        self.symbol_table = SymbolTable(self.symbol_table, ScopeType.LOOP_SCOPE)
        i.declaration.accept(self)
        result_comparacion: Variable = i.condition.accept(self)
        isBreak=False

        if result_comparacion is None:
            print("EL RESULTADO DE LA COMPARACIÓN ES NONE")
            return None

        while result_comparacion.value is True:
            # self.symbol_table = SymbolTable(self.symbol_table, ScopeType.LOOP_SCOPE)
            for instruction in i.instructions:
                result = instruction.accept(self)
                if result is not None:
                    if result.__class__.__name__ == "Return":
                        if self.symbol_table.is_in_loop_scope():
                            self.symbol_table = self.symbol_table.parent
                            return result
                        else:
                            self.errors.append(ExceptionPyType("ERROR EN RETURN NO ESTA DENTRO DE UN CICLO.", i.line, i.column))
                            self.symbol_table = self.symbol_table.parent
                            return None
                    elif result.__class__.__name__ == "Continue":
                        break
                    elif result.__class__.__name__ == "Break":
                        self.symbol_table = self.symbol_table.parent
                        # isBreak=True
                        return None
            # self.symbol_table = self.symbol_table.parent
            # if isBreak:
                # isBreak=False
                # break
            i.increment.accept(self)
            result_comparacion = i.condition.accept(self)
            if result_comparacion is False:
                self.symbol_table = self.symbol_table.parent
                return None
                # break

        self.symbol_table = self.symbol_table.parent
        return None

    def visit_function(self, i: FunctionState):
        # print("function debug")
        if i.isInTable is True:
            print("VISITOR FUNCTION")
            #tmp_table= SymbolTable(self.symbol_table, ScopeType.FUNCTION_SCOPE)
            #self.symbol_table = tmp_table
            if i.parameters is not None:
                for param in i.parameters:
                    param.accept(self)

            if i.instructions is not None:
                for instruction in i.instructions:
                    result = instruction.accept(self)
                    if result is not None:
                        if isinstance(result, Return):
                           if result is not None:
                               return_element: Variable = result.accept(self)
                               #self.symbol_table = self.symbol_table.parent
                               return return_element

                #self.symbol_table = self.symbol_table.parent
                return None
            else:
                #self.symbol_table = self.symbol_table.parent
                return None



    def visit_if(self, i: IfState):
        if i.condition is None:
            self.errors.append(ExceptionPyType("IF NO TIENE CONDICION.", i.line, i.column))
            return None
        comparacion: Variable = i.condition.accept(self)
        if comparacion is None:
            self.errors.append(ExceptionPyType(" IF NO SE PUDO REALIZAR LA COMPARACION.", i.line, i.column))
            return None
        if comparacion.data_type != VariableType.lista_variables["BOOLEAN"]:
            self.errors.append(ExceptionPyType("IF LA CONDICION DEBE SER BOOLEANA.", i.line, i.column))
            return None
        if comparacion.value is True:
            tmp_if: SymbolTable = SymbolTable(self.symbol_table, ScopeType.IF_SCOPE)
            self.symbol_table = tmp_if
            if i.bloque_verdadero is not None:
                for instruction in i.bloque_verdadero:
                    result = instruction.accept(self)
                    #print("RESULTSSSSSS")
                    #print(result)
                    if result is not None:
                        if result.__class__.__name__ == "Return":
                           if self.symbol_table.is_in_fun_scope():
                                 return_element: Return = result
                                 self.symbol_table = self.symbol_table.parent
                                 return return_element
                           else:
                                 self.errors.append(ExceptionPyType("ERROR EN RETURN NO ESTA DENTRO DE UNA FUNCION.", i.line, i.column))
                                 self.symbol_table = self.symbol_table.parent
                                 return None
                        elif result.__class__.__name__ == "Continue":
                            continue_element: Continue = Continue(i.line, i.column)
                            self.symbol_table = self.symbol_table.parent
                            return continue_element
                        elif result.__class__.__name__ == "Break":
                            break_element: Break = Break(i.line, i.column)
                            self.symbol_table = self.symbol_table.parent
                            return break_element

                self.symbol_table = self.symbol_table.parent
            else:
                self.symbol_table = self.symbol_table.parent
                return None
        elif comparacion.value is False:
            if i.bloque_falso is not None:
                result_else = i.bloque_falso.accept(self)
                if result_else is not None:
                    if result_else.__class__.__name__ == "Return":
                        return_element: Return = result_else
                        # self.symbol_table = self.symbol_table.parent
                        return return_element
                    elif result_else.__class__.__name__ == "Continue":
                        continue_element: Continue = Continue(i.line, i.column)
                        # self.symbol_table = self.symbol_table.parent
                        return continue_element
                    elif result_else.__class__.__name__ == "Break":
                        break_element: Break = Break(i.line, i.column)
                        # self.symbol_table = self.symbol_table.parent
                        return break_element
            else:
                #self.symbol_table = self.symbol_table.parent
                return None

    def visit_interface_assign(self, i: InterfaceAssign):
        attributes: [Variable] = []

        for attr in i.attributes:
            result: Variable = attr.accept(self)

            if result is None:
                self.errors.append(ExceptionPyType("NO SE PUDO REALIZAR LA OPERACIÓN /INTERFACE/", i.line, i.column))
            else:
                is_duplicate = False
                for a in attributes:
                    if a.id == result.id:
                        is_duplicate = True
                        break

                if is_duplicate:
                    self.errors.append(ExceptionPyType("ATRIBUTO YA DECLARADO", i.line, i.column))

                else:
                    attributes.append(result)

        model = InterfaceModel('', attributes)
        variable = Variable()
        variable.data_type = VariableType().buscar_type("DEFINIRLA")
        variable.value = model
        variable.symbol_type = SymbolType().VARIABLE
        variable.isAny = False

        return variable


    def visit_inter_attr_assign(self, i: InterAttributeAssign):
        attribute:Variable = i.interAttribute.accept(self)

        if attribute is None:
            self.errors.append(ExceptionPyType("NO SE ENCONTRÓ EL ATRIBUTO", i.line, i.column))
            return None

        value = i.value.accept(self)

        if value is None:
            self.errors.append(ExceptionPyType("NO SE PUDO REALIZAR LA OPERACIÓN", i.line, i.column))
            return None

        if attribute.data_type != value.data_type:
            self.errors.append(ExceptionPyType("LOS TIPOS NO COINCIDEN", i.line, i.column))
            return None

        attribute.value = value.value

        return attribute



    def visit_interface(self, i: InterfaceState):
        if VariableType().type_declared(i.id):
            self.errors.append(ExceptionPyType("YA SE HA DECLARADO LA INTERFAZ.", i.line, i.column))

        else:
            VariableType().add_type(i.id)

            attributes: [Variable] = []

            for attribute in i.attributes:

                attr: Variable = attribute.accept(self)

                if attr is None:
                    self.errors.append(ExceptionPyType("NO SE PUDO REALIZAR LA ASIGNACIÓN", i.line, i.column))

                else:
                    is_duplicate = False
                    for a in attributes:
                        if attr.id == a.id:
                            is_duplicate = True
                            break

                    if is_duplicate:
                        self.errors.append(ExceptionPyType("ATRIBUTO YA DECLARADO", i.line, i.column))
                        return None
                    else:
                        attributes.append(attr)
                        # print("AGREGANDO ATRIBUTO: " + attr.id)

            interfaceModel = InterfaceModel(i.id, attributes)

            result = Variable()
            result.id = i.id
            result.symbol_type = SymbolType().INTERFACE
            result.isAny = False
            result.data_type = i.id
            result.value = interfaceModel

            self.symbol_table.add_variable(result)
            # print("AGREGANDO VARIABLE: " + result.__str__())

            return result


    def visit_native(self, i: NativeFunction):
        if i.type == NativeFunType.TOFIXED:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append(ExceptionPyType("FUNCION NATIVA NO EXISTE LA VARIABLE.", i.line, i.column))
                return None
            if variable.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append(ExceptionPyType("FUNCION NATIVA LA VARIABLE NO ES DE TIPO NUMBER.", i.line, i.column))
                return None
            if i.parameter is None:
                self.errors.append(ExceptionPyType("FUNCION NATIVA NO TIENE PARAMETROS.", i.line, i.column))
                return None
            nume = i.parameter[0]
            var_n = copy.deepcopy(variable)
            var_n.value = self.toFixed(variable.value, nume.accept(self).value)
            return var_n
        elif i.type == NativeFunType.TOEXPONENTIAL:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append(ExceptionPyType("FUNCION NATIVA NO EXISTE LA VARIABLE.", i.line, i.column))
                return None
            if variable.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append(ExceptionPyType("FUNCION NATIVA LA VARIABLE NO ES DE TIPO NUMBER.", i.line, i.column))
                return None
            if i.parameter is None:
                self.errors.append(ExceptionPyType("FUNCION NATIVA NO TIENE PARAMETROS.", i.line, i.column))
                return None
            nume = i.parameter[0]
            var_n = copy.deepcopy(variable)
            var_n.value = self.toExponential(variable.value, nume.accept(self).value)
            return var_n
        elif i.type == NativeFunType.TOSTRING:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append(ExceptionPyType("FUNCION NATIVA NO EXISTE LA VARIABLE.", i.line, i.column))
                return None
            var_n = copy.deepcopy(variable)
            var_n.value = str(variable.value)
            var_n.data_type = VariableType.lista_variables["STRING"]
            return var_n
        elif i.type == NativeFunType.TOLOWERCASE:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append(ExceptionPyType("FUNCION NATIVA NO EXISTE LA VARIABLE.", i.line, i.column))
                return None
            if variable.data_type != VariableType.lista_variables["STRING"]:
                self.errors.append(ExceptionPyType("FUNCION NATIVA LA VARIABLE NO ES DE TIPO STRING.", i.line, i.column))
                return None
            var_n = copy.deepcopy(variable)
            var_n.value = variable.value.lower()
            return var_n
        elif i.type == NativeFunType.TOUPPERCASE:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append(ExceptionPyType("FUNCION NATIVA NO EXISTE LA VARIABLE.", i.line, i.column))
                return None
            if variable.data_type != VariableType.lista_variables["STRING"]:
                self.errors.append(ExceptionPyType("FUNCION NATIVA LA VARIABLE NO ES DE TIPO STRING.", i.line, i.column))
                return None
            var_n = copy.deepcopy(variable)
            var_n.value = variable.value.upper()
            return var_n
        elif i.type == NativeFunType.SPLIT:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append(ExceptionPyType("FUNCION NATIVA NO EXISTE LA VARIABLE.", i.line, i.column))
                return None
            if variable.data_type != VariableType.lista_variables["STRING"]:
                self.errors.append(ExceptionPyType("FUNCION NATIVA LA VARIABLE NO ES DE TIPO STRING.", i.line, i.column))
                return None
            if len(i.parameter) == 0:
                self.errors.append(ExceptionPyType("FUNCION NATIVA NO TIENE PARAMETROS.", i.line, i.column))
                return None
            parameter = i.parameter[0].accept(self)

            if parameter is None:
                self.errors.append(ExceptionPyType("NO SE PUDO REALIZAR LA OPERACION DE PARAMETROS.", i.line, i.column))
                return None

            if parameter.data_type != VariableType().buscar_type("STRING"):
                self.errors.append(ExceptionPyType("SE ESPERABA UN VALOR TIPO STRING", i.line, i.column))
                return None

            values = variable.value.split(parameter.value)

            first_node = None
            result = Variable()
            result.symbol_type = SymbolType().ARRAY
            result.isAny = False

            for value in values:
                newVar = Variable()
                newVar.data_type = VariableType().buscar_type("STRING")
                newVar.isAny = False
                newVar.symbol_type = SymbolType().VARIABLE
                newVar.value = str(value)

                current_node = ArrayModel(newVar)

                if first_node is None:
                    first_node = current_node
                else:
                    next_node: ArrayModel = first_node

                    while next_node.next is not None:
                        next_node = next_node.next

                    next_node.next = current_node
                    first_node.len = first_node.len + 1
                    # print("AGREGANDO OTRO NODO")

            result.value = first_node
            return result
        elif i.type == NativeFunType.CONCAT:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append(ExceptionPyType("FUNCION NATIVA NO EXISTE LA VARIABLE.", i.line, i.column))
                return None
            if i.parameter is None:
                self.errors.append(ExceptionPyType("FUNCION NATIVA NO TIENE PARAMETROS.", i.line, i.column))
                return None

            if variable.symbol_type == SymbolType().VARIABLE:
                if variable.data_type != VariableType().buscar_type("STRING"):
                    self.errors.append(ExceptionPyType("SE ESPERABA UN VALOR TIPO STRING", i.line, i.column))
                    return None

                nume = i.parameter[0]
                var_n = copy.deepcopy(variable)
                var_n.value = variable.value + nume.accept(self).value
                return var_n

            elif variable.symbol_type == SymbolType().ARRAY:
                arr = i.parameter[0]
                arr_result:Variable = arr.accept(self)

                if arr_result is None:
                    self.errors.append("NO SE PUDO EJECUTAR LA OPERACIÓN")
                    self.errors.append(ExceptionPyType("NO SE PUDO EJECUTAR LA OPERACION DEL ARRAY.", i.line, i.column))
                    return None

                if arr_result.symbol_type != SymbolType().ARRAY:
                    self.errors.append(ExceptionPyType("SE ESPERABA UN ARRAY", i.line, i.column))
                    return None

                arrayModel = variable.value
                newArrayModel = arr_result.value
                arrayModel.len = arrayModel.len + newArrayModel.len

                while arrayModel.next is not None:
                    arrayModel = arrayModel.next

                arrayModel.next = newArrayModel

                return variable
                # TODO: CONCATENAR ARRAYS
        elif i.type == NativeFunType.LENGTH:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append(ExceptionPyType("FUNCION NATIVA NO SE PUDO REALIZAR LA OPERACION", i.line, i.column))
                self.errors.append("ERROR EN FUNCIÓN NATIVA NO SE PUDO REALIZAR LA OPERACIÓN")
                return None

            if variable.symbol_type == SymbolType().VARIABLE:
                if variable.data_type != VariableType().buscar_type("STRING"):
                    self.errors.append(ExceptionPyType("SOLO PUEDE USAR LA FUNCION LENGTH EN VARIABLES TIPO STRING", i.line, i.column))
                    return None

                result = Variable()
                result.data_type = VariableType().buscar_type("NUMBER")
                result.symbol_type = SymbolType().VARIABLE
                result.isAny = False
                result.value = int(len(variable.value))
                return result

            elif variable.symbol_type == SymbolType().ARRAY:
                print("#### ENTRANDO A LENGTH ARRAY ####")
                #TODO: AGREGAR FUNCIONALIDAD PARA OBTENER EL  LEN DE UN ARRAY
                result = Variable()
                result.symbol_type = SymbolType().VARIABLE
                result.data_type = VariableType().buscar_type("NUMBER")
                arrayModel: ArrayModel = variable.value
                result.isAny = False
                result.value = arrayModel.len
                print(f'RETORNANDO {result.value} {result.symbol_type}')
                return result
        elif i.type == NativeFunType.PUSH:
            variable: Variable = i.variable.accept(self)

            if variable is None:
                self.errors.append(ExceptionPyType("FUNCION NATIVA NO SE PUDO REALIZAR LA OPERACION", i.line, i.column))
                return None

            if variable.symbol_type != SymbolType().ARRAY:
                self.errors.append(ExceptionPyType("SE ESPERABA UNA VARIABLE TIPO ARRAY", i.line, i.column))
                return None

            parameter: Variable = i.parameter[0].accept(self)

            if parameter is None:
                self.errors.append(ExceptionPyType("FUNCION NATIVA NO SE PUDO REALIZAR LA OPERACION", i.line, i.column))
                return None

            if parameter.symbol_type != SymbolType().VARIABLE:
                self.errors.append(ExceptionPyType("SE ESPERABA UNA VARIABLE PERO SE OBTUVO: "+ parameter.symbol_type, i.line, i.column))
                return None

            if variable.isAny:
                arrayModel = variable.value
                arrayModel.len = arrayModel.len+1

                while arrayModel.next is not None:
                    arrayModel = arrayModel.next

                newModel = ArrayModel(parameter)
                newModel.isAny = parameter.isAny
                arrayModel.next = newModel
                return variable

            if variable.data_type != parameter.data_type:
                self.errors.append(ExceptionPyType("INCOMPATIBILIDAD DE TIPOS", i.line, i.column))
                return None

            arrayModel = variable.value
            arrayModel.len = arrayModel.len+1

            while arrayModel.next is not None:
                arrayModel = arrayModel.next

            newModel = ArrayModel(parameter)
            newModel.isAny = parameter.isAny
            arrayModel.next = newModel
            return variable



    def visit_only_assign(self, i: OnlyAssignment):
        variable: Variable = self.symbol_table.find_var_by_id(i.id)
        if variable is None:
            self.errors.append(ExceptionPyType("ASIGNACION DE VARIABLE NO EXISTE LA VARIABLE.", i.line, i.column))
            return None
        tmp: Variable = i.value.accept(self)
        if tmp is None:
            self.errors.append(ExceptionPyType("ASIGNACION DE VARIABLE NO SE PUDO ASIGNAR VALOR.", i.line, i.column))
            return None
        if variable.data_type != tmp.data_type:
            if variable.isAny:
                variable.data_type = tmp.data_type
                variable.value = tmp.value
                return None
            else:
                self.errors.append(ExceptionPyType("ASIGNACION DE VARIABLE TIPOS DE DATOS DIFERENTES.", i.line, i.column))
                return None

        variable.value = tmp.value
        return None

    def visit_parameter(self, i: Parameter):
        vr:Variable= Variable()
        vr.id= i.id
        vr.data_type= i.data_type
        return vr

    def visit_return(self, i: Return):
        if self.symbol_table.parent is None:
            self.errors.append(ExceptionPyType("RETURN NO ESTA EN UNA FUNCION.", i.line, i.column))
            return None
        if i.expression is None:
            vr_rrr= Return(i.line, i.column, Value(i.line, i.column, 0,ValueType().ENTERO))
            return vr_rrr
        if i.expression is None:
            self.errors.append(ExceptionPyType("RETURN NO TIENE EXPRESION.", i.line, i.column))
            return None
        else:
            return i

    def visit_unary_op(self, i: UnaryOperation):
        right = i.right_operator.accept(self)
        if right is None:
            self.errors.append(ExceptionPyType("NO SE PUDO REALIZAR LA OPERACION UNARIA.", i.line, i.column))
            return None

        if right.symbol_type == SymbolType().ARRAY or right.symbol_type == SymbolType().INTERFACE:
            self.errors.append(ExceptionPyType("SOLO PUEDES REALIZAR OPERACIONES ENTRE VARIABLES", i.line, i.column))
            return None

        result = Variable()
        if i.operator == OperationType.NEGATIVE:
            if right.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (-) UNARIO ENTRE VARIABLE DE TIPO NUMBER.", i.line, i.column))
                return None

            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = -right.value
            result.symbol_type = SymbolType().VARIABLE
            result.isAny = False
            return result

        elif i.operator == OperationType.POSITIVE:
            if right.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) UNARIO ENTRE VARIABLE DE TIPO NUMBER.", i.line, i.column))
                return None

            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = right.value
            result.symbol_type = SymbolType().VARIABLE
            result.isAny = False
            return result

        elif i.operator == OperationType.NOT:
            if right.data_type != VariableType.lista_variables["BOOLEAN"]:
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (!) UNARIO ENTRE VARIABLE DE TIPO BOOLEAN.", i.line, i.column))
                return None

            result.data_type = VariableType().buscar_type("BOOLEAN")
            result.value = not right.value
            result.symbol_type = SymbolType().VARIABLE
            result.isAny = False
            return result

        elif i.operator == OperationType.INCREMENT:
            var = self.symbol_table.find_var_by_id(right.id)
            if right.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (++) UNARIO ENTRE VARIABLE DE TIPO NUMBER.", i.line, i.column))
                return None

            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = right.value + 1
            var.value = result.value
            return result

        elif i.operator == OperationType.DECREMENT:
            var = self.symbol_table.find_var_by_id(right.id)
            if right.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append(ExceptionPyType("SOLO PUEDE REALIZAR OPERACIONES TIPO (--) UNARIO ENTRE VARIABLE DE TIPO NUMBER.", i.line, i.column))
                return None

            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = right.value - 1
            var.value = result.value
            return result

    def visit_while(self, i: WhileState):
        if i.condition.accept is None:
            self.errors.append(ExceptionPyType("WHILE NO TIENE CONDICION.", i.line, i.column))
            return None
        result = i.condition.accept(self)
        if result is None:
            self.errors.append(ExceptionPyType("WHILE NO SE PUDO EVALUAR CONDICION.", i.line, i.column))
            return None
        isBreak = False
        while result.value:
            self.symbol_table = SymbolTable(self.symbol_table, ScopeType.LOOP_SCOPE)
            if i.instructions is not None:
                for instruccion in i.instructions:
                    result=instruccion.accept(self)
                    if result is not None:
                        if result.__class__.__name__ == "Return":
                            if self.symbol_table.is_in_loop_scope():
                                self.symbol_table = self.symbol_table.parent
                                return result
                            else:
                                self.errors.append(ExceptionPyType("RETURN NO ESTA EN UNA FUNCION.", i.line, i.column))
                                self.symbol_table = self.symbol_table.parent
                                return None
                        elif result.__class__.__name__ == "Break":
                            isBreak = True
                            break
                        elif result.__class__.__name__ == "Continue":
                            break
                self.symbol_table = self.symbol_table.parent
                if isBreak:
                    break

                result = i.condition.accept(self)
                if result is None:
                    self.errors.append(ExceptionPyType("WHILE NO SE PUDO EVALUAR CONDICION.", i.line, i.column))
                    return None
        return None

    def visit_value(self, i: Value):
        variable = Variable()
        if i.value_type == ValueType.CADENA:
            variable.data_type = VariableType().buscar_type("STRING")
            variable.symbol_type = SymbolType().VARIABLE
            variable.isAny = False
            variable.value = str(i.value)
            return variable
        elif i.value_type == ValueType.ENTERO:
            variable.data_type = VariableType().buscar_type("NUMBER")
            variable.symbol_type = SymbolType().VARIABLE
            variable.isAny = False

            variable.value = int(i.value)
            return variable
        elif i.value_type == ValueType.DECIMAL:
            variable.data_type = VariableType().buscar_type("NUMBER")
            variable.symbol_type = SymbolType().VARIABLE
            variable.isAny = False

            variable.value = float(i.value)
            return variable
        elif i.value_type == ValueType.BOOLEANO:
            variable.data_type = VariableType().buscar_type("BOOLEAN")
            variable.value = True if i.value == "true" else False
            variable.symbol_type = SymbolType().VARIABLE
            variable.isAny = False

            return variable
        elif i.value_type == ValueType.LITERAL:
            var_in_table = self.symbol_table.find_var_by_id(str(i.value))
            if var_in_table is None:
                self.errors.append(ExceptionPyType("NO SE ENCONTRÓ LA VARIABLE: " + i.value + " EN LA TABLA DE SIMBOLOS.", i.line, i.column))
                return None

            if var_in_table.symbol_type == SymbolType().ARRAY or not VariableType().is_primitive(var_in_table.data_type):
                return var_in_table

            # print("ENCONTRANDO VALOR PRIMITIVO, HACIENDO COPIA")
            result = copy.deepcopy(var_in_table)
            return result

    ######################################## METODOS NATIVOS ########################################
    def toFixed(self, num, decimales=0):
        formato = "{:." + str(decimales) + "f}"
        numero_redondeado = round(num, decimales)
        return formato.format(numero_redondeado)

    def toExponential(self,num, decimales=0):
        signo = '+' if num >= 0 else '-'  # Determinar el signo del número
        if signo == '-':
            formato = signo+"{:.{}e}".format(abs(num), decimales)  # Obtener la representación exponencial del valor absoluto del número
            return formato
        else:
            formato ="{:.{}e}".format(abs(num), decimales)  # Obtener la representación exponencial del valor absoluto del número
            return formato


    def assignDefaultValue(self, vr:VariableType):
        if vr == VariableType().buscar_type("NUMBER"):
            return 1
        elif vr == VariableType().buscar_type("STRING"):
            return "hola"
        elif vr == VariableType().buscar_type("BOOLEAN"):
            return True
        elif vr == VariableType().buscar_type("ARRAY"):
            return [1, 2, 3]
        elif vr == VariableType().buscar_type("NULL"):
            return None
        else:
            interface = self.symbol_table.find_interface_by_id(vr)

            interfaceModel: InterfaceModel = interface.value
            return copy.deepcopy(interfaceModel)

    ######################################## METODOS PARA SOBRECARGA DE FUNCIONES ########################################

    def is_duplicated_fun(self, id: str, parameters: [Variable]):
        functions:[Variable] = self.symbol_table.find_fun_by_id(id)

        if len(functions) == 0:
            return False

        for function in functions:

            functionModel: FunctionModel = function.value

            if len(functionModel.parameters) != len(parameters):
                continue

            same_params = True

            for i in range(len(functionModel.parameters)):
                if functionModel.parameters[i].data_type != parameters[i].data_type:
                    same_params = False
                    break

            if same_params:
                return True

        return False

    def get_fun(self, id: str, arguments: [Variable]):
        functions:[Variable] = self.symbol_table.find_fun_by_id(id)

        if len(functions) == 0:
            return None

        for function in functions:

            functionModel: FunctionModel = function.value

            if len(functionModel.parameters) != len(arguments):
                continue

            same_params = True

            for i in range(len(functionModel.parameters)):
                if functionModel.parameters[i].data_type != arguments[i].data_type and not functionModel.parameters[i].isAny:
                    same_params = False
                    break

            if same_params:
                return copy.deepcopy(functionModel)

        return None
