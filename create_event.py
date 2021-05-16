from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import requests
from requests.structures import CaseInsensitiveDict
import json
from datetime import datetime



def createEvent(doctormail, attendeemail, startunix, endunix):
  service = get_calendar_service()
  d = datetime.fromtimestamp(int(str(startunix)[:-3]))
  e = datetime.fromtimestamp(int(str(endunix)[:-3]))
  start = d.isoformat()
  end = e.isoformat()
  event_result = service.events().insert(calendarId='primary', conferenceDataVersion= 1,
      body={
'summary': 'Doctor Appointment',
'location': 'Bellary',
'description': 'A chance to hear more about Corona Treatment.',
'start': {
  'dateTime':  start,
  'timeZone': 'Asia/Kolkata',
},
'end': {
  'dateTime': end,
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
  # filtered = list(filter(lambda x: x['statusid'] == 0, inp))
  return inp

def updateBookedStatus(appid):
  url = "https://oeco2uan71.execute-api.ap-south-1.amazonaws.com/api/Appointment/UpdateStatus/{}".format(appid)
  xep = requests.get(url)
  print(xep)


# def main():
#   list = findAllAppointments()
#   if list:
#       for x in list:
#         try:
#           createEvent(x["Doc_Email"], x["Ptn_Email"], x["Start"], x["End"])
#           updateBookedStatus(x["Id"])
#         except:
#           print("failed")

# if __name__ == "__main__":
#     main()


