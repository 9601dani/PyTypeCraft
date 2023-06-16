from .Visitor import Visitor
from ..models import Assignment, Parameter
from ..models import ArrayState
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

import copy
from decimal import Decimal


class Runner(Visitor):

    def __init__(self, symbol_table: SymbolTable, errors):
        super().__init__()
        self.symbol_table = symbol_table
        self.errors = errors

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
                self.errors.append("NO SE PUDO REALIZAR LA ASIGNACIÓN")
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
                    self.errors.append("NO SE PUEDE ASIGNAR UN ARREGLO ANY A UNA VARIABLE QUE NO LO ES")
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
                    self.errors.append("NO SE ENCONTRÓ EL TIPO")
                    return None

                interface = self.symbol_table.find_interface_by_id(i.type)

                if interface is None:
                    self.errors.append("NO SE ENCONTRÓ LA INTERFAZ")
                    return None

                model: InterfaceModel = interface.value
                valueModel: InterfaceModel = value.value

                if len(model.attributes) != len(valueModel.attributes):
                    self.errors.append("EL NÚMERO DE ATRIBUTOS NO COINCIDE")
                    return None

                for attr in model.attributes:
                    attrInValue = None
                    for valueAttr in valueModel.attributes:
                        if attr.id == valueAttr.id:
                            attrInValue = valueAttr
                            break

                    if attrInValue is None:
                        self.errors.append("NO SE ENCONTRÓ EL ATRIBUTO: " + attr.id)
                        return None

                    if attr.data_type != attrInValue.data_type:
                        self.errors.append("LOS TIPOS DE ATRIBUTOS NO COINCIDEN")
                        return None

                result.data_type = i.type
                result.symbol_type = SymbolType().VARIABLE
                result.value = valueModel
                result.isAny = False

                return result

            if i.type != value.data_type:
                # print(str(value.data_type))
                self.errors.append("LA VARIABLE NO ES DEL MISMO TIPO")
                # print("LA VARIABLE NO ES DEL MISMO TIPO")
                return None

            result.data_type = value.data_type
            result.symbol_type = SymbolType().VARIABLE
            result.isAny = False
            result.value = value.value
            return result

    def visit_array_state(self, i: ArrayState):
        first_node = None
        result = Variable()
        result.symbol_type = SymbolType.ARRAY
        result.isAny = False

        for value in i.values:
            var:Variable = value.accept(self)

            if var is None:
                self.errors.append("NO SE PUDO REALIZAR LA OPERACIÓN")
                return None

            current_node = ArrayModel(var)

            if first_node is None:
                first_node = current_node
                result.data_type = var.data_type
                print("AGREGANDO PRIMER NODO")
            else:
                next_node: ArrayModel = first_node

                while next_node.next is not None:
                    next_node = next_node.next

                next_node.next = current_node
                first_node.len = first_node.len + 1
                print("AGREGANDO OTRO NODO RUN")

                if result.data_type != var.data_type:
                    first_node.isAny = True

        result.value = first_node
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
                    print("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE VARIABLES DEL MISMO TIPO.")
                    self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (+) ENTRE VARIABLES DEL MISMO TIPO.")
                    return None

                result.symbol_type = SymbolType.VARIABLE
                result.data_type = VariableType().buscar_type("NUMBER")
                a=Decimal(left.value)
                b=Decimal(right.value)
                result.value = a + b
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
        if self.symbol_table.parent is None:
            print("ERROR EN BREAK NO ESTA DENTRO DE UN CICLO.")
            return None
        else:
            return i

    def visit_call_arr(self, i: CallArray):
        variable: Variable = self.symbol_table.find_var_by_id(i.id)

        if variable is None:
            self.errors.append("NO SE ENCONTRÓ EL ARRAY: "+i.id)
            return None

        if variable.symbol_type != SymbolType().ARRAY:
            self.errors.append("LA VARIABLE NO ES UN ARRAY")
            return None

        current_var = variable

        for dimension in i.dimensions:
            index: Variable = dimension.accept(self)

            if index is None:
                self.errors.append("NO SE PUDO REALIZAR LA OPERACIÓN")
                return None

            if index.data_type != VariableType().buscar_type("NUMBER"):
                self.errors.append("EL ÍNDICE DEBE SER TIPO NUMBER")
                return None

            if current_var.symbol_type != SymbolType().ARRAY:
                self.errors.append("DIMENSIÓN NO ENCONTRADA")
                return None

            current_model: ArrayModel = current_var.value

            if int(index.value) > current_model.len:
                self.errors.append("INDICE FUERA DE LOS LÍMITES SE ESPERABA:"+str(current_model.len)+" PERO SE OBTUVO:"+str(index.value))
                return None

            for i in range(int(index.value)):
                current_model = current_model.next

            current_var = current_model.var

        return current_var

    def visit_call_attr(self, i: CallAttribute):
        value: Variable = i.id.accept(self)

        if value is None:
            self.errors.append("NO SE ENCONTRÓ LA VARIABLE")
            return None

        if not isinstance(value.value, InterfaceModel):
            self.errors.append("LA VARIABLE NO ES DE TIPO INTERFACE")
            return None

        model: InterfaceModel = value.value

        for attribute in model.attributes:
            if attribute.id == i.attr:
                return attribute

        self.errors.append("NO SE ENCONTRÓ EL ATRIBUTO: " + i.attr)
        return None

    def visit_call_fun(self, i: CallFunction):
        # print("CALL FUN")
        print(i.assignments)
        # self.symbol_table = SymbolTable(self.symbol_table, ScopeType.FUNCTION_SCOPE)
        # vr: Variable = Variable()
        # variables_nuevas = []
        # if i.assignments is not None:
        #     if self.symbol_table.fun_in_table(i.name) is not None:
        #         for assignment in i.assignments:
        #             result = assignment.accept(self)
        #             if result.__class__.__name__ == "Variable":
        #                 vr = result
        #                 variables_nuevas.append(vr)
        #             else:
        #                 print("ERROR EN ASIGNACIÓN DE VALORES EN FUNCIÓN.")
        #                 self.symbol_table = self.symbol_table.parent
        #                 return None
        #
        #         fun_match: Variable = Variable()
        #         find_fun: [Variable] = self.symbol_table.find_fun_by_id(i.name)
        #         for parametro in find_fun:
        #             if len(parametro.value.parameters) == len(i.assignments):
        #                 fun_match = parametro
        #                 break
        #
        #         fun_ejecutar_value: FunctionModel = fun_match.value
        #         fun_ejecutar: FunctionState = fun_ejecutar_value
        #         if len(fun_ejecutar.parameters) != len(variables_nuevas):
        #             self.errors.append("LA CANTIDAD DE PARAMETROS NO COINCIDE CON LA FUNCIÓN.")
        #             print("LA CANTIDAD DE PARAMETROS NO COINCIDE CON LA FUNCIÓN.")
        #             self.symbol_table = self.symbol_table.parent
        #             return None
        #         for p in range(len(fun_ejecutar.parameters)):
        #             fun_ejecutar.parameters[p].value = variables_nuevas[p].value
        #             nv_parametro = Variable()
        #             nv_parametro.id = fun_ejecutar.parameters[p].id
        #             nv_parametro.data_type = fun_ejecutar.parameters[p].data_type
        #             nv_parametro.value = fun_ejecutar.parameters[p].value
        #             nv_parametro.symbol_type = SymbolType.VARIABLE
        #             self.symbol_table.add_variable(nv_parametro)
        #         for fs in fun_ejecutar.instructions:
        #             result_fs = fs.accept(self)
        #             if result_fs is not None:
        #                 if result_fs.__class__.__name__ == "Return":
        #                     vr_return = result_fs.expression.accept(self)
        #                     self.symbol_table = self.symbol_table.parent
        #                     return vr_return
        #                 elif result_fs.__class__.__name__ == "Variable":
        #                     self.symbol_table = self.symbol_table.parent
        #                     return result_fs
        #
        #     else:
        #                 self.errors.append("NO SE ENCONTRÓ LA FUNCIÓN: " + i.name)
        #                 self.symbol_table = self.symbol_table.parent
        #                 return None
        # else:
        #     #self.symbol_table= SymbolTable(self.symbol_table, ScopeType.FUNCTION_SCOPE)
        #     find_fun: [Variable] = self.symbol_table.find_fun_by_id(i.name)
        #     fun_match: Variable = Variable()
        #     if find_fun is None or len(find_fun) == 0:
        #         self.errors.append("NO SE ENCONTRÓ LA FUNCIÓN: " + i.name)
        #         print("NO SE ENCONTRÓ LA FUNCIÓN: " + i.name)
        #         self.symbol_table = self.symbol_table.parent
        #         return None
        #
        #     for parametro in find_fun:
        #         if len(parametro.value.parameters) == 0:
        #             fun_match = parametro
        #             break
        #     fun_ejecutar_value: FunctionModel = fun_match.value
        #     fun_ejecutar: FunctionState = fun_ejecutar_value
        #     for fs in fun_ejecutar.instructions:
        #         result_fs = fs.accept(self)
        #         if result_fs is not None:
        #             if result_fs.__class__.__name__ == "Return":
        #                 vr_return = result_fs.expression.accept(self)
        #                 self.symbol_table = self.symbol_table.parent
        #                 return vr_return
        #             elif result_fs.__class__.__name__ == "Variable":
        #                 self.symbol_table = self.symbol_table.parent
        #                 return result_fs

        #TODO: PRUEBA DE MODIFICACIÓN EN CALL_FUN

        arguments = []

        for argument in i.assignments:
            value = argument.accept(self)

            if value is None:
                print("NO SE PUDO REALIZAR LA OPERACIÓN")
                return None

            arguments.append(value)
            # print("AGREGANDO ARGUMENTO: "+value.__str__())

        if i.name == "typeof":
            if len(arguments) != 1:
                print("LA FUNCIÓN TYPEOF ESPERABA SOLO UN ARGUMENTO")
                return None

            result = Variable()
            result.symbol_type = SymbolType().VARIABLE
            result.value = arguments[0].data_type
            result.data_type = VariableType().buscar_type("STRING")
            result.isAny = False
            return result

        elif i.name == "toString":
            if len(arguments) != 1:
                print("LA FUNCIÓN STRING ESPERABA SOLO UN ARGUMENTO")
                return None

            result = Variable()
            result.symbol_type = SymbolType().VARIABLE
            result.value = str(arguments[0].value)
            result.data_type = VariableType().buscar_type("STRING")
            result.isAny = False
            return result

        match_fun:FunctionModel = self.get_fun(i.name, arguments)

        if match_fun is None:
            print("NO SE ENCONTRÓ LA FUNCIÓN")
            return None

        print("FUNCIÓN: "+match_fun.id)
        # CREANDO NUEVO SCOPE PARA LA FUNCIÓN
        temp_table = SymbolTable(self.symbol_table, ScopeType.FUNCTION_SCOPE)
        self.symbol_table = temp_table
        # AGREGANDO LOS ARGUMENTOS CON SUS PARÁMETROS A LA TABLA DE SIMBOLOS
        for i in range(len(match_fun.parameters)):
            match_fun.parameters[i].value = arguments[i].value
            self.symbol_table.add_variable(match_fun.parameters[i])

        for instruction in match_fun.instructions:
            print("EJECUTANDO INSTRUCCIONES EN CALLFUNCTION")
            result=instruction.accept(self)
            if result is not None:
                if result.__class__.__name__ == "Return":
                    vr_return = result.expression.accept(self)
                    self.symbol_table = self.symbol_table.parent
                    print("RETORNANDO VALOR: "+vr_return.__str__() )
                    return vr_return
                elif result.__class__.__name__ == "Variable":
                    self.symbol_table = self.symbol_table.parent
                    return result

        self.symbol_table = self.symbol_table.parent
        return None

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
        if self.symbol_table.parent is None:
            print("ERROR EN CONTINUE NO ESTA DENTRO DE UN CICLO.")
            return None
        else:
            return i

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
        pass

    def visit_for(self, i: ForState):
        pass

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
            self.errors.append("ERROR EN IF NO TIENE CONDICION.")
            print("ERROR EN IF NO TIENE CONDICION.")
            return None
        comparacion: Variable = i.condition.accept(self)
        if comparacion is None:
            self.errors.append(
                "ERROR EN IF NO SE PUDO REALIZAR LA COMPARACION. line: " + str(i.condition.line) + " column: " + str(i.condition.column))
            print("ERROR EN IF NO SE PUDO REALIZAR LA COMPARACION.")
            return None
        if comparacion.data_type != VariableType.lista_variables["BOOLEAN"]:
            self.errors.append("ERROR EN IF LA CONDICION DEBE SER BOOLEANA.")
            print("ERROR EN IF LA CONDICION DEBE SER BOOLEANA.")
            return None
        if comparacion.value is True:
            tmp_if: SymbolTable = SymbolTable(self.symbol_table, ScopeType.IF_SCOPE)
            self.symbol_table = tmp_if
            if i.bloque_verdadero is not None:
                for instruction in i.bloque_verdadero:
                    result = instruction.accept(self)
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
                self.errors.append("NO SE PUDO REALIZAR LA OPERACIÓN")
            else:
                is_duplicate = False
                for a in attributes:
                    if a.id == result.id:
                        is_duplicate = True
                        break

                if is_duplicate:
                    self.errors.append("ATRIBUTO YA DECLARADO")

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
            self.errors.append("NO SE ENCONTRÓ EL ATRIBUTO")
            return None

        value = i.value.accept(self)

        if value is None:
            self.errors.append("NO SE PUDO REALIZAR LA OPERACIÓN")
            return None

        if attribute.data_type != value.data_type:
            self.errors.append("LOS TIPOS NO COINCIDEN")
            return None

        attribute.value = value.value

        return attribute



    def visit_interface(self, i: InterfaceState):
        if VariableType().type_declared(i.id):
            self.errors.append("YA SE HA DECLARADO LA INTERFAZ.")

        else:
            VariableType().add_type(i.id)

            attributes: [Variable] = []

            for attribute in i.attributes:

                attr: Variable = attribute.accept(self)

                if attr is None:
                    self.errors.append("NO  SE PUDO REALIZAR LA ASIGNACIÓN")

                else:
                    is_duplicate = False
                    for a in attributes:
                        if attr.id == a.id:
                            is_duplicate = True
                            break

                    if is_duplicate:
                        self.errors.append("ATRIBUTO YA DECLARADO")
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
                self.errors.append("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                print("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                return None
            if variable.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append("ERROR EN FUNCION NATIVA LA VARIABLE NO ES DE TIPO NUMBER.")
                print("ERROR EN FUNCION NATIVA LA VARIABLE NO ES DE TIPO NUMBER.")
                return None
            if i.parameter is None:
                self.errors.append("ERROR EN FUNCION NATIVA NO TIENE PARAMETROS.")
                print("ERROR EN FUNCION NATIVA NO TIENE PARAMETROS.")
                return None
            nume = i.parameter[0]
            var_n = copy.deepcopy(variable)
            var_n.value = self.toFixed(variable.value, nume.accept(self).value)
            return var_n
        elif i.type == NativeFunType.TOEXPONENTIAL:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                print("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                return None
            if variable.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append("ERROR EN FUNCION NATIVA LA VARIABLE NO ES DE TIPO NUMBER.")
                print("ERROR EN FUNCION NATIVA LA VARIABLE NO ES DE TIPO NUMBER.")
                return None
            if i.parameter is None:
                self.errors.append("ERROR EN FUNCION NATIVA NO TIENE PARAMETROS.")
                print("ERROR EN FUNCION NATIVA NO TIENE PARAMETROS.")
                return None
            nume = i.parameter[0]
            var_n = copy.deepcopy(variable)
            var_n.value = self.toExponential(variable.value, nume.accept(self).value)
            return var_n
        elif i.type == NativeFunType.TOSTRING:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                print("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                return None
            var_n = copy.deepcopy(variable)
            var_n.value = str(variable.value)
            var_n.data_type = VariableType.lista_variables["STRING"]
            return var_n
        elif i.type == NativeFunType.TOLOWERCASE:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                print("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                return None
            if variable.data_type != VariableType.lista_variables["STRING"]:
                self.errors.append("ERROR EN FUNCION NATIVA LA VARIABLE NO ES DE TIPO STRING.")
                print("ERROR EN FUNCION NATIVA LA VARIABLE NO ES DE TIPO STRING.")
                return None
            var_n = copy.deepcopy(variable)
            var_n.value = variable.value.lower()
            return var_n
        elif i.type == NativeFunType.TOUPPERCASE:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                print("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                return None
            if variable.data_type != VariableType.lista_variables["STRING"]:
                self.errors.append("ERROR EN FUNCION NATIVA LA VARIABLE NO ES DE TIPO STRING.")
                print("ERROR EN FUNCION NATIVA LA VARIABLE NO ES DE TIPO STRING.")
                return None
            var_n = copy.deepcopy(variable)
            var_n.value = variable.value.upper()
            return var_n
        elif i.type == NativeFunType.SPLIT:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                print("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                return None
            if variable.data_type != VariableType.lista_variables["STRING"]:
                self.errors.append("ERROR EN FUNCION NATIVA LA VARIABLE NO ES DE TIPO STRING.")
                print("ERROR EN FUNCION NATIVA LA VARIABLE NO ES DE TIPO STRING.")
                return None
            if i.parameter is None:
                self.errors.append("ERROR EN FUNCION NATIVA NO TIENE PARAMETROS.")
                print("ERROR EN FUNCION NATIVA NO TIENE PARAMETROS.")
                return None
            nume = i.parameter[0]
            var_n = copy.deepcopy(variable)
            var_n.value = variable.value.split(nume.accept(self).value)
            #var_n.data_type = VariableType.lista_variables["ARRAY"]
            return var_n
        elif i.type == NativeFunType.CONCAT:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                print("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                return None
            if variable.data_type != VariableType.lista_variables["STRING"] and variable.data_type != VariableType.lista_variables["ARRAY"]:
                self.errors.append("ERROR EN FUNCION NATIVA LA VARIABLE NO ES DE TIPO STRING.")
                print("ERROR EN FUNCION NATIVA LA VARIABLE NO ES DE TIPO STRING.")
                return None
            if i.parameter is None:
                self.errors.append("ERROR EN FUNCION NATIVA NO TIENE PARAMETROS.")
                print("ERROR EN FUNCION NATIVA NO TIENE PARAMETROS.")
                return None
            if variable.data_type == VariableType.lista_variables["STRING"]:
                nume = i.parameter[0]
                var_n = copy.deepcopy(variable)
                var_n.value = variable.value + nume.accept(self).value
                return var_n
            elif variable.data_type == VariableType.lista_variables["ARRAY"]:
                pass
                #TODO: CONCATENAR ARRAYS
        elif i.type == NativeFunType.LENGTH:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append("ERROR EN FUNCIÓN NATIVA NO SE PUDO REALIZAR LA OPERACIÓN")
                return None

            if variable.symbol_type == SymbolType().VARIABLE:
                if variable.data_type != VariableType().buscar_type("STRING"):
                    self.errors.append("SOLO PUEDE USAR LA FUNCIÓN LENGTH EN VARIABLES TIPO STRING")
                    return None

                result = Variable()
                result.data_type = VariableType().buscar_type("NUMBER")
                result.symbol_type = SymbolType().VARIABLE
                result.isAny = False
                result.value = int(len(variable.value))
                return result

            elif variable.symbol_type == SymbolType().ARRAY:
                #TODO: AGREGAR FUNCIONALIDAD PARA OBTENER EL  LEN DE UN ARRAY
                print("PRINT PARA QUE NO DE ERROR")


    def visit_only_assign(self, i: OnlyAssignment):
        variable: Variable = self.symbol_table.find_var_by_id(i.id)
        if variable is None:
            self.errors.append("ERROR EN ASIGNACION DE VARIABLE NO EXISTE LA VARIABLE.")
            print("ERROR EN ASIGNACION DE VARIABLE NO EXISTE LA VARIABLE.")
            return None
        tmp: Variable = i.value.accept(self)
        if tmp is None:
            self.errors.append("ERROR EN ASIGNACION DE VARIABLE NO SE PUDO ASIGNAR VALOR.")
            print("ERROR EN ASIGNACION DE VARIABLE NO SE PUDO ASIGNAR VALOR.")
            return None
        if variable.data_type != tmp.data_type:
            if variable.isAny:
                variable.data_type = tmp.data_type
                variable.value = tmp.value
                return None
            else:
                self.errors.append("ERROR EN ASIGNACION DE VARIABLE TIPOS DE DATOS DIFERENTES.")
                print("ERROR EN ASIGNACION DE VARIABLE TIPOS DE DATOS DIFERENTES.")
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
            self.errors.append("ERROR EN RETURN NO ESTA EN UNA FUNCION.")
            print("ERROR EN RETURN NO ESTA EN UNA FUNCION.")
            return None
        if i.expression is None:
            self.errors.append("ERROR EN RETURN NO TIENE VALOR.")
            print("ERROR EN RETURN NO TIENE VALOR.")
            return None
        if i.expression is None:
            self.errors.append("ERROR EN RETURN NO TIENE EXPRESION.")
            print("ERROR EN RETURN NO TIENE EXPRESION.")
            return None
        else:
            return i

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

        elif i.operator == OperationType.INCREMENT:
            var = self.symbol_table.find_var_by_id(right.id)
            if right.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (++) UNARIO ENTRE VARIABLE DE TIPO NUMBER.")
                return None

            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = right.value + 1
            var.value = result.value
            return result

        elif i.operator == OperationType.DECREMENT:
            var = self.symbol_table.find_var_by_id(right.id)
            if right.data_type != VariableType.lista_variables["NUMBER"]:
                self.errors.append("SOLO PUEDE REALIZAR OPERACIONES TIPO (--) UNARIO ENTRE VARIABLE DE TIPO NUMBER.")
                return None

            result.data_type = VariableType().buscar_type("NUMBER")
            result.value = right.value - 1
            var.value = result.value
            return result

    def visit_while(self, i: WhileState):
        pass

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
            var_in_table: Variable = self.symbol_table.find_var_by_id(str(i.value))
            if var_in_table is None:
                print("NO SE ENCONTRÓ LA VARIABLE: " + i.value + " EN LA TABLA DE SIMBOLOS")
                return None

            variable = copy.deepcopy(var_in_table)
            return variable

    ######################################## METODOS NATIVOS ########################################
    def toFixed(self, num, decimales=0):
        formato = "{:." + str(decimales) + "f}"
        numero_redondeado = round(num, decimales)
        return formato.format(numero_redondeado)

    def toExponential(self,num, decimales=0):
        signo = '+' if num >= 0 else '-'  # Determinar el signo del número
        formato = "{:.{}e}".format(abs(num), decimales)  # Obtener la representación exponencial del valor absoluto del número
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
                if functionModel.parameters[i].data_type != arguments[i].data_type:
                    same_params = False
                    break

            if same_params:
                return copy.deepcopy(functionModel)

        return None