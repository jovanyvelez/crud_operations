# Ejercicios CRUD con FastAPI y SQL
## Tarea para la próxima clase - Sistema de Estudiantes

### Objetivo
Implementar un sistema CRUD completo utilizando FastAPI y consultas SQL directas, trabajando **TODOS** con la misma tabla de estudiantes para facilitar la comprensión y comparación.

### Modalidad de Trabajo
- **Grupos de 2 estudiantes** (38 estudiantes = 19 grupos)
- **TODOS los grupos trabajan con la tabla `estudiantes`**
- **Cada grupo implementa un conjunto diferente de endpoints** (asignados por el profesor)

### Tabla Única para Todos
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

### Instrucciones Generales
1. **Todos usan la misma tabla** `estudiantes` con los mismos campos
2. **Incluir manejo de errores básico** en todas las operaciones
3. Usar consultas SQL directas con `text()` de SQLAlchemy
4. Usar `from bd import SessionDepends` como en el ejemplo
5. **Implementar solo los endpoints asignados** a su grupo

### Requisitos Técnicos
- Python con FastAPI
- SQLAlchemy para conexión a base de datos
- Base de datos SQLite
- Estructura idéntica al proyecto de héroes y ejemplos dados

---

## Asignación de Endpoints por Grupo

### **Grupo 1: Operaciones Básicas**
**Endpoints a implementar:**
- GET `/estudiantes` - Listar todos los estudiantes
- GET `/estudiantes/{id}` - Obtener estudiante por ID
- POST `/estudiantes` - Crear nuevo estudiante

### **Grupo 2: Operaciones Básicas + Actualización**
**Endpoints a implementar:**
- GET `/estudiantes` - Listar todos los estudiantes
- GET `/estudiantes/{id}` - Obtener estudiante por ID  
- PUT `/estudiantes/{id}` - Actualizar estudiante completo

### **Grupo 3: Operaciones Básicas + Eliminación**
**Endpoints a implementar:**
- GET `/estudiantes` - Listar todos los estudiantes
- POST `/estudiantes` - Crear nuevo estudiante
- DELETE `/estudiantes/{id}` - Eliminar estudiante por ID

### **Grupo 4: CRUD Completo Básico**
**Endpoints a implementar:**
- GET `/estudiantes` - Listar todos los estudiantes
- GET `/estudiantes/{id}` - Obtener estudiante por ID
- POST `/estudiantes` - Crear nuevo estudiante
- DELETE `/estudiantes/{id}` - Eliminar estudiante

### **Grupo 5: Búsqueda por Email**
**Endpoints a implementar:**
- GET `/estudiantes` - Listar todos los estudiantes
- GET `/estudiantes/email/{email}` - Buscar por email
- POST `/estudiantes` - Crear nuevo estudiante

### **Grupo 6: Filtro por Carrera**
**Endpoints a implementar:**
- GET `/estudiantes` - Listar todos los estudiantes
- GET `/estudiantes/carrera/{carrera}` - Estudiantes por carrera
- POST `/estudiantes` - Crear nuevo estudiante

### **Grupo 7: Filtro por Semestre**
**Endpoints a implementar:**
- GET `/estudiantes` - Listar todos los estudiantes
- GET `/estudiantes/semestre/{semestre}` - Estudiantes por semestre
- PUT `/estudiantes/{id}` - Actualizar estudiante

### **Grupo 8: Solo Activos**
**Endpoints a implementar:**
- GET `/estudiantes` - Listar todos los estudiantes
- GET `/estudiantes/activos` - Solo estudiantes activos
- PATCH `/estudiantes/{id}/estado` - Cambiar estado activo/inactivo

### **Grupo 9: Actualización de Promedio**
**Endpoints a implementar:**
- GET `/estudiantes` - Listar todos los estudiantes
- GET `/estudiantes/{id}` - Obtener estudiante por ID
- PATCH `/estudiantes/{id}/promedio` - Actualizar solo promedio

### **Grupo 10: Búsqueda por Nombre**
**Endpoints a implementar:**
- GET `/estudiantes` - Listar todos los estudiantes
- GET `/estudiantes/nombre/{nombre}` - Buscar por nombre (contiene)
- POST `/estudiantes` - Crear nuevo estudiante

### **Grupo 11: Eliminar por Email**
**Endpoints a implementar:**
- GET `/estudiantes` - Listar todos los estudiantes
- POST `/estudiantes` - Crear nuevo estudiante
- DELETE `/estudiantes/email/{email}` - Eliminar por email

### **Grupo 12: Estudiantes por Carrera y Semestre**
**Endpoints a implementar:**
- GET `/estudiantes/carrera/{carrera}/semestre/{semestre}` - Filtro combinado
- POST `/estudiantes` - Crear nuevo estudiante
- PUT `/estudiantes/{id}` - Actualizar estudiante

### **Grupo 13: Actualización de Teléfono**
**Endpoints a implementar:**
- GET `/estudiantes` - Listar todos los estudiantes
- GET `/estudiantes/{id}` - Obtener estudiante por ID
- PATCH `/estudiantes/{id}/telefono` - Actualizar solo teléfono

### **Grupo 14: Eliminar Inactivos**
**Endpoints a implementar:**
- GET `/estudiantes` - Listar todos los estudiantes
- DELETE `/estudiantes/inactivos` - Eliminar todos los inactivos
- PATCH `/estudiantes/{id}/activar` - Activar estudiante

### **Grupo 15: Contar Estudiantes**
**Endpoints a implementar:**
- GET `/estudiantes/count` - Contar total de estudiantes
- GET `/estudiantes/count/carrera/{carrera}` - Contar por carrera
- GET `/estudiantes` - Listar todos los estudiantes

### **Grupo 16: Promedio por Carrera**
**Endpoints a implementar:**
- GET `/estudiantes/promedio/carrera/{carrera}` - Promedio de calificaciones por carrera
- GET `/estudiantes/carrera/{carrera}` - Estudiantes por carrera
- POST `/estudiantes` - Crear nuevo estudiante

### **Grupo 17: Estudiantes sin Teléfono**
**Endpoints a implementar:**
- GET `/estudiantes/sin-telefono` - Estudiantes sin teléfono registrado
- PATCH `/estudiantes/{id}/telefono` - Actualizar teléfono
- GET `/estudiantes` - Listar todos los estudiantes

### **Grupo 18: Rango de Semestres**
**Endpoints a implementar:**
- GET `/estudiantes/semestre/rango/{min}/{max}` - Estudiantes en rango de semestres
- GET `/estudiantes/semestre/{semestre}` - Estudiantes por semestre específico
- PUT `/estudiantes/{id}` - Actualizar estudiante

### **Grupo 19: CRUD Completo Avanzado**
**Endpoints a implementar:**
- GET `/estudiantes` - Listar todos los estudiantes
- POST `/estudiantes` - Crear nuevo estudiante
- PUT `/estudiantes/{id}` - Actualizar estudiante completo
- DELETE `/estudiantes/{id}` - Eliminar estudiante
- GET `/estudiantes/estadisticas` - Estadísticas básicas (total, por carrera, etc.)

---

---

## Datos de Ejemplo para Insertar

Todos los grupos deben usar estos mismos datos de prueba:

```sql
INSERT INTO estudiantes (nombre, apellido, email, carrera, semestre, telefono, promedio, activo) VALUES
('Juan', 'Pérez', 'juan.perez@email.com', 'Ingeniería en Sistemas', 3, '555-0001', 8.5, TRUE),
('María', 'González', 'maria.gonzalez@email.com', 'Administración', 5, '555-0002', 9.2, TRUE),
('Carlos', 'López', 'carlos.lopez@email.com', 'Ingeniería en Sistemas', 2, NULL, 7.8, TRUE),
('Ana', 'Martínez', 'ana.martinez@email.com', 'Psicología', 4, '555-0004', 8.9, TRUE),
('Luis', 'Rodríguez', 'luis.rodriguez@email.com', 'Contaduría', 1, '555-0005', NULL, TRUE),
('Sofia', 'Hernández', 'sofia.hernandez@email.com', 'Medicina', 6, NULL, 9.5, TRUE),
('Diego', 'Torres', 'diego.torres@email.com', 'Derecho', 3, '555-0007', 8.1, FALSE),
('Carmen', 'Vásquez', 'carmen.vasquez@email.com', 'Ingeniería en Sistemas', 4, '555-0008', 8.7, TRUE),
('Roberto', 'Jiménez', 'roberto.jimenez@email.com', 'Administración', 2, '555-0009', NULL, TRUE),
('Lucía', 'Morales', 'lucia.morales@email.com', 'Psicología', 5, NULL, 9.0, FALSE);
```

---

## Criterios de Evaluación

### Funcionalidad (40%)
- ✅ Implementación correcta de todos los endpoints asignados
- ✅ Manejo correcto de parámetros y respuestas
- ✅ Operaciones de base de datos funcionando

### Manejo de Errores (35%)
- ✅ **Try-catch en todos los endpoints**
- ✅ **Validaciones básicas** (IDs positivos, campos requeridos)
- ✅ **Verificación de existencia** antes de UPDATE/DELETE
- ✅ **Mensajes de error descriptivos**
- ✅ **Rollback en operaciones de escritura**

### Código SQL (15%)
- ✅ Uso correcto de consultas SQL con `text()`
- ✅ Manejo apropiado de campos NULL
- ✅ Parámetros para evitar SQL injection

### Estructura y Presentación (10%)
- ✅ Código limpio y comentado
- ✅ Presentación clara en clase
- ✅ Demostración de endpoints funcionando

---

## Entrega

**Fecha límite:** Próxima clase  
**Modalidad:** Grupos de 2 estudiantes  
**Asignación:** El profesor asigna los grupos y endpoints

**Formato:** Proyecto completo con:
- Archivo principal de FastAPI (`main.py`)
- Archivo de configuración de base de datos (`bd.py`) 
- Base de datos SQLite con los datos de ejemplo proporcionados
- README.md con documentación básica

### Elementos requeridos:
1. **Tabla única** `estudiantes` con la estructura exacta proporcionada
2. **Solo los endpoints asignados** a su grupo
3. **Manejo básico de errores** con try-catch
4. **10 registros de ejemplo** (los proporcionados)
5. **Presentación de 5 minutos** mostrando funcionamiento

### Validaciones mínimas esperadas:
- IDs deben ser números positivos
- Emails deben contener "@"
- Semestre entre 1 y 10
- Campos requeridos no pueden estar vacíos
- Verificar existencia antes de actualizar/eliminar

---

## Ejemplo de Estructura del Proyecto

```
proyecto_estudiantes_grupo_X/
├── main.py              # Solo endpoints asignados a su grupo
├── bd.py               # Configuración de base de datos
├── estudiantes.db      # Base de datos con los 10 registros
├── README.md           # Documentación de sus endpoints
└── requirements.txt    # fastapi, sqlalchemy, uvicorn
```

---

## Presentación en Clase

### Cada grupo tendrá 5 minutos para:
1. **Mostrar la tabla** con los datos cargados
2. **Demostrar sus endpoints** funcionando (usar Swagger/Postman)
3. **Mostrar manejo de errores** (casos de error intencionales)
4. **Explicar brevemente** el código más importante

### Orden de presentación:
- Grupos 1-5: Operaciones básicas
- Grupos 6-10: Búsquedas y filtros
- Grupos 11-15: Operaciones específicas
- Grupos 16-19: Funcionalidades avanzadas

---

**¡Todos trabajando con la misma tabla facilita la comprensión y comparación! 🚀**

---

## Recursos Adicionales

- [Documentación FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy Text](https://docs.sqlalchemy.org/en/14/core/tutorial.html#using-textual-sql)
- Revisar el código de ejemplo del proyecto de héroes

---

**¡Buena suerte y a programar! 🚀**
