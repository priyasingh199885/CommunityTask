import datetime
from datetime import datetime, timedelta, time
from BlockerCreate.CreateBlocker import create_draft_invitation
import eel
from MeetingDate import meetingdate

eel.init('') # 'web' is the directory where the your web files are present


@eel.expose
def create_draft_invitations(slot, week):
    print(week)
    #time to be 5 minutes before slot timings
    starting_time = slot.split("-")[0].split(" ")[1];
    week_day=slot.split("-")[0].split(" ")[0];
    print(week_day)
    print(starting_time)
    dt_object = datetime.strptime(starting_time, "%I%p")  # This will default to today's date
    new_dt_object = dt_object - timedelta(minutes=5)  # Subtract 5 minutes
    time_object = new_dt_object.time()  # Extract the new time
    #time_object = datetime.strptime(starting_time, "%I%p").time()
    print(time_object)
    meeting_date = datetime(2023, 12, 14).date()  # for example, it's set to Dec 11, 2023
    d = meetingdate(week,week_day)
    attendees = []  # list of attendees emails
    # attendees = input("Enter the email addresses for required attendees, separated by commas: ").split(',')
    optional_attendees = ['priya.singh05@sap.com']  # list of optional (cc) attendees emails
    create_draft_invitation(subject="Blocker for Ecosystem:",meeting_date=d,start_time=time_object,duration=timedelta(hours=1, minutes=5),attendees=attendees,optional_attendees=optional_attendees,body='')
    print(f"Executing function for slot: {slot}")
    return f"Function executed for slot: {slot}"



eel.start('output.html')