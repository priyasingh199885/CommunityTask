import datetime as dt
import pytz
import win32com.client

def datetime_to_ole(datetime_obj):
    # Convert datetime object to OLE Automation date
    return datetime_obj.strftime("%m/%d/%Y %H:%M:%S")

def create_draft_meeting_invite_local(subject, start_datetime, end_datetime, location, body_text, recipients, organizer_email):
    """
    Create a draft meeting invite using the local Outlook application.

    Parameters
    ----------
    subject : str
        Subject of the meeting.
    start_datetime : datetime.datetime
        Start date and time of the meeting in UTC.
    end_datetime : datetime.datetime
        End date and time of the meeting in UTC.
    location : str
        Meeting location.
    body_text : str
        Meeting description and additional details.
    recipients : list of str
        List of recipient email addresses.
    organizer_email : str
        Email address of the meeting organizer.

    Returns
    -------
    None
    """
    # Start the Outlook application
    outlook_app = win32com.client.Dispatch('Outlook.Application')

    # Create a new appointment item
    appt = outlook_app.CreateItem(1)  # 1: olAppointmentItem

    # Set the appointment properties
    appt.Subject = subject
    appt.Start = datetime_to_ole(start_datetime)
    appt.End = datetime_to_ole(end_datetime)
    # appt.Location = location #empty location is a teams meeting
    appt.Body = body_text

    # Add organizer email if provided
    if organizer_email:
        organizer = appt.Recipients.Add(organizer_email)
        organizer.Resolve()

    # Add recipients
    for email in recipients:
        recipient = appt.Recipients.Add(email)
        recipient.Resolve()

    # Disable request responses
    appt.ResponseRequested = False
    #appt.AllowNewTimeProposal = False #it appears that the AllowNewTimeProposal property is not available for use within the local Outlook application using the win32com.client library.

    # Save the meeting request as draft (3: olMeeting)
    appt.Display(True)  # Display the meeting invite in a non-modal dialog

    # Remove organizer from recipients and set the MeetingStatus property after displaying the invite
    # if organizer_email:
    #    organizer.Delete()
    # appt.MeetingStatus = 3

    print("Meeting invite opened as a draft.")


if __name__ == "__main__":
    # Test data
    subject = "Team Meeting"
    start_datetime = dt.datetime(2023, 6, 26, 15, 0, tzinfo=pytz.UTC)
    end_datetime = dt.datetime(2023, 6, 26, 16, 0, tzinfo=pytz.UTC)
    location = "Meeting Room 1"
    body_text = "This is to discuss our upcoming project."
    recipients = ["klaus.haeuptle@sap.com", "priya.singh05@sap.com"]
    organizer_email = "klaus.haeuptle@sap.com"

    # Create draft meeting invite
    create_draft_meeting_invite_local(subject, start_datetime, end_datetime, location, body_text, recipients, organizer_email)
