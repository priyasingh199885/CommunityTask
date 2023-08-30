import dateutil.parser
from datetime import datetime, time, timedelta
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

# Assume existing_appointments hold appointment data

for month in pd.date_range(begin, end, freq='M'):
    for week in range(1,6): # since there can be max 5 weeks in a month
        weekly_counts[f'{week} week of {month.strftime("%B %Y")}'] = {'Count':0, 'Slots': create_timeslots()}
overlapping_meetings =[]
# Process appointments
for appointment in appointments:
    if 'blocker for ecosystem' in appointment.Subject.lower():
        week_str = str(week_of_month(appointment.Start)) + ' week of ' + appointment.Start.strftime('%B %Y')
        if week_str in weekly_counts:
            weekly_counts[week_str]['Count'] += 1
            # Verifying overlap
            for slot in weekly_counts[week_str]['Slots']:
                day, time_slot = slot.split(' ')
                slot_start, slot_end = map(lambda x:datetime.strptime(x, '%I%p'), time_slot.split('-'))
                if not (appointment.Start.time() > slot_end.time() or
                        appointment.End.time() < slot_start.time()):
                    if appointment.Start.strftime('%A') == day:
                        weekly_counts[week_str]['Slots'].remove(slot)
                        break
print(weekly_counts)
overlapping_slots =[]
for week_str, slot_data in weekly_counts.items():
    week_num = int(week_str.split(' ')[0]) - 1  # extract the week number and subtract 1 for 0-indexed
    month_str = ' '.join(week_str.split(' ')[-3:])  # Str like "August 2023"
    month = dateutil.parser.parse(f'1 {month_str}')  # Convert to date object
    for slot_str in slot_data['Slots']:
        day, times = slot_str.split(' ')  # Split the day and times
        start_time_str, end_time_str = times.split('-')  # Split start and end times
        start_time = datetime.strptime(start_time_str, "%I%p").time()
        end_time = datetime.strptime(end_time_str, "%I%p").time()

        # Find out the date for the specific day in the first week of the month
        if day == 'Monday':
            day_date = month + timedelta(days=0 - month.weekday(), weeks=week_num)
        elif day == 'Tuesday':
            day_date = month + timedelta(days=1 - month.weekday(), weeks=week_num)
        elif day == 'Wednesday':
            day_date = month + timedelta(days=2 - month.weekday(), weeks=week_num)
        elif day == 'Thursday':
            day_date = month + timedelta(days=3 - month.weekday(), weeks=week_num)
        elif day == 'Friday':
            day_date = month + timedelta(days=4 - month.weekday(), weeks=week_num)
        elif day == 'Saturday':
            day_date = month + timedelta(days=5 - month.weekday(), weeks=week_num)
        else:  # Sunday
            day_date = month + timedelta(days=6 - month.weekday(), weeks=week_num)

        # Combine day_date with start_time and end_time
        start_datetime = datetime.combine(day_date, start_time)
        end_datetime = datetime.combine(day_date, end_time)

        # Check if any existing appointment overlaps with the current slot
        if str(start_datetime) in all_appointments:
            for appointment in all_appointments.get(str(start_datetime), []):
                appt_start = datetime.strptime(appointment['Start'], "%Y-%m-%d %H:%M:%S")
                appt_end = datetime.strptime(appointment['End'], "%Y-%m-%d %H:%M:%S")
                # Check if slot time overlap with appointment time
                print("hi")
                if max(start_datetime, appt_start) < min(end_datetime, appt_end):
                    print("There is a parallel meeting at this time slot.")


# Prepare the data for DataFrame
data = []
for week, details in weekly_counts.items():
    slots = ', '.join(details['Slots']) if details['Count'] < 2 else 'NA'
    data.append([week, details['Count'], slots])
# Change overlapping slots to red
for row in data:
    if row[2] != 'NA':
        slots = row[2].split(", ")
        slots = ["<a href='http://localhost:5000/executeFunction?slot="+slot+"'>"+slot+"</a>" if slot not in overlapping_slots else "<a href='http://localhost:5000/executeFunction?slot="+slot+"' style='color:red'>"+slot+"</a>" for slot in slots]
        row[2] = ', '.join(slots)
# Convert to DataFrame
df = pd.DataFrame(data, columns=["Week", "Count of 'Blocker' Meetings", "Available Slots"])

# Output DataFrame to HTML file
with open('output.html', 'w') as file:
    file.write(df.to_html(escape=False, index=False).replace('<td>','<td style="color: red;">' if row[2] != 'NA' and row[2] in overlapping_meetings else '<td>', 1))
    #file.write(df.to_html(escape=False, index=False))
