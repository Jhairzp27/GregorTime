
from backend.core.asistente import (
    agregar_objetivo,
    agregar_recordatorio,
    mostrar_sugerencia
)
from datetime import datetime

def usar_asistente():
    while True:
        print("\n🤖 Asistente inteligente")
        print("1. Agregar objetivo")
        print("2. Agregar recordatorio")
        print("3. Ver sugerencia del día")
        print("0. Volver al menú principal")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == '1':
            nombre = input("🎯 Nombre del objetivo: ").strip()
            descripcion = input("📝 Descripción: ").strip()
            fecha_limite = input("📆 Fecha límite (YYYY-MM-DDTHH:MM:SS): ").strip()
            try:
                fecha = datetime.strptime(fecha_limite, "%Y-%m-%dT%H:%M:%S")
                agregar_objetivo(nombre, descripcion, fecha)
            except ValueError:
                print("⚠️ Formato de fecha inválido. Usa YYYY-MM-DDTHH:MM:SS")

        elif opcion == '2':
            mensaje = input("🔔 Mensaje del recordatorio: ").strip()
            minutos = input("⏳ ¿En cuántos minutos quieres que se active?: ").strip()
            if minutos.isdigit():
                agregar_recordatorio(mensaje, int(minutos))
            else:
                print("⚠️ Debes ingresar un número válido.")

        elif opcion == '3':
            mostrar_sugerencia()

        elif opcion == '0':
            print("👋 Volviendo al menú principal...")
            break

        else:
            print("⚠️ Opción inválida.")
