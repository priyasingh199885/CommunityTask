import eel
import datetime
import pandas as pd
import win32com.client
import os

# Initiate eel with the 'web' directory
eel.init('web')

# Load persisted data if exists otherwise create an empty DataFrame
if os.path.isfile('persisted_data.csv'):
    all_data = pd.read_csv('persisted_data.csv')
else:
    all_data = pd.DataFrame(columns=["Subject", "Start", "Duration", "Attendees", "Reminder"])

# The same code you're using to pull data from Outlook
Outlook = win32com.client.Dispatch("Outlook.Application")
namespace = Outlook.GetNamespace("MAPI")
calendar = namespace.GetDefaultFolder(9)
appointments = calendar.Items
appointments.Sort("[Start]")

# Fetch details from the appointments
begin = datetime.date.today() + datetime.timedelta(days=1)
appointments = appointments.Restrict("[Start] >= '" + begin.strftime("%m/%d/%Y") + "'")
data = []
for appointment in appointments:
    if 'blocker for ecosystem' in appointment.Subject.lower():
        # First convert start to string as DataFrame does not support datetime
        start = appointment.Start.Format("%Y-%m-%d %H:%M:%S")

        # If the appointment (with the same Start time) already exists, fetch its reminder status, otherwise set it to No
        reminder = all_data.loc[all_data.Start == start, 'Reminder'].values[
            0] if start in all_data.Start.values else 'No'

        data.append({
            'Subject': appointment.Subject,
            'Start': start,
            'Duration': appointment.Duration,
            'Attendees': '; '.join([r.Name for r in appointment.Recipients]),
            'Reminder': reminder
        })
eel.init('')
# Update persisted DataFrame and write to CSV
all_data = pd.DataFrame(data)
all_data.to_csv('persisted_data.csv', index=False)


@eel.expose
def get_data():
    df_html = all_data.to_html(escape=False, index=False)

    # Add a clickable link on "No" text with Start as a parameter
    df_html = df_html.replace('"No"', '<a href="#" class="reminder-link" data-status="No">No</a>')
    df_html = df_html.replace('"Yes"', '<a href="#" class="reminder-link" data-status="Yes">Yes</a>')

    return df_html


@eel.expose
def set_reminder(index, status):
    # Update reminder status in DataFrame
    all_data.loc[index, 'Reminder'] = 'Yes' if status == 'No' else 'No'

    # Save DataFrame to CSV for future use
    all_data.to_csv('persisted_data.csv', index=False)

    return get_data()  # Return updated table


eel.start('index.html', size=(800, 600))