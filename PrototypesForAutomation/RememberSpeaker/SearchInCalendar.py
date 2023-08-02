import win32com.client as win32
from datetime import datetime, timedelta

def get_calendar_meetings(date_to_search, keyword):
    outlook = win32.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    calendar = namespace.GetDefaultFolder(9)  # 9 represents the Calendar folder
    print(calendar.Name)

    cal = namespace.Folders("priya.singh05@sap.com").Folders("Calendar")
    print(cal.Name)

    # Get the start and end times for the specified date
    start = datetime.combine(date_to_search, datetime.min.time())
    end = datetime.combine(date_to_search, datetime.max.time())
    print(end)

    # Set the filter to retrieve meetings within the specified date range
    filter_str = "[Start] >= '{}' AND [Start] <= '{}' AND [MeetingStatus] = 1".format(start,end)

    # Retrieve the filtered appointments/meetings in the calendar
    appointments = calendar.Items.Restrict(filter_str)
    appointments.IncludeRecurrences = True

    for appointment in appointments:
        if appointment.MeetingStatus == 0:
            print("Subject:", appointment.Subject)
            print("Start Time:", appointment.Start)
            print("End Time:", appointment.End)
            print("Location:", appointment.Location)
            print("Organizer:", appointment.Organizer)
            print("-----------------------")
        elif appointment.MeetingStatus == 1:
            print("Subject:", appointment.Subject)
            print("Start Time:", appointment.Start)
            print("End Time:", appointment.End)
            print("Location:", appointment.Location)
            print("Organizer:", appointment.Organizer)
            print("-----------------------")


# Usage example
date_to_search_str = input("Enter the date to search (YYYY-MM-DD): ")
date_to_search = datetime.strptime(date_to_search_str, "%Y-%m-%d").date()

keyword = input("Enter the keyword to search in the subject: ")

get_calendar_meetings(date_to_search, keyword)

#if appointment.MeetingStatus == 1:  # 1 represents a meeting request/appointment
        #if keyword in appointment.Subject: