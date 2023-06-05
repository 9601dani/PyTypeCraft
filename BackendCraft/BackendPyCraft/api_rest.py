from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test_api():
    return {"Hello": "from test_api"}
@app.get("/compiler/{text}")
async def get_text_compiler():
    return {"text from compiler/texto"}