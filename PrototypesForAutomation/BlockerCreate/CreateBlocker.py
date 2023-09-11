import os

import win32com.client as win32
from datetime import datetime, timedelta, time
import SpeakerProfile
outlook = win32.Dispatch("Outlook.Application")
def create_draft_invitation(subject, meeting_date, start_time, duration,attendees, optional_attendees, body):
    #outlook = win32com.client.Dispatch("Outlook.Application")


    speaker_name = [attendee.split(".")[0].capitalize() for attendee in attendees]
    print(speaker_name)
    # Open the pre-saved appointment item
    profile = SpeakerProfile.speakerType(attendees)
    if profile == "internal":
        template = os.path.join(os.getcwd(), 'BlockerTemplate.oft')
    else:
        template = os.path.join(os.getcwd(), 'BlockerTemplateExternal.oft')
    appointment = outlook.CreateItemFromTemplate(template)

    # set start and end time for meeting
    start_datetime = datetime.combine(meeting_date, start_time)
    end_datetime = start_datetime + duration

    # create new appointment item
    #appointment = appointments.Add(1)
    appointment.Start = start_datetime
    appointment.End = end_datetime
    appointment.Subject = subject
    if len(attendees)>1 and profile =="internal":
        appointment.Body = appointment.Body.replace("Speaker_name", "Colleagues")
    else:
        appointment.Body = appointment.Body.replace("Speaker_name", speaker_name[0])
    # set the meeting status to olMeeting (1), so it becomes a meeting invitation
    appointment.MeetingStatus = 1



    # add necessary attendees
    for attendee in attendees:
        recipient= appointment.Recipients.Add(attendee)
        recipient.Type = 1

    # add optional attendees (the equivalent of a 'cc')
    for attendee in optional_attendees:
        recipient = appointment.Recipients.Add(attendee)
        recipient.Type = 2  # optional attendees

    # do not send but only create a draft appointment
    appointment.Save()
    appointment.Display(False)
"""
#test the function
subject = "Blocker for Ecosystem:"
meeting_date = datetime(2023, 12, 14).date()  # for example, it's set to Dec 11, 2023
start_time = time(15, 55)  # 3:00 PM
duration = timedelta(hours=1, minutes=5)  # 1 hours meeting
attendees = []  # list of attendees emails
attendees = input("Enter the email addresses for required attendees, separated by commas: ").split(',')
optional_attendees = ['priya.singh05@sap.com']  # list of optional (cc) attendees emails
create_draft_invitation(subject, meeting_date, start_time, duration, attendees, optional_attendees, body='')
"""
