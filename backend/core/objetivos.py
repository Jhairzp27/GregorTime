# Aquí se encontrará la gestión de objetivos y metas personales
import datetime

class Objetivo:
    def __init__(self, nombre, descripcion, fecha_limite):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.progreso = 0

    def actualizar_progreso(self, nuevo_progreso):
        self.progreso = max(0, min(100, nuevo_progreso))

    def es_vencido(self):
        return datetime.datetime.now() > self.fecha_limite

    def __str__(self):
        return f"Objetivo: {self.nombre} - Progreso: {self.progreso}%"


def crear_objetivo(nombre, descripcion, fecha_limite):
    return Objetivo(nombre, descripcion, fecha_limite)


