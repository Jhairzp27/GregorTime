import json
from backend.core.constantes import RUTA_ASISTENTE

def cargar_objetivos_desde_json():
    try:
        with open(RUTA_ASISTENTE, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
            objetivos = data.get("objetivos", [])
            print(f"DEBUG - Objetivos cargados desde {RUTA_ASISTENTE}: {objetivos}")
            return objetivos
    except FileNotFoundError:
        print(f"❌ Archivo {RUTA_ASISTENTE} no encontrado.")
    except json.JSONDecodeError as e:
        print(f"❌ Error al decodificar JSON: {e}")
    return []
