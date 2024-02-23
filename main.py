from typing import Union

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from truth_table import TruthTable, VariablesAreNotProvided
from pydantic import BaseModel
import uvicorn

description = """
API калькулятора таблицы истинности.
"""

app = FastAPI(
    title="BestCalculatorEver",
    description=description,
    version="1.0.1",
    contact={
        "name": "Khaiam Aliev",
        "email": "khaiam.aliev@mail.ru"
    }
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Table(BaseModel):
    truth_table: dict
    solution: list
    status_code: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"truth_table": {"B": [0, 0, 1, 1], "C": [0, 1, 0, 1], "1": [0, 0, 0, 1]}, "solution": ["B/\\C"],
                 "status_code": 200}
            ]
        }
    }


@app.post("/api/solve_instance", status_code=200)
async def solve_instance(instance: str) -> Union[Table, HTTPException]:
    """
    Это метод решает логические функции. Возращает таблицу истинности
    """
    truth_table = TruthTable()
    try:
        truth_table.set_start_columns(instance)
    except VariablesAreNotProvided as e:
        return HTTPException(status_code=400, detail=e.msg)
    try:
        truth_table.solve_instance(instance)
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
    return Table(truth_table=truth_table.get_dict(), solution=truth_table.get_solution(), status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
