import calendar

import win32com.client
import datetime
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta, MO

Outlook = win32com.client.Dispatch("Outlook.Application")
namespace = Outlook.GetNamespace("MAPI")

appointments = namespace.GetDefaultFolder(9).Items
appointments.Sort("[Start]")
appointments.IncludeRecurrences = "True"
#today
today = datetime.now()
current_month = today.strftime('%B')
print(current_month)
#begin = datetime.now()
begin = datetime.strptime('2023-01-01', '%Y-%m-%d')
print(begin)
end = begin + timedelta(days=12*30)
#display only slots from current_month
display=False

appointments = appointments.Restrict("[Start] >= '" + begin.strftime("%d/%m/%Y") + "' AND [END] <= '" +end.strftime("%d/%m/%Y") + "'")
overlapping_slots = []
weekly_counts = {}
copy_weekly_counts={}
# Collect all appointments timings and subjects
all_appointments = []
for appointment in namespace.GetDefaultFolder(9).Items:
    all_appointments.append((appointment.Start, appointment.End, appointment.Subject))

# Find week of month for a given date
def week_of_month(dt):
    first_day = dt.replace(day=1)
    dom = dt.day
    adjusted_dom = dom + first_day.weekday()
    return (adjusted_dom // 7) + 1
"""def get_week_days(week_days):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    week_days = [day for day in days if day in week_days]
    return week_days"""

def create_timeslots():
    days = ['Tuesday', 'Wednesday', 'Thursday']
    slots = ['10am-11am', '3pm-4pm','4pm-5pm']
    return [f'{day} {slot}' for day in days for slot in slots]

def create_empty_timeslots():
    days = []
    slots = []
    return [f'{day} {slot}' for day in days for slot in slots]

#initialize all weeks with 0 blocker meetings and all possible slots
"""for month in pd.date_range(begin, end, freq='M'):
    for week in range(1,7): # since there can be max 5 weeks in a month
        # Calculate the first and last day of the month
        first_day = datetime(month.year, month.month, 1)
        last_day = first_day + timedelta(days=calendar.monthrange(month.year, month.month)[1] - 1)

        # Create a list of all days in the month
        all_days = [first_day + timedelta(days=i) for i in range((last_day - first_day).days + 1)]

        # Chunk the days into weeks
        weeks = [all_days[i:i + 7] for i in range(0, len(all_days), 7)]

        for week_idx, week in enumerate(weeks, start=1):
            week_days = list(map(lambda date: date.strftime("%A"), week))
            week_days = get_week_days(week_days)
            week_str = f'{week_idx} week of {month.strftime("%B %Y")} starting {week[0].strftime("%d %B %Y")}'
            weekly_counts[week_str] = {'Count': 0,
                                                                              'Slots': create_timeslots(week_days)}
            copy_weekly_counts[week_str] = {'Count':0, 'Slots': create_empty_timeslots()}
            """

overlapping_meetings =[]

# Create a list of all Mondays in the range
mondays = pd.date_range(begin, end, freq='W-MON')

# Initialize all weeks with 0 blocker meetings and all possible slots
weekly_counts = {}

for idx, monday in enumerate(mondays, start=1):
    weekly_counts[f'Week {idx} of {monday.strftime("%B %Y")}'] = {'Count':0, 'Slots': create_timeslots()}
    copy_weekly_counts[f'Week {idx} of {monday.strftime("%B %Y")}'] = {'Count': 0, 'Slots': create_empty_timeslots()}

# Process appointments
for appointment in appointments:
    week_str = None

    # Find the corresponding week for this appointment
    for monday in reversed(mondays):
        if appointment.Start.date() >= monday.date():
            week_str = f'Week {list(mondays).index(monday) + 1} of {monday.strftime("%B %Y")}'
            break
    if week_str is not None:
        if 'blocker for ecosystem' in appointment.Subject.lower():
            weekly_counts[week_str]['Count'] += 1
            # Verifying overlap
            for slot in weekly_counts[week_str]['Slots']:
                #print(slot + appointment.Subject, appointment.Start)
                day, time_slot = slot.split(' ')
                slot_start, slot_end = map(lambda x: datetime.strptime(x, '%I%p'), time_slot.split('-'))
                if not (appointment.Start.time() >= slot_end.time() or
                        appointment.End.time() <= slot_start.time()):
                    if appointment.Start.strftime('%A') == day:
                        weekly_counts[week_str]['Slots'].remove(slot)
                        # break

        else:
            #week_str = str(week_of_month(appointment.Start)) + ' week of ' + appointment.Start.strftime('%B %Y')
            """if week_str in weekly_counts:
                # weekly_counts[week_str]['Count'] += 1
                # Verifying overlap"""
            for slot in weekly_counts[week_str]['Slots']:
                day, time_slot = slot.split(' ')
                slot_start, slot_end = map(lambda x: datetime.strptime(x, '%I%p'), time_slot.split('-'))
                if not (appointment.Start.time() >= slot_end.time() or
                        appointment.End.time() <= slot_start.time()):
                    if appointment.Start.strftime('%A') == day:
                        # overlapping_slots.append(slot)
                        copy_weekly_counts[week_str]['Slots'].append(slot)
                        # break



print(weekly_counts)
print(copy_weekly_counts)

# Prepare the data for DataFrame
data = []
for week, details in weekly_counts.items():
    print(week)
    second_word = week.split(" ")[1]
    third_word = week.split(" ")[3]
    print(second_word)
    if(display!=True and third_word.lower()==current_month.lower()):
        display=True
    slots = ', '.join(details['Slots']) if details['Count'] < 2 else 'NA'
    if display== True:
        data.append([week, details['Count'], slots])

"""
# Convert slots to URLs
for row in data:
    if row[2] != 'NA':
        slots = row[2].split(", ")
        slots = ["<a href='http://localhost:5000/executeFunction?slot="+slot+"'>"+slot+"</a>" for slot in slots]
        row[2] = ', '.join(slots)
"""

print(data)
# Change overlapping slots to red
for row in data:
    if row[2] != 'NA':
        slots = row[2].split(", ")
        week_str = row[0]
        #slots = ["<a href='http://localhost:5000/executeFunction?slot="+slot+"'>"+slot+"</a>" if slot not in overlapping_slots else "<a href='http://localhost:5000/executeFunction?slot="+slot+"' style='color:red'>"+slot+"</a>" for slot in slots]
        #slots = [f"<a href='http://localhost:5000/executeFunction?slot={slot}' onclick='callPythonFunc(\"{slot}\")' style='color:red'>{slot}</a>" if row[0] in copy_weekly_counts and slot in copy_weekly_counts[row[0]]['Slots'] else f"<a href='http://localhost:5000/executeFunction?slot={slot}' onclick='callPythonFunc(\"{slot}\")'>{slot}</a>"
        slots = [f"<a href='#' onclick='callPythonFunc(\"{slot}\", \"{week_str}\")' style='color:red'>{slot}</a>" if row[0] in copy_weekly_counts and slot in copy_weekly_counts[row[0]]['Slots'] else f"<a href='#' onclick='callPythonFunc(\"{slot}\", \"{week_str}\")'>{slot}</a>"
            for slot in slots]
        row[2] = ', '.join(slots)
# Convert to DataFrame
df = pd.DataFrame(data, columns=["Week", "Count of 'Blocker' Meetings", "Available Slots"])

#df = pd.DataFrame(data, columns=["Subject", "Start", "Duration", "Attendees", "Reminder"])
# Output DataFrame to HTML file
with open('output.html', 'w') as file:
    file.write(df.to_html(escape=False, index=False).replace('<td>','<td style="color: red;">' if row[2] != 'NA' and row[2] in overlapping_meetings else '<td>', 1))
    #file.write(df.to_html(escape=False, index=False))


#write script
# read the file
with open("output.html", "r") as file:
    data = file.read()

# specify the script
script = """
<script type="text/javascript" src="/eel.js"></script>
<script type="text/javascript">
    function callPythonFunc(slot,week   ) {
        eel.create_draft_invitations(slot,week)((response) => console.log(response));
    }
</script>
"""

# append the script to the end of the file
data += script

# write the file again
with open("output.html", "w") as file:
    file.write(data)