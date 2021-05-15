import json
from create_event import createEvent, findAllAppointments

def lambda_handler(event, context):
    list = findAllAppointments()
    if list:
        for x in list:
            createEvent(x["docemail"], x["patientemail"], x["date"])

