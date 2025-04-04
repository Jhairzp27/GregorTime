from backend.database import task_manager
from datetime import datetime

def mostrar_menu_tareas():
    print("\n🗃️ Menú de tareas")
    print("1. Agregar nueva tarea")
    print("2. Ver tareas pendientes")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("0. Volver al menú principal")
    return input("Selecciona una opción: ").strip()

def pedir_datos_tarea():
    print("\n📝 Crear nueva tarea")
    nombre = input("📌 Nombre: ").strip()
    descripcion = input("📄 Descripción: ").strip()
    fecha = input("📅 Fecha límite (YYYY-MM-DD): ").strip()

    # Validación simple de fecha
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        print("⚠️ Fecha inválida. Usa el formato YYYY-MM-DD.")
        return None

    return task_manager.crear_tarea(nombre, descripcion, fecha)

def ver_tareas():
    tareas = task_manager.listar_tareas()
    if not tareas:
        print("📭 No tienes tareas registradas.")
        return
    print("\n📋 Lista de tareas:")
    for i, tarea in enumerate(tareas, 1):
        estado = "✅" if tarea["completada"] else "❌"
        print(f"{i}. {tarea['nombre']} [{estado}] - Límite: {tarea['fecha_limite']} (ID: {tarea['id']})")

def seleccionar_tarea():
    tareas = task_manager.listar_tareas()
    if not tareas:
        print("📭 No hay tareas para seleccionar.")
        return None
    ver_tareas()
    opcion = input("🔢 Ingresa el número de la tarea: ").strip()
    if opcion.isdigit():
        indice = int(opcion)
        if 1 <= indice <= len(tareas):
            return tareas[indice - 1]["id"]
    print("⚠️ Selección inválida.")
    return None

def gestionar_tareas():
    while True:
        opcion = mostrar_menu_tareas()

        if opcion == '1':
            nueva = pedir_datos_tarea()
            if nueva:
                task_manager.agregar_tarea(nueva)
                print("✅ Tarea agregada correctamente.")
        elif opcion == '2':
            ver_tareas()
        elif opcion == '3':
            tarea_id = seleccionar_tarea()
            if tarea_id:
                task_manager.marcar_completada(tarea_id)
                print("✅ Tarea marcada como completada.")
        elif opcion == '4':
            tarea_id = seleccionar_tarea()
            if tarea_id:
                task_manager.eliminar_tarea(tarea_id)
                print("🗑️ Tarea eliminada.")
        elif opcion == '0':
            break
        else:
            print("⚠️ Opción inválida.")
