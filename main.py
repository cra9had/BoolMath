from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from truth_table import TruthTable, VariablesAreNotProvided
from fastapi.responses import JSONResponse

import uvicorn


app = FastAPI()


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/solve_instance", status_code=200)
async def solve_instance(instance: str):
    """
    Это метод решает логические функции. Возращает таблицу истинности
    """
    truth_table = TruthTable()
    try:
        truth_table.set_start_columns(instance)
    except VariablesAreNotProvided as e:
        return HTTPException(status_code=400, detail=e.msg)
    truth_table.solve_instance(instance)
    return JSONResponse({
        "truth_table": truth_table.get_dict(),
        "status_code": 200
    })


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
