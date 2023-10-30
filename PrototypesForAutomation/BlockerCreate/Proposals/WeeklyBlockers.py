import win32com.client
import datetime
import pandas as pd
from IPython.display import display, HTML

Outlook = win32com.client.Dispatch("Outlook.Application")
namespace = Outlook.GetNamespace("MAPI")

appointments = namespace.GetDefaultFolder(9).Items
appointments.Sort("[Start]")
appointments.IncludeRecurrences = "True"

def displaTable(blocker_dict):
    # assuming 'blocker_dict' is your dictionary
    df = pd.DataFrame(list(blocker_dict.items()), columns=['Date and Subject', 'Count'])
    with open('../output.html', 'w') as f:
        f.write(df.to_html())
    display(HTML(df.to_html()))


def get_overlap_events(blocker_start_time, blocker_end_time, months):
    begin = datetime.date.today()
    end = datetime.date.today() + datetime.timedelta(months * 30)

    # Define the time period you want to use.
    appointments_range = appointments.Restrict(
        "[Start] >= '" + begin.strftime("%m/%d/%Y") + "' AND [END] <= '" + end.strftime("%m/%d/%Y") + "'")

    overlap_events = {}
    for appointment in appointments_range:
        if appointment.Start <= blocker_end_time and appointment.End >= blocker_start_time:
            overlap_events[appointment.Start, appointment.Subject] = True

    # Return the overlapping events.
    return overlap_events

def get_blocker_events(months):
    begin = datetime.date.today()
    end = datetime.date.today() + datetime.timedelta(months * 30)

    appointmentss = appointments.Restrict(
        "[Start] >= '" + begin.strftime("%m/%d/%Y") + "' AND [END] <= '" + end.strftime("%m/%d/%Y") + "'")

    blocker_count = 0
    blocker_dict = {}
    for appointment in appointmentss:
        if 'blocker for ecosystem' in appointment.Subject.lower():
            blocker_count += 1
            overlap_events = get_overlap_events(appointment.Start, appointment.End, months)
            # Change the color to red if the event has an overlap.
            color = 'red' if overlap_events else 'black'
            blocker_dict[appointment.Start, appointment.Subject, color] = blocker_count

    # Output: {(datetime.datetime(2019, 1, 31, 11, 0, tzinfo=<TimeZoneInfo 'UTC': UTC, UTC, 0:0:0, STD>), 'Blocker meeting'): 1}
    print(blocker_dict)
    displaTable(blocker_dict)

get_blocker_events(4)