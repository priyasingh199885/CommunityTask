import win32com.client
import datetime
import pandas as pd

Outlook = win32com.client.Dispatch("Outlook.Application")
namespace = Outlook.GetNamespace("MAPI")

appointments = namespace.GetDefaultFolder(9).Items
appointments.Sort("[Start]")
appointments.IncludeRecurrences = "True"

begin = datetime.datetime.now()
end = begin + datetime.timedelta(days=5*30)

appointments = appointments.Restrict("[Start] >= '" + begin.strftime("%m/%d/%Y") + "' AND [END] <= '" +end.strftime("%m/%d/%Y") + "'")

weekly_counts = {}


# Find week of month for a given date
def week_of_month(dt):
    first_day = dt.replace(day=1)
    dom = dt.day
    adjusted_dom = dom + first_day.weekday()
    return (adjusted_dom // 7) + 1

#initialize all weeks with 0 blocker meetings
for month in pd.date_range(begin, end, freq='M'):
    for week in range(1,6): # Since there can be max 5 weeks in a month
        weekly_counts[f'{week} week of {month.strftime("%B %Y")}'] = 0

# Process appointments
for appointment in appointments:
    if 'blocker for ecosystem' in appointment.Subject.lower():
        week_str = str(week_of_month(appointment.Start)) + ' week of ' + appointment.Start.strftime('%B %Y')
        if week_str in weekly_counts:
            weekly_counts[week_str] += 1

# Convert dict to DataFrame for neat output
df = pd.DataFrame(list(weekly_counts.items()), columns=["Week", "Count of 'Blocker' Meetings"])

# Output DataFrame to HTML file
with open('../output.html', 'w') as file:
    file.write(df.to_html(index=False))