# Ejemplo CRUD con Manejo de Errores - Sistema de Estudiantes
## Proyecto de referencia CON manejo de errores básico

### Estructura de la tabla (igual que el ejemplo básico)
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

### Código main.py - Versión con Manejo de Errores

```python
from fastapi import FastAPI
from bd import SessionDepends
from sqlalchemy import text

app = FastAPI()

@app.get("/estudiantes")
async def obtener_estudiantes(session: SessionDepends):
    try:
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
    
    except Exception as e:
        return {"error": f"Error al obtener estudiantes: {str(e)}"}

@app.get("/estudiantes/{estudiante_id}")
async def obtener_estudiante(estudiante_id: int, session: SessionDepends):
    try:
        # Validar que el ID sea positivo
        if estudiante_id <= 0:
            return {"error": "El ID debe ser un número positivo"}
        
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
    
    except Exception as e:
        return {"error": f"Error al obtener estudiante: {str(e)}"}

@app.post("/estudiantes")
async def crear_estudiante(nombre: str, apellido: str, email: str, carrera: str, semestre: int, session: SessionDepends):
    try:
        # Validaciones básicas
        if not nombre or not apellido:
            return {"error": "Nombre y apellido son obligatorios"}
        
        if not email or "@" not in email:
            return {"error": "Email debe ser válido"}
        
        if semestre < 1 or semestre > 10:
            return {"error": "Semestre debe estar entre 1 y 10"}
        
        if not carrera:
            return {"error": "Carrera es obligatoria"}
        
        # Verificar si el email ya existe
        email_existente = session.execute(
            text("SELECT id FROM estudiantes WHERE email = :email"), 
            {"email": email}
        ).first()
        
        if email_existente:
            return {"error": "El email ya está registrado"}
        
        # Crear estudiante
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
    
    except Exception as e:
        session.rollback()
        return {"error": f"Error al crear estudiante: {str(e)}"}

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
    try:
        # Validar ID
        if estudiante_id <= 0:
            return {"error": "El ID debe ser un número positivo"}
        
        # Verificar si existe
        verificar = session.execute(text("SELECT id FROM estudiantes WHERE id = :id"), {"id": estudiante_id})
        if verificar.first() is None:
            return {"error": "Estudiante no encontrado"}
        
        # Validaciones de campos si se proporcionan
        if email is not None and ("@" not in email or not email):
            return {"error": "Email debe ser válido"}
        
        if semestre is not None and (semestre < 1 or semestre > 10):
            return {"error": "Semestre debe estar entre 1 y 10"}
        
        if nombre is not None and not nombre.strip():
            return {"error": "Nombre no puede estar vacío"}
        
        if apellido is not None and not apellido.strip():
            return {"error": "Apellido no puede estar vacío"}
        
        # Verificar email duplicado si se está actualizando
        if email is not None:
            email_duplicado = session.execute(
                text("SELECT id FROM estudiantes WHERE email = :email AND id != :id"), 
                {"email": email, "id": estudiante_id}
            ).first()
            
            if email_duplicado:
                return {"error": "El email ya está en uso por otro estudiante"}
        
        # Construir actualización dinámica
        campos_actualizar = []
        parametros = {"id": estudiante_id}
        
        if nombre is not None:
            campos_actualizar.append("nombre = :nombre")
            parametros["nombre"] = nombre.strip()
        
        if apellido is not None:
            campos_actualizar.append("apellido = :apellido")
            parametros["apellido"] = apellido.strip()
        
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
    
    except Exception as e:
        session.rollback()
        return {"error": f"Error al actualizar estudiante: {str(e)}"}

@app.delete("/estudiantes/{estudiante_id}")
async def eliminar_estudiante(estudiante_id: int, session: SessionDepends):
    try:
        # Validar ID
        if estudiante_id <= 0:
            return {"error": "El ID debe ser un número positivo"}
        
        # Verificar si existe
        verificar = session.execute(text("SELECT id FROM estudiantes WHERE id = :id"), {"id": estudiante_id})
        if verificar.first() is None:
            return {"error": "Estudiante no encontrado"}
        
        # Eliminar estudiante
        eliminar_query = text("DELETE FROM estudiantes WHERE id = :id")
        session.execute(eliminar_query, {"id": estudiante_id})
        session.commit()
        
        return {"message": "Estudiante eliminado correctamente"}
    
    except Exception as e:
        session.rollback()
        return {"error": f"Error al eliminar estudiante: {str(e)}"}

# Para ejecutar directamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
```

### Mejoras implementadas en el manejo de errores:

#### 1. **Try-Catch en todos los endpoints**
```python
try:
    # Operaciones de base de datos
    return {"message": "Éxito"}
except Exception as e:
    session.rollback()  # Solo en operaciones de escritura
    return {"error": f"Error: {str(e)}"}
```

#### 2. **Validaciones de entrada**
- IDs positivos
- Emails válidos (contienen "@")
- Campos obligatorios no vacíos
- Rangos válidos (semestre 1-10)

#### 3. **Verificaciones de duplicados**
```python
# Verificar email duplicado
email_existente = session.execute(
    text("SELECT id FROM estudiantes WHERE email = :email"), 
    {"email": email}
).first()

if email_existente:
    return {"error": "El email ya está registrado"}
```

#### 4. **Rollback en operaciones fallidas**
```python
except Exception as e:
    session.rollback()  # Deshace cambios si algo falla
    return {"error": f"Error: {str(e)}"}
```

#### 5. **Mensajes de error descriptivos**
- "El ID debe ser un número positivo"
- "Email debe ser válido"
- "El email ya está registrado"
- "Semestre debe estar entre 1 y 10"

### Datos de ejemplo (iguales al ejemplo básico)

```sql
INSERT INTO estudiantes (nombre, apellido, email, carrera, semestre, activo) VALUES
('Juan', 'Pérez', 'juan.perez@email.com', 'Ingeniería en Sistemas', 3, TRUE),
('María', 'González', 'maria.gonzalez@email.com', 'Administración', 5, TRUE),
('Carlos', 'López', 'carlos.lopez@email.com', 'Ingeniería en Sistemas', 2, TRUE),
('Ana', 'Martínez', 'ana.martinez@email.com', 'Psicología', 4, TRUE),
('Luis', 'Rodríguez', 'luis.rodriguez@email.com', 'Contaduría', 1, TRUE);
```

### Comparación con el ejemplo básico:

| Aspecto | Ejemplo Básico | Con Manejo de Errores |
|---------|----------------|----------------------|
| **Try-Catch** | ❌ No | ✅ En todos los endpoints |
| **Validaciones** | ❌ Mínimas | ✅ Completas |
| **Rollback** | ❌ No | ✅ En operaciones de escritura |
| **Mensajes de error** | ❌ Genéricos | ✅ Descriptivos |
| **Verificaciones** | ❌ Solo existencia | ✅ Duplicados y formatos |
