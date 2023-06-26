from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
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
import grammar
import json
import pickle
import sys

app = FastAPI()
origins = [
    "http://localhost:3000",
    "localhost:3000",
    #TODO: aqui van los dominios
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], #TODO: aqui van los metodos
    allow_headers=["*"], #TODO: aqui van los headers
)

class TextApi(BaseModel):

    print(sys.getrecursionlimit())
    sys.setrecursionlimit(2000)
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

    #print("#### CST ####")
    #print(content)
################# C3D #################
    table= TableC3d()
    code_c3d= C3DGenerator(table)
    code_c3d.cleanAll()
    if instrucciones is not None:
        for instruccion in instrucciones:
            instruccion.accept(code_c3d)
    #print("#############################CODIGO C3D")
    #print(code_c3d.get_code())

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
    objeto_return= ModelResponse(runner.symbol_table.symbols,runner.errors,runner.console, content, code_c3d.get_code())
    #print("#############################OBJETO RETURN")
    #print(objeto_return)
    return (objeto_return.__getstate__())
    #return {"result": "ok"}

if __name__ == "__main__":
    import uvicorn
    app.run(app,host = '0.0.0.0', port=8000)