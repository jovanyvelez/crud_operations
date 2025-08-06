from fastapi import FastAPI

from bd import SessionDepends
from sqlalchemy import text


app = FastAPI()




























































@app.get("/consultar")
async def root(session: SessionDepends):
    datos = session.execute(text("SELECT * FROM heroes"))

    heroes  = []

    for hero in datos:
        heroes.append({
            "nombre": hero.name,
            "edad": hero.age
        })

    return {"message": heroes}
















































@app.get("/consultar/{heroe_id}")
async def consultar_heroe(heroe_id: int, session: SessionDepends):
    datos = session.execute(text("SELECT * FROM heroes WHERE id = :id"), {"id": heroe_id})
    hero = datos.first()
    
    if hero is None:
        return {"error": "Héroe no encontrado"}
    
    return {
        "message": {
            "id": hero.id,
            "nombre": hero.name,
            "edad": hero.age,
            "secreto": hero.secret_name
        }
    }

@app.post("/insertar")
async def insertar_heroe(nombre:str, edad:int, secreto:str, session: SessionDepends):
    print(f"nombre: {nombre}, edad: {edad}, secreto: {secreto}")
    nuevo_heroe = text("INSERT INTO heroes (name, age, secret_name) VALUES (:name, :age, :secret_name)")
    session.execute(nuevo_heroe, {"name": nombre, "age": edad, "secret_name": secreto})
    session.commit()
    return {"message": "Heroe insertado correctamente"}

@app.delete("/borrar/{heroe_id}")
async def borrar_heroe(heroe_id: int, session: SessionDepends):
    # Primero verificar si el héroe existe
    verificar = session.execute(text("SELECT id FROM heroes WHERE id = :id"), {"id": heroe_id})
    if verificar.first() is None:
        return {"error": "Héroe no encontrado"}
    
    # Borrar el héroe
    borrar_query = text("DELETE FROM heroes WHERE id = :id")
    session.execute(borrar_query, {"id": heroe_id})
    session.commit()
    return {"message": "Héroe borrado correctamente"}
























































































@app.put("/actualizar/{heroe_id}")
async def actualizar_heroe(session: SessionDepends, heroe_id: int, nombre: str | None = None, edad: int | None = None, secreto: str | None = None):
    # Verificar si el héroe existe
    verificar = session.execute(text("SELECT id FROM heroes WHERE id = :id"), {"id": heroe_id})
    if verificar.first() is None:
        return {"error": "Héroe no encontrado"}
    
    # Construir la consulta de actualización dinámicamente
    campos_actualizar = []
    parametros: dict[str, str | int] = {"id": heroe_id}
    
    if nombre is not None:
        campos_actualizar.append("name = :name")
        parametros["name"] = nombre
    
    if edad is not None:
        campos_actualizar.append("age = :age")
        parametros["age"] = edad
    
    if secreto is not None:
        campos_actualizar.append("secret_name = :secret_name")
        parametros["secret_name"] = secreto
    
    if not campos_actualizar:
        return {"error": "No se proporcionaron campos para actualizar"}
    
    # Ejecutar la actualización
    consulta_update = f"UPDATE heroes SET {', '.join(campos_actualizar)} WHERE id = :id"
    session.execute(text(consulta_update), parametros)
    session.commit()
    
    return {"message": "Héroe actualizado correctamente"}