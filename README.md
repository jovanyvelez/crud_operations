# Sistema CRUD con FastAPI y SQL Raw
## Proyecto educativo para aprender FastAPI con consultas SQL directas

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 📋 Descripción

Este repositorio contiene material educativo para enseñar **operaciones CRUD con FastAPI** utilizando **consultas SQL directas** con SQLAlchemy. El proyecto está diseñado para estudiantes que están aprendiendo desarrollo de APIs REST y manejo de bases de datos.

### 🎯 Objetivos del proyecto:
- Aprender FastAPI desde lo básico
- Entender operaciones CRUD (Create, Read, Update, Delete)
- Usar consultas SQL directas con `text()` de SQLAlchemy
- Implementar manejo de errores en APIs
- Trabajar con bases de datos SQLite

---

## 📁 Estructura del Proyecto

```
raw_sql/
├── main.py                     # Ejemplo principal (héroes)
├── bd.py                      # Configuración de base de datos
├── modelo_datos.py            # Modelos SQLAlchemy
├── marvel.db                  # Base de datos de ejemplo
├── pyproject.toml             # Configuración del proyecto
├── uv.lock                    # Dependencias
├── documentacion/             # Material educativo
│   ├── ejemplo_basico.md      # CRUD básico sin errores
│   ├── ejemplo_con_errores.md # CRUD con manejo de errores
│   └── ejercicios_crud_fastapi.md # 19 ejercicios para estudiantes
└── README.md                  # Esta documentación
```

---

## 🚀 Instalación y Uso

### Prerrequisitos
- Python 3.8 o superior
- pip o uv (recomendado)

### Instalación
```bash
# Clonar el repositorio
git clone <tu-repositorio>
cd raw_sql

# Instalar dependencias
pip install fastapi sqlalchemy uvicorn

# O usando uv (recomendado)
uv sync
```

### Ejecutar el proyecto principal
```bash
python main.py
```

La aplicación estará disponible en: `http://localhost:8000`

Documentación interactiva: `http://localhost:8000/docs`

---

## 📚 Material Educativo

### 1. **Ejemplo Principal** (`main.py`)
- Sistema de héroes con operaciones CRUD básicas
- Ejemplo de referencia mostrado en clase
- Endpoints: consultar, insertar, actualizar, borrar héroes

### 2. **Ejemplo Básico** (`documentacion/ejemplo_basico.md`)
- Sistema de estudiantes **SIN manejo de errores**
- Estructura simple y fácil de entender
- CRUD básico para aprender los conceptos fundamentales

### 3. **Ejemplo con Manejo de Errores** (`documentacion/ejemplo_con_errores.md`)
- Mismo sistema de estudiantes **CON manejo de errores**
- Try-catch en todos los endpoints
- Validaciones de entrada y rollback de transacciones
- Mensajes de error descriptivos

### 4. **Ejercicios para Estudiantes** (`documentacion/ejercicios_crud_fastapi.md`)
- 19 grupos de ejercicios diferentes
- Todos trabajan con la misma tabla `estudiantes`
- Asignación progresiva de dificultad
- Criterios de evaluación claros

---

## 🗃️ Base de Datos

### Tabla Principal (Héroes)
```sql
CREATE TABLE heroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    secret_name TEXT NOT NULL
);
```

### Tabla de Ejercicios (Estudiantes)
```sql
CREATE TABLE estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    email TEXT NOT NULL,
    carrera TEXT NOT NULL,
    semestre INTEGER NOT NULL,
    telefono TEXT,           -- Campo NULL
    promedio REAL,           -- Campo NULL  
    activo BOOLEAN DEFAULT TRUE
);
```

---

## 📖 Endpoints Disponibles

### Sistema de Héroes (main.py)
```http
GET    /consultar              # Lista todos los héroes
GET    /consultar/{heroe_id}   # Obtiene héroe por ID
POST   /insertar               # Crea nuevo héroe
PUT    /actualizar/{heroe_id}  # Actualiza héroe
DELETE /borrar/{heroe_id}      # Elimina héroe
```

### Parámetros de ejemplo:
```json
{
  "nombre": "Spider-Man",
  "edad": 25,
  "secreto": "Peter Parker"
}
```

---

## 🎓 Para Estudiantes

### Flujo de Aprendizaje Recomendado:

1. **Estudiar** el ejemplo principal (`main.py`)
2. **Comparar** con el ejemplo básico de estudiantes
3. **Analizar** las diferencias con el ejemplo que incluye manejo de errores
4. **Implementar** el ejercicio asignado por el profesor
5. **Presentar** en clase (5 minutos por grupo)

### Conceptos Clave a Aprender:
- ✅ Configuración de FastAPI
- ✅ Conexión a base de datos con SQLAlchemy
- ✅ Consultas SQL con `text()`
- ✅ Manejo de parámetros para evitar SQL injection
- ✅ Try-catch para manejo de errores
- ✅ Validaciones de entrada
- ✅ Rollback de transacciones
- ✅ Códigos de respuesta HTTP

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **FastAPI** | 0.104+ | Framework web para APIs REST |
| **SQLAlchemy** | 2.0+ | ORM y consultas SQL |
| **SQLite** | 3.0+ | Base de datos ligera |
| **Uvicorn** | 0.24+ | Servidor ASGI |
| **Python** | 3.8+ | Lenguaje de programación |

---

## 📝 Ejemplo de Código

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
                "email": estudiante.email
            })
        
        return {"estudiantes": estudiantes}
    
    except Exception as e:
        return {"error": f"Error al obtener estudiantes: {str(e)}"}
```

---

## 🤝 Contribuciones

Este es un proyecto educativo. Si eres estudiante:
- Haz fork del repositorio
- Implementa tu ejercicio asignado
- Crea un pull request con tu solución
- Documenta tu código claramente

---

## 📞 Soporte

Para dudas sobre el proyecto:
- Consulta la documentación en la carpeta `documentacion/`
- Revisa los ejemplos proporcionados
- Pregunta en clase o durante las tutorías

---

## 📄 Licencia

Este proyecto tiene fines educativos. Siéntete libre de usar el código para aprender y enseñar.

---

## 🏆 Créditos

Desarrollado como material educativo para la enseñanza de FastAPI y SQL.

**¡Happy coding! 🚀**