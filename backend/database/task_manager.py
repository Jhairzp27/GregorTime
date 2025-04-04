import json
import os
from datetime import datetime

RUTA_DB = "backend/database/tareas.json"

# Estructura de una tarea
def crear_tarea(nombre, descripcion, fecha_limite):
    return {
        "id": datetime.now().strftime("%Y%m%d%H%M%S"),  # ID único basado en fecha
        "nombre": nombre,
        "descripcion": descripcion,
        "fecha_limite": fecha_limite,
        "completada": False,
        "creada": datetime.now().isoformat()
    }

def cargar_tareas():
    if not os.path.exists(RUTA_DB):
        return []
    with open(RUTA_DB, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def guardar_tareas(tareas):
    with open(RUTA_DB, 'w', encoding='utf-8') as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)

def agregar_tarea(tarea):
    tareas = cargar_tareas()
    tareas.append(tarea)
    guardar_tareas(tareas)

def listar_tareas():
    return cargar_tareas()

def marcar_completada(tarea_id):
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            break
    guardar_tareas(tareas)

def eliminar_tarea(tarea_id):
    tareas = cargar_tareas()
    tareas = [t for t in tareas if t["id"] != tarea_id]
    guardar_tareas(tareas)
