from backend.services.calendar_service import crear_evento, listar_eventos, eliminar_evento, obtener_evento, actualizar_evento

def crear_evento_personalizado(nombre, descripcion, fecha_inicio, fecha_fin):
    try:
        enlace = crear_evento(nombre, descripcion, fecha_inicio, fecha_fin)
        return True, enlace
    except Exception as e:
        return False, str(e)
    
def obtener_eventos_dias(n=1):
    return listar_eventos(dias=n)

def eliminar_evento_por_id(event_id):
    return eliminar_evento(event_id)


def obtener_evento_por_id(event_id):
    return obtener_evento(event_id)

def actualizar_evento_existente(event_id, nuevos_datos):
    try:
        evento_actual = obtener_evento(event_id)
        evento_actual['summary'] = nuevos_datos['summary']
        evento_actual['description'] = nuevos_datos['description']
        evento_actual['start']['dateTime'] = nuevos_datos['start']
        evento_actual['end']['dateTime'] = nuevos_datos['end']
        evento_actual['start']['timeZone'] = 'America/Guayaquil'
        evento_actual['end']['timeZone'] = 'America/Guayaquil'
        evento_actualizado = actualizar_evento(event_id, evento_actual)
        return True, evento_actualizado.get('htmlLink')
    except Exception as e:
        return False, str(e)
