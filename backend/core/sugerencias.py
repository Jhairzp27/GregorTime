from datetime import datetime

def generar_sugerencia(objetivos):
    print("DEBUG - Objetivos recibidos:", objetivos)

    # Filtrar y ordenar los objetivos según la fecha límite
    objetivos_validos = []
    for obj in objetivos:
        if isinstance(obj, dict) and 'nombre' in obj and 'fecha_limite' in obj:
            try:
                # Convertir la fecha
                obj['fecha_parseada'] = datetime.fromisoformat(obj['fecha_limite'])
                objetivos_validos.append(obj)
                print(f"DEBUG - Fecha convertida correctamente para {obj['nombre']} - {obj['fecha_parseada']}")
            except ValueError:
                print(f"⚠️ No se pudo convertir la fecha para el objetivo: {obj['nombre']} ({obj['fecha_limite']})")
                continue  # ignoramos si la fecha no es válida

    print("DEBUG - Objetivos válidos antes de ordenar:", objetivos_validos)

    if not objetivos_validos:
        return "No hay objetivos válidos disponibles aún."

    # Ordenamos los objetivos por la fecha límite
    objetivos_ordenados = sorted(objetivos_validos, key=lambda x: x['fecha_parseada'])
    seleccion = objetivos_ordenados[:3] if len(objetivos_ordenados) >= 3 else objetivos_ordenados
    sugerencia = seleccion[0]  # Se elige el objetivo más cercano

    return f"🎯 Prioriza: '{sugerencia['nombre']}' - {sugerencia.get('descripcion', '')} (para {sugerencia.get('fecha_limite', 'pronto')})"
