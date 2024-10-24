from fastapi import FastAPI, Response
import uvicorn
import os
from pydantic import BaseModel
from libs.calculus import add

app = FastAPI()

class ab_entry(BaseModel):
    a: float
    b: float

@app.get('/')
def root():
    return Response("<h1> Test fastapi app </h1>")

@app.post('/summation', response_model=ab_entry)
async def summation(ab:ab_entry):

    s = add(ab.a, ab.b)

    res = str(s)

    return Response(res)

if __name__ == "__main__":
    host = "0.0.0.0"
    dev_host = "127.0.0.1"
    uvicorn.run(app, host=host, port=int(os.environ.get("PORT", 8080)))