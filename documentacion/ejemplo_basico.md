# Ejemplo Básico CRUD - Sistema de Estudiantes
## Proyecto de referencia sin manejo de errores

### Estructura de la tabla
```sql
CREATE TABLE estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    email TEXT NOT NULL,
    carrera TEXT NOT NULL,
    semestre INTEGER NOT NULL,
    activo BOOLEAN DEFAULT TRUE
);
```

### Código main.py - Versión Básica

```python
from fastapi import FastAPI
from bd import SessionDepends
from sqlalchemy import text

app = FastAPI()

@app.get("/estudiantes")
async def obtener_estudiantes(session: SessionDepends):
    datos = session.execute(text("SELECT * FROM estudiantes"))
    
    estudiantes = []
    
    for estudiante in datos:
        estudiantes.append({
            "id": estudiante.id,
            "nombre": estudiante.nombre,
            "apellido": estudiante.apellido,
            "email": estudiante.email,
            "carrera": estudiante.carrera,
            "semestre": estudiante.semestre,
            "activo": estudiante.activo
        })
    
    return {"estudiantes": estudiantes}

@app.get("/estudiantes/{estudiante_id}")
async def obtener_estudiante(estudiante_id: int, session: SessionDepends):
    datos = session.execute(text("SELECT * FROM estudiantes WHERE id = :id"), {"id": estudiante_id})
    estudiante = datos.first()
    
    if estudiante is None:
        return {"error": "Estudiante no encontrado"}
    
    return {
        "estudiante": {
            "id": estudiante.id,
            "nombre": estudiante.nombre,
            "apellido": estudiante.apellido,
            "email": estudiante.email,
            "carrera": estudiante.carrera,
            "semestre": estudiante.semestre,
            "activo": estudiante.activo
        }
    }

@app.post("/estudiantes")
async def crear_estudiante(nombre: str, apellido: str, email: str, carrera: str, semestre: int, session: SessionDepends):
    nuevo_estudiante = text("""
        INSERT INTO estudiantes (nombre, apellido, email, carrera, semestre, activo) 
        VALUES (:nombre, :apellido, :email, :carrera, :semestre, :activo)
    """)
    
    session.execute(nuevo_estudiante, {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "carrera": carrera,
        "semestre": semestre,
        "activo": True
    })
    session.commit()
    
    return {"message": "Estudiante creado correctamente"}

@app.put("/estudiantes/{estudiante_id}")
async def actualizar_estudiante(
    estudiante_id: int, 
    session: SessionDepends,
    nombre: str = None, 
    apellido: str = None, 
    email: str = None, 
    carrera: str = None, 
    semestre: int = None,
    activo: bool = None
):
    # Verificar si existe
    verificar = session.execute(text("SELECT id FROM estudiantes WHERE id = :id"), {"id": estudiante_id})
    if verificar.first() is None:
        return {"error": "Estudiante no encontrado"}
    
    # Construir actualización dinámica
    campos_actualizar = []
    parametros = {"id": estudiante_id}
    
    if nombre is not None:
        campos_actualizar.append("nombre = :nombre")
        parametros["nombre"] = nombre
    
    if apellido is not None:
        campos_actualizar.append("apellido = :apellido")
        parametros["apellido"] = apellido
    
    if email is not None:
        campos_actualizar.append("email = :email")
        parametros["email"] = email
    
    if carrera is not None:
        campos_actualizar.append("carrera = :carrera")
        parametros["carrera"] = carrera
    
    if semestre is not None:
        campos_actualizar.append("semestre = :semestre")
        parametros["semestre"] = semestre
    
    if activo is not None:
        campos_actualizar.append("activo = :activo")
        parametros["activo"] = activo
    
    if not campos_actualizar:
        return {"error": "No se proporcionaron campos para actualizar"}
    
    # Ejecutar actualización
    consulta_update = f"UPDATE estudiantes SET {', '.join(campos_actualizar)} WHERE id = :id"
    session.execute(text(consulta_update), parametros)
    session.commit()
    
    return {"message": "Estudiante actualizado correctamente"}

@app.delete("/estudiantes/{estudiante_id}")
async def eliminar_estudiante(estudiante_id: int, session: SessionDepends):
    # Verificar si existe
    verificar = session.execute(text("SELECT id FROM estudiantes WHERE id = :id"), {"id": estudiante_id})
    if verificar.first() is None:
        return {"error": "Estudiante no encontrado"}
    
    # Eliminar estudiante
    eliminar_query = text("DELETE FROM estudiantes WHERE id = :id")
    session.execute(eliminar_query, {"id": estudiante_id})
    session.commit()
    
    return {"message": "Estudiante eliminado correctamente"}

# Para ejecutar directamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
```

### Datos de ejemplo para insertar

```sql
INSERT INTO estudiantes (nombre, apellido, email, carrera, semestre, activo) VALUES
('Juan', 'Pérez', 'juan.perez@email.com', 'Ingeniería en Sistemas', 3, TRUE),
('María', 'González', 'maria.gonzalez@email.com', 'Administración', 5, TRUE),
('Carlos', 'López', 'carlos.lopez@email.com', 'Ingeniería en Sistemas', 2, TRUE),
('Ana', 'Martínez', 'ana.martinez@email.com', 'Psicología', 4, TRUE),
('Luis', 'Rodríguez', 'luis.rodriguez@email.com', 'Contaduría', 1, TRUE);
```

### Endpoints disponibles:
- **GET** `/estudiantes` - Lista todos los estudiantes
- **GET** `/estudiantes/{id}` - Obtiene un estudiante por ID
- **POST** `/estudiantes` - Crea un nuevo estudiante
- **PUT** `/estudiantes/{id}` - Actualiza un estudiante
- **DELETE** `/estudiantes/{id}` - Elimina un estudiante

### Observaciones importantes:
1. **Sin validaciones avanzadas** - Solo verificamos existencia básica
2. **Sin manejo de excepciones** - Las operaciones pueden fallar sin control
3. **Estructura simple** - Fácil de entender y replicar
4. **Imports mínimos** - Solo lo necesario como en el ejemplo de héroes
