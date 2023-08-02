import calendar

import win32com.client as win32
import os
from datetime import datetime, timedelta

internal_template = os.path.join(os.getcwd(), 'Template_Internal.oft')
external_template = os.path.join(os.getcwd(), 'Template_External.oft')
def create_outlook_draft():
    to = input("Enter Speakers name: ")
    date_input = input("enter session date (YYYY-MM-DD): ")
    title_input = input("enter topic of session")
    print(external_template)
    date = datetime.strptime(date_input, "%Y-%m-%d").date()
    print(date)
    search_appointment(date)
    # extract speakers name from recipient
    speaker_name = to.split(".")[0].capitalize()  #assuming email is of form name.lastname@example.com
    speaker_type = to.split("@")[1]
    print(speaker_type)
    outlook = win32.Dispatch("Outlook.Application")
    position = speaker_name.find("sap.com")
    if position != -1:
        print("speaker is from sap", position)
        mail = outlook.CreateItemFromTemplate(internal_template)
    else:
        mail = outlook.CreateItemFromTemplate(external_template)
    mail.HTMLBody = mail.HTMLBody.replace("Speaker_name", speaker_name)
    mail.HTMLBody = mail.HTMLBody.replace("TOPIC", title_input)
    mail.HTMLBody = mail.HTMLBody.replace("DATE", date_input)
    mail.HTMLBody = mail.HTMLBody.replace("Working_Student","Priya")
    mail.To = to
    mail.CC = "klaus@haeuptle@sap.com"
    mail.Save()
    mail.Display()


def search_appointment(date):
    outlook = win32.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    calendar = namespace.GetDefaultFolder(9)
    # Get the start of the day and end of the day for the specified date
    start = datetime(date.year, date.month, date.day)
    end = start + timedelta(days=1)
    print(start,end)
    # Get the appointments within the specified date range
    appointments = calendar.Items.Restrict("[Start] >= '{}' AND [End] <= '{}'".format(start.strftime('%m/%d/%Y'), end.strftime('%m/%d/%Y')))

    for appointment in appointments:
        #print("Subject:", appointment.Subject)
        if appointment.Subject == "Lectures - Morning":
            print("Organizer:", appointment.Organizer)
            print("Subject:", appointment.Subject)
            print("Date:", appointment.Start)


create_outlook_draft()

