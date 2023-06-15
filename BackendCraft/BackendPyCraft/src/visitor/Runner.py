
from .Visitor import Visitor
from ..models import Assignment, Parameter
from ..models import BinaryOperation
from ..models import Break
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
from ..symbolTable.ScopeType import ScopeType
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
        if self.symbol_table.parent is None:
            print("ERROR EN CONTINUE NO ESTA DENTRO DE UN CICLO.")
            return None
        else:
            return i

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
                    #print("DECLARACION DE VARIABLE EXITOSA.")
                    #print(self.symbol_table.__str__())
                else:
                    self.errors.append("ERROR EN DECLARACION DE VARIABLE NO SE PUDO ASIGNAR VALOR.")
                    print("ERROR EN DECLARACION DE VARIABLE NO SE PUDO ASIGNAR VALOR.")
                    return None

    def visit_else(self, i: ElseState):
        if i.bloque is not None:
            tmp_if: SymbolTable = SymbolTable(self.symbol_table, ScopeType.ELSE_SCOPE)
            self.symbol_table = tmp_if
            for elemento in i.bloque:
                result = elemento.accept(self)
                if result is not None:
                    if isinstance(result, Return):
                        return_element: Return = result
                        self.symbol_table = self.symbol_table.parent
                        return return_element
                    elif isinstance(result, Continue):
                        continue_element: Continue = Continue(i.line, i.column)
                        self.symbol_table = self.symbol_table.parent
                        return continue_element
                    elif isinstance(result, Break):
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
        pass

    def visit_if(self, i: IfState):
        if i.condition is None:
            self.errors.append("ERROR EN IF NO TIENE CONDICION.")
            print("ERROR EN IF NO TIENE CONDICION.")
            return None
        comparacion: Variable = i.condition.accept(self)
        if comparacion is None:
            self.errors.append(
                "ERROR EN IF NO SE PUDO REALIZAR LA COMPARACION. line: " + i.condition.line + " column: " + i.condition.column)
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
                        if isinstance(result, Return):
                            return_element: Return = result
                            self.symbol_table = self.symbol_table.parent
                            return return_element
                        elif isinstance(result, Continue):
                            continue_element: Continue = Continue(i.line, i.column)
                            self.symbol_table = self.symbol_table.parent
                            return continue_element
                        elif isinstance(result, Break):
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
                    if isinstance(result_else, Return):
                        return_element: Return = result_else
                        self.symbol_table = self.symbol_table.parent
                        return return_element
                    elif isinstance(result_else, Continue):
                        continue_element: Continue = Continue(i.line, i.column)
                        self.symbol_table = self.symbol_table.parent
                        return continue_element
                    elif isinstance(result_else, Break):
                        break_element: Break = Break(i.line, i.column)
                        self.symbol_table = self.symbol_table.parent
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
        elif i.type == NativeFunType.TYPE_OF:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                print("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                return None
            var_n = copy.deepcopy(variable)
            var_n.value = variable.data_type
            var_n.data_type = VariableType.lista_variables["STRING"]
            return var_n
        elif i.type == NativeFunType.STRING_CAST:
            variable: Variable = i.variable.accept(self)
            if variable is None:
                self.errors.append("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                print("ERROR EN FUNCION NATIVA NO EXISTE LA VARIABLE.")
                return None
            var_n = copy.deepcopy(variable)
            var_n.value = str(variable.value)
            var_n.data_type = VariableType.lista_variables["STRING"]
            return var_n


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
        pass

    def visit_return(self, i: Return):
        if self.symbol_table.parent is None:
            self.errors.append("ERROR EN RETURN NO ESTA EN UNA FUNCION.")
            print("ERROR EN RETURN NO ESTA EN UNA FUNCION.")
            return None
        if i.value is None:
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
