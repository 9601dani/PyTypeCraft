from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import grammar

app = FastAPI()

class TextApi(BaseModel):
    text: str
@app.get("/")
def test_api():
    return {"Hello": "from test_api"}
@app.post("/analisis")
async def get_text_compiler(content : TextApi):
    print(content.text)
    text = content.text
    grammar.parse(text)
    return {"result": "ok"}