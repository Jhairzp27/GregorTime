# GregoLianaTime

Es un proyecto diseñado para optimizar la organización personal de los usuarios. Permite crear y monitorear rutinas de vida, enviar notificaciones o recordatorios de tareas, ofrecer una vista clara de horarios diarios y, adicionalmente, llevar un registro de cuentas e ingresos, facilitando así la mejora de hábitos y la gestión financiera.

App desarrollada en Python para gestionar tareas y eventos personales a través de la API de Google Calendar. Pensada para escritorio (y futura versión móvil), con funcionalidades que evolucionarán hacia un asistente inteligente.

---

## 🚀 Funcionalidades actuales

- Crear eventos personalizados desde consola
- Ver eventos programados (hasta 7 días)
- Eliminar eventos seleccionados
- Modificar eventos existentes (nombre, descripción, fecha/hora)
- Validación de entradas y confirmación previa

---

## 🛠️ Tecnologías

- Python
- Google Calendar API
- OAuth 2.0
- Arquitectura modular (MVC + servicios)
- Consola interactiva (modo CLI)

---

## ⚙️ Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/organizador-personal.git
   ```

2. Entra en la carpeta del proyecto:

   ```bash
    cd organizador-personal
    ```

3. Crea y activa un entorno virtual:

   ```bash
    python -m venv venv
    venv\Scripts\activate   # En Windows
    source venv/bin/activate  # En macOS/Linux
    
    ```

4. Instala las dependencias

   ```bash
   pip install -r requirements.txt
    
    ```

5. Coloca tu `credentials.js` en la carpeta `credentials/` (este archivo no se incluye por temas de seguridad)

   ```bash
    python main.py    
    ```

6. Ejecuta el programa:

   ```bash
   python main.py
   ```

>[!CAUTION]
> Es muy importante manejar las credenciales con precaución para evitar problemas de seguridad al implementarlo en sus códigos

---

## 📌 Próximas funcionalidades

- Sugerencias inteligentes en huecos libres
- Registro de metas y tareas personales
- Análisis de rendimiento semanal
- Versión móvil (Android) con Kivy o Flutter
- Asistente que recuerde objetivos y dé consejos

---

## 👨‍💻 Desarrollado por

**Jhair Zambrano**  
Gregoliana — 2025  

📚 [Documentación técnica completa](docs/arquitectura.md)

---
