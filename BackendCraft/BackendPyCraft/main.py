# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from fastapi.encoders import jsonable_encoder
from flask import Flask, render_template, request
from flask_cors import CORS
from src.models.Instruction import Instruction
from src.symbolTable.SymbolTable import SymbolTable
from src.visitor.Debugger import Debugger
from src.visitor.Runner import Runner
from src.models.VariableType import VariableType
from src.ObjectError.ModelResponse import ModelResponse
from src.visitor.CstDrawer import CstDrawer
from src.symbolTable.TableC3d import TableC3d
from src.symbolTable.SymC3d import SymC3d
from src.visitor.C3DGenerator import C3DGenerator
from src.ObjectError.ExceptionPyTypeEncoder import ExceptionPyTypeEncoder
from src.symbolModel.ArrayModelEncoder import ArrayModelEncoder
from src.models.VariableEncoder import VariableEncoder
import grammar
import json
import pickle
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
text: str

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET"])
def test_api():
    return {"Hello": "from test_api"}
@app.route('/analisis', methods=['POST'])
def get_text_compiler():
    data = request.get_json()
    text = data['text']
    return ParsearTextoApi(text)

@app.route('/c3d', methods=['POST'])
def get_text_c3d():
    data = request.get_json()
    text = data['text']
    return parserCod3d(text)

def ParsearTextoApi(texto):
    grammar.global_arr = []
    errors = grammar.global_arr
    instrucciones : Instruction = grammar.parse(texto)
#################  VISITOR DEBUG  #################
    table= SymbolTable()
    debbuger= Debugger(table,errors)


    if instrucciones is not None:
        for instruccion in instrucciones:
            instruccion.accept(debbuger)

    errorsR = errors
    tableR =  SymbolTable()
    console= []
    VariableType().clean_types()
    tableR.symbols = debbuger.symbol_table.getAllFunctions()
####################### CST #######################
    drawer = CstDrawer()
    content = "digraph {\n"
    if instrucciones is not None:
        for i in instrucciones:
            content = content + f'init -> {i.node_name()}\n'
            content = content + i.accept(drawer)
    content = content+"}\n"

    #print("#### CST ####")
    #print(content)
#################  VISITOR RUNNER  #################
    #print("#################  VISITOR RUNNER  #################")
    runner = Runner(tableR,errorsR,console)
    if instrucciones is not None:
        for instruccion in instrucciones:
            instruccion.accept(runner)
    #print("#############################TABLA DE SIMBOLOS")
    for i in runner.symbol_table.symbols:
        print(str(i))
    #print("#############################ERRORES")
    if len(runner.errors) > 0:
        for error in runner.errors:
            print(str(error))
    #print("#############################CONSOLE")
    for console in runner.console:
        print(str(console))
    objeto_return= ModelResponse(runner.symbol_table.symbols,runner.errors,runner.console, content)
    #print("#############################OBJETO RETURN")
    # print(objeto_return.__getstate__())
    array_errores=[]
    for i in runner.errors:
        array_errores.append(json.dumps(i, cls=ExceptionPyTypeEncoder))
        print(json.dumps(i, cls=ExceptionPyTypeEncoder))

    array_simbolos=[]
    print("####### tabla de simbolos #######")
    for i in runner.symbol_table.symbols:
        array_simbolos.append(json.dumps(i, cls=VariableEncoder))
        print(json.dumps(i, cls=VariableEncoder))
    #return (objeto_return.__getstate__())
    return {"table": array_simbolos, "errors": array_errores, "console": runner.console, "cst": content}
def parserCod3d(texto):
    ################# C3D #################
    instrucciones : Instruction = grammar.parse(texto)
    table= TableC3d()
    code_c3d= C3DGenerator(table)
    code_c3d.cleanAll()
    if instrucciones is not None:
        for instruccion in instrucciones:
            instruccion.accept(code_c3d)
    return {"c3d": code_c3d.get_code()}
    #print("#############################CODIGO C3D")
    #print(code_c3d.get_code())


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)