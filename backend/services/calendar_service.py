import os
import pickle
from datetime import datetime, timedelta
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS_PATH = 'credentials/credentials.json'
TOKEN_PATH = 'credentials/token.pickle'

def get_calendar_service():
    creds = None
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'wb') as token:
            pickle.dump(creds, token)
    return build('calendar', 'v3', credentials=creds)

def crear_evento(summary, description, start_datetime, end_datetime):
    service = get_calendar_service()
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_datetime,
            'timeZone': 'America/Guayaquil',
        },
        'end': {
            'dateTime': end_datetime,
            'timeZone': 'America/Guayaquil',
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    return event.get('htmlLink')

def listar_eventos(dias=1):
    service = get_calendar_service()
    ahora = datetime.utcnow().isoformat() + 'Z'
    fin = (datetime.utcnow() + timedelta(days=dias)).isoformat() + 'Z'

    eventos_resultado = service.events().list(
        calendarId='primary',
        timeMin=ahora,
        timeMax=fin,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    return eventos_resultado.get('items', [])

def eliminar_evento(event_id):
    try:
        service = get_calendar_service()
        service.events().delete(calendarId='primary', eventId=event_id).execute()
        return True
    except Exception as e:
        return False

def obtener_evento(event_id):
    service = get_calendar_service()
    return service.events().get(calendarId='primary', eventId=event_id).execute()

def actualizar_evento(event_id, nuevo_evento):
    service = get_calendar_service()
    return service.events().update(calendarId='primary', eventId=event_id, body=nuevo_evento).execute()
