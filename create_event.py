from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import requests
from requests.structures import CaseInsensitiveDict
import json
from datetime import datetime



def createEvent(doctormail, attendeemail, unixdate):
  service = get_calendar_service()
  d = datetime.fromtimestamp(unixdate)
  start = d.isoformat()
  end = (d + timedelta(hours=1)).isoformat()
  event_result = service.events().insert(calendarId='primary', conferenceDataVersion= 1,
      body={
'summary': 'Doctor Appointment',
'location': 'Bellary',
'description': 'A chance to hear more about Corona Treatment.',
'start': {
  'dateTime':  d.isoformat(),
  'timeZone': 'Asia/Kolkata',
},
'end': {
  'dateTime': (d + timedelta(hours=1)).isoformat(),
  'timeZone': 'Asia/Kolkata',
},
'recurrence': [
  'RRULE:FREQ=DAILY;COUNT=1'
],
'attendees': [
  {'email': doctormail,
'email':  attendeemail,}
],
'conferenceData': {
  'createRequest': {
    'requestId': 'sample123',
    'conferenceSolutionKey': { 'type': 'hangoutsMeet' },
  },
},
'reminders': {
  'useDefault': False,
  'overrides': [
    {'method': 'email', 'minutes': 6},
    {'method': 'popup', 'minutes': 6},
  ],
},
}

  ).execute()

def findAllAppointments():
  url = 'https://oeco2uan71.execute-api.ap-south-1.amazonaws.com/api/Appointment/GetAppointments'
  xep = requests.get(url)
  inp = xep.json()
  # input_list = [{'doctorname':"Pramod",'statusid':0}, {'doctorname':"Nityay",'statusid':1},{'doctorname':"Batnuj",'statusid':0}, {'doctorname':"Brityay",'statusid':1}]
  filtered = list(filter(lambda x: x['statusid'] == 0, inp))
  return filtered



