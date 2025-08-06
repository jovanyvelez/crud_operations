from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_item(nombre: str | None = "Desconocido"):
    return {"nombre": nombre}