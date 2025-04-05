import json
import os
from datetime import datetime, timedelta
from backend.core.asistente_archivo import cargar_objetivos_desde_json
from backend.core.sugerencias import generar_sugerencia
from backend.core.constantes import RUTA_ASISTENTE


def _cargar_datos():
    if not os.path.exists(RUTA_ASISTENTE):
        return {"objetivos": [], "recordatorios": []}
    with open(RUTA_ASISTENTE, "r") as f:
        return json.load(f)

def _guardar_datos(data):
    with open(RUTA_ASISTENTE, "w") as f:
        json.dump(data, f, indent=4, default=str)

def agregar_objetivo(nombre, descripcion, fecha_limite):
    datos = _cargar_datos()
    objetivo = {
        "id": f"objetivo-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "nombre": nombre,
        "descripcion": descripcion,
        "fecha_limite": fecha_limite.isoformat(),
        "progreso": 0
    }
    datos["objetivos"].append(objetivo)
    _guardar_datos(datos)
    print("✅ Objetivo agregado.")

def agregar_recordatorio(mensaje, minutos):
    datos = _cargar_datos()
    fecha_hora = datetime.now() + timedelta(minutes=minutos)
    recordatorio = {
        "id": f"recordatorio-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "mensaje": mensaje,
        "fecha_hora": fecha_hora.isoformat()
    }
    datos["recordatorios"].append(recordatorio)
    _guardar_datos(datos)
    print("✅ Recordatorio agregado.")


def mostrar_sugerencia():
    objetivos = cargar_objetivos_desde_json()  # 🚨 Aquí es clave usar esta función, no Google Calendar
    sugerencia = generar_sugerencia(objetivos)
    print("\n💡 Sugerencia:")
    print(sugerencia)


def cargar_objetivos():
    try:
        with open('asistente.json', 'r') as file:
            datos = json.load(file)
            return datos.get('objetivos', [])
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo 'asistente.json'.")
        return []
    except json.JSONDecodeError:
        print("⚠️ Error al leer el archivo 'asistente.json'.")
        return []