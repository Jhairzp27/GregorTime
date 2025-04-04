from datetime import datetime

def mostrar_menu():
    print("\n🗂️ ¿Qué deseas hacer?")
    print("1. Crear un evento")
    print("2. Ver eventos próximos")
    print("3. Eliminar un evento")
    print("4. Modificar un evento")
    print("0. Salir")
    return input("Selecciona una opción: ").strip()

def mostrar_eventos(eventos):
    if not eventos:
        print("😴 No tienes eventos próximos.")
        return
    print("\n📅 Eventos encontrados:")
    for i, evento in enumerate(eventos, 1):
        nombre = evento.get('summary', 'Sin título')
        inicio = evento['start'].get('dateTime', evento['start'].get('date'))
        print(f"{i}. {nombre} - {inicio}")

def seleccionar_evento_para_borrar(eventos):
    mostrar_eventos(eventos)
    opcion = input("🔢 Ingresa el número del evento que deseas eliminar (o 0 para cancelar): ").strip()
    if opcion.isdigit():
        indice = int(opcion)
        if indice == 0 or indice > len(eventos):
            return None
        return eventos[indice - 1].get('id')
    return None


def pedir_datos_evento():
    print("\n🔔 Crear nuevo evento en Google Calendar")

    nombre = input("📌 Nombre del evento: ").strip()
    descripcion = input("📝 Descripción: ").strip()

    fecha_inicio = pedir_fecha_valida("📅 Fecha y hora inicio (YYYY-MM-DDTHH:MM:SS): ")
    fecha_fin = pedir_fecha_valida("📅 Fecha y hora fin (YYYY-MM-DDTHH:MM:SS): ")

    print("\n🧐 Revisa la información ingresada:")
    print(f"🗓️  Evento: {nombre}")
    print(f"📄 Descripción: {descripcion}")
    print(f"🕐 Inicio: {fecha_inicio}")
    print(f"🕐 Fin: {fecha_fin}")

    confirmacion = input("¿Deseas agendar este evento? (s/n): ").lower()
    if confirmacion == 's':
        return nombre, descripcion, fecha_inicio, fecha_fin
    else:
        print("❌ Evento cancelado por el usuario.")
        return None, None, None, None

def pedir_fecha_valida(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            datetime.strptime(valor, "%Y-%m-%dT%H:%M:%S")
            return valor
        except ValueError:
            print("⚠️ Formato inválido. Usa el formato correcto: YYYY-MM-DDTHH:MM:SS")

def mostrar_resultado(success, mensaje):
    if success:
        print(f"✅ Evento creado exitosamente: {mensaje}")
    else:
        print(f"❌ Error al crear evento: {mensaje}")

def editar_evento_desde_consola(evento):
    print("\n✏️ Edición de evento:")
    print(f"Evento actual: {evento.get('summary', 'Sin título')}")
    nombre = input("📌 Nuevo nombre del evento (deja vacío para no cambiar): ").strip()
    descripcion = input("📝 Nueva descripción (deja vacío para no cambiar): ").strip()

    inicio_actual = evento['start'].get('dateTime', '')
    fin_actual = evento['end'].get('dateTime', '')

    nueva_fecha_inicio = input(f"📅 Nueva fecha/hora de inicio (actual: {inicio_actual}): ").strip()
    nueva_fecha_fin = input(f"📅 Nueva fecha/hora de fin (actual: {fin_actual}): ").strip()

    # Usar valores actuales si el usuario deja vacío
    nombre = nombre if nombre else evento.get('summary', '')
    descripcion = descripcion if descripcion else evento.get('description', '')
    nueva_fecha_inicio = nueva_fecha_inicio if nueva_fecha_inicio else inicio_actual
    nueva_fecha_fin = nueva_fecha_fin if nueva_fecha_fin else fin_actual

    return {
        'summary': nombre,
        'description': descripcion,
        'start': nueva_fecha_inicio,
        'end': nueva_fecha_fin
    }
