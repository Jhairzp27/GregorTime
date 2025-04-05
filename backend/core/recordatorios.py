from datetime import datetime, timedelta

class Recordatorio:
    def __init__(self, mensaje, fecha_hora):
        self.mensaje = mensaje
        self.fecha_hora = fecha_hora

    def es_hora(self):
        return datetime.now() >= self.fecha_hora

    def __str__(self):
        return f"Recordatorio: {self.mensaje} - Fecha/Hora: {self.fecha_hora}"


def crear_recordatorio(mensaje, minutos):
    fecha_hora = datetime.now() + timedelta(minutes=minutos)
    return Recordatorio(mensaje, fecha_hora)
