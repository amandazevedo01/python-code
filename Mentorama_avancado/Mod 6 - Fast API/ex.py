from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}


class Resp(BaseModel):
    valor1: int
    valor2: int
    operacao: str


@app.post("/novarota")
async def novarota(resp:Resp):
    R = resp
    if R.operacao == 'soma':
        soma = R.valor1 + R.valor2
        return soma

    elif R.operacao == 'subtracao':
        sub = R.valor1 - R.valor2
        return sub
    elif R.operacao == 'multiplicacao':
        m = R.valor1 * R.valor2
        return m

    elif R.operacao == 'divisao':
        d = R.valor1 / R.valor2
        return d