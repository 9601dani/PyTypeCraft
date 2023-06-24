from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from src.models.Instruction import Instruction
from src.symbolTable.SymbolTable import SymbolTable
from src.visitor.Debugger import Debugger
from src.visitor.Runner import Runner
from src.models.VariableType import VariableType
from src.ObjectError.ModelResponse import ModelResponse
from src.visitor.CstDrawer import CstDrawer
import grammar
import json
import pickle
import sys

app = FastAPI()

class TextApi(BaseModel):

    print(sys.getrecursionlimit())
    sys.setrecursionlimit(1500)
    print(sys.getrecursionlimit())
    text: str
@app.get("/")
def test_api():
    return {"Hello": "from test_api"}
@app.post("/analisis")
async def get_text_compiler(content : TextApi):
    print(content.text)
    text = content.text
    return ParsearTextoApi(text)

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

    print("#### CST ####")
    print(content)
#################  VISITOR RUNNER  #################
    print("#################  VISITOR RUNNER  #################")
    runner = Runner(tableR,errorsR,console)
    if instrucciones is not None:
        for instruccion in instrucciones:
            instruccion.accept(runner)
    print("#############################TABLA DE SIMBOLOS")
    for i in runner.symbol_table.symbols:
        print(str(i))
    print("#############################ERRORES")
    if len(runner.errors) > 0:
        for error in runner.errors:
            print(str(error))
    print("#############################CONSOLE")
    for console in runner.console:
        print(str(console))
    objeto_return= ModelResponse(runner.symbol_table.symbols,runner.errors,runner.console, content)
    print("#############################OBJETO RETURN")
    print(objeto_return)
    return (objeto_return.__getstate__())
    #return {"result": "ok"}