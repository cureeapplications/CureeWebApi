import json
from create_event import createEvent, findAllAppointments, updateBookedStatus

def lambda_handler(event, context):
    list = findAllAppointments()
    if list:
        for x in list:
            try:
                createEvent(x["Doc_Email"], x["Ptn_Email"], x["Start"], x["End"])
                updateBookedStatus(x["Id"])
            except:
                print("failed")

