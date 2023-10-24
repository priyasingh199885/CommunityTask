import win32com.client
from datetime import datetime, timedelta
#body
body = """Hi Speaker,

I have sent out the invitation. Looking forward to the session!

Regards,
Klaus

To ensure that the connection is stable and the audio is clear, please follow the best practices below:
1.	Make sure you have a calm space around you and that your camera works as talks are way more social and encouraging when one can see the speaker 💪🏿
2.	Directly connect to the fastest internet connection available.
3.	Shut down any programs NOT being used for the presentation.
4.	Do not use a photograph for a background. Solid color backgrounds with simple corporate logos work best.
5.	Have programs that you are screen-sharing open to the appropriate window and ready to demonstrate – avoid launching and logging into programs while screen sharing.
6.	Optimize room bandwidth to DSL regardless of your connection.
7.	If using a telephone for audio, use a handset or quality headset, NO SPEAKERPHONES as it will cause voice fluctuations and background audio will be picked up during the recording.
8.	Remember the participants after 15 minutes that they can ask questions in the chat
"""

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
calendar = outlook.GetDefaultFolder(9).Items  # "9" refers to the calendar folder

calendar.Sort("[Start]")  # Sort appointment items by start date
calendar.IncludeRecurrences = "True"
def UpdateBlockerBody(date_of_session):
    # Specify the date range
    date_obj = datetime.strptime(date_of_session, '%Y-%m-%d')
    #date_obj=date_of_session
    # add 1 day to the date
    new_date_obj = date_obj + timedelta(days=1)

    # if you want the new date as string, convert it back
    new_date_str = new_date_obj.strftime('%Y-%m-%d')

    begin_year = date_of_session
    end_year = new_date_str
    #begin_year = "08/23/2023"
    #end_year = "08/24/2023"
    appointments = calendar.Restrict("[Start] >= '" + begin_year + "' AND [Start] <= '" + end_year + "'")

    #start = datetime.combine(date_of_session, datetime.min.time())
    #end = datetime.combine(date_of_session, datetime.max.time())
    #filter_str = "[Start] >= '{}' AND [Start] <= '{}' AND [MeetingStatus] = 1".format(start, end)
    #appointments = calendar.Restrict(filter_str)

    # Loop through each appointment item in the calendar and check its subject
    for appointment in appointments:
        if 'Blocker' in appointment.Subject:
            print(appointment.Start, appointment.Subject)
            #to = appointment.To
            #speaker_name = to.split(".")[0].capitalize()
            appointment.Body = body
            appointment.Save()
            appointment.Display(True)
            print(appointment.body)

#dates ="2023-08-23"
#date_object = datetime.strptime(dates, "%Y-%m-%d")
#UpdateBlockerBody(dates)
