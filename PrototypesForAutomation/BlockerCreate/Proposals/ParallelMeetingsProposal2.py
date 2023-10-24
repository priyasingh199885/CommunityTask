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

begin = datetime.now()
end = begin + timedelta(days=5*30)

appointments = appointments.Restrict("[Start] >= '" + begin.strftime("%m/%d/%Y") + "' AND [END] <= '" +end.strftime("%m/%d/%Y") + "'")

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

def create_timeslots():
    days = ['Tuesday', 'Wednesday', 'Thursday']
    slots = ['10am-11am', '3pm-4pm','4pm-5pm']
    return [f'{day} {slot}' for day in days for slot in slots]
def create_empty_timeslots():
    days = []
    slots = []
    return [f'{day} {slot}' for day in days for slot in slots]

#initialize all weeks with 0 blocker meetings and all possible slots
for month in pd.date_range(begin, end, freq='M'):
    for week in range(1,6): # since there can be max 5 weeks in a month
        weekly_counts[f'{week} week of {month.strftime("%B %Y")}'] = {'Count':0, 'Slots': create_timeslots()}
        copy_weekly_counts[f'{week} week of {month.strftime("%B %Y")}'] = {'Count':0, 'Slots': create_empty_timeslots()}

overlapping_meetings =[]
# Process appointments
for appointment in appointments:
    week_str = str(week_of_month(appointment.Start)) + ' week of ' + appointment.Start.strftime('%B %Y')
    if week_str in weekly_counts:
        weekly_counts[week_str]['Count'] += 1
        # Verifying overlap
        for slot in weekly_counts[week_str]['Slots']:
            day, time_slot = slot.split(' ')
            slot_start, slot_end = map(lambda x: datetime.strptime(x, '%I%p'), time_slot.split('-'))
            if not (appointment.Start.time() > slot_end.time() or
                    appointment.End.time() < slot_start.time()):
                if appointment.Start.strftime('%A') == day:
                    if not 'blocker for ecosystem' in appointment.Subject.lower():
                        copy_weekly_counts[week_str] = {'Count':weekly_counts[week_str]['Count'], 'Slots': slot}
                    if 'blocker for ecosystem' in appointment.Subject.lower():
                        weekly_counts[week_str]['Slots'].remove(slot)
                    break


print(copy_weekly_counts)
overlapping_slots = []
# Prepare the data for DataFrame
data = []
for week, details in weekly_counts.items():
    slots = ', '.join(details['Slots']) if details['Count'] < 2 else 'NA'
    data.append([week, details['Count'], slots])

"""
# Convert slots to URLs
for row in data:
    if row[2] != 'NA':
        slots = row[2].split(", ")
        slots = ["<a href='http://localhost:5000/executeFunction?slot="+slot+"'>"+slot+"</a>" for slot in slots]
        row[2] = ', '.join(slots)
"""


# Change overlapping slots to red
for row in data:
    if row[2] != 'NA':
        slots = row[2].split(", ")
        slots = ["<a href='http://localhost:5000/executeFunction?slot="+slot+"'>"+slot+"</a>" if slot not in overlapping_slots else "<a href='http://localhost:5000/executeFunction?slot="+slot+"' style='color:red'>"+slot+"</a>" for slot in slots]
        row[2] = ', '.join(slots)
# Convert to DataFrame
df = pd.DataFrame(data, columns=["Week", "Count of 'Blocker' Meetings", "Available Slots"])

# Output DataFrame to HTML file
with open('../output.html', 'w') as file:
    file.write(df.to_html(escape=False, index=False).replace('<td>','<td style="color: red;">' if row[2] != 'NA' and row[2] in overlapping_meetings else '<td>', 1))
    #file.write(df.to_html(escape=False, index=False))
