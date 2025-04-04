from frontend.desktop.console_ui import (
    editar_evento_desde_consola,
    pedir_datos_evento,
    mostrar_resultado,
    mostrar_menu,
    mostrar_eventos,
    seleccionar_evento_para_borrar
)
from backend.controllers.evento_controller import (
    crear_evento_personalizado,
    obtener_eventos_dias,
    eliminar_evento_por_id
)

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            nombre, descripcion, inicio, fin = pedir_datos_evento()
            if not nombre:
                continue
            exito, mensaje = crear_evento_personalizado(nombre, descripcion, inicio, fin)
            mostrar_resultado(exito, mensaje)

        elif opcion == '2':
            eventos = obtener_eventos_dias(7)
            mostrar_eventos(eventos)

        elif opcion == '3':
            eventos = obtener_eventos_dias(7)
            event_id = seleccionar_evento_para_borrar(eventos)
            if event_id:
                resultado = eliminar_evento_por_id(event_id)
                if resultado:
                    print("✅ Evento eliminado correctamente.")
                else:
                    print("❌ Hubo un problema al eliminar el evento.")
            else:
                print("❌ Eliminación cancelada.")
                
        elif opcion == '4':
            eventos = obtener_eventos_dias(7)
            event_id = seleccionar_evento_para_borrar(eventos)  # Reutilizamos selección
            if event_id:
                from backend.controllers.evento_controller import (
                    obtener_evento_por_id, actualizar_evento_existente
                )
                evento = obtener_evento_por_id(event_id)
                nuevos_datos = editar_evento_desde_consola(evento)
                exito, mensaje = actualizar_evento_existente(event_id, nuevos_datos)
                if exito:
                    print(f"✅ Evento modificado correctamente: {mensaje}")
                else:
                    print(f"❌ Error al modificar evento: {mensaje}")
            else:
                print("❌ Modificación cancelada.")
                
        elif opcion == '0':
            print("👋 ¡Hasta pronto!")
            break

        else:
            print("⚠️ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
