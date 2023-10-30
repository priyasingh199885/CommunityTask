import win32com.client as win32
import pandas as pd
import eel
from RememberDraft import create_outlook_draft
from db_operations import save_dataframe, update_dataframe,get_data
# Initialize Eel
eel.init('')

# Create  a new instance of outlook
outlook = win32.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")
calendar = namespace.GetDefaultFolder(9).Items

# Helper function to convert attendees list to string
def attendees_to_string(attendee_list):
    #return '; '.join(attendee_list)
    #attendees_list = attendees.split(';')
    #attendees_list = [attendee.strip() for attendee in attendee_list]  # remove leading/trailing whitespaces

    return '; '.join(attendee_list)

# Define dataframe container for messages
df_container = {
    "Subject": [],
    "Start": [],
    "Duration": [],
    "Attendees": [],
    "Reminder": [],
    "Speaker": []
}
address_list = []
# Filter messages and parse information
for appointment in calendar:
    if 'Blocker for Ecosystem' in appointment.Subject:
        #print(appointment.Subject, appointment.Duration, appointment.Start, appointment.RequiredAttendees)
        df_container["Subject"].append(appointment.Subject)
        df_container["Start"].append(appointment.Start)
        df_container["Duration"].append(appointment.Duration)
        df_container["Reminder"].append('NO')
        df_container['Attendees'].append('; '.join([r.Name for r in appointment.Recipients if r.Name not in ['Singh, Priya', 'Haeuptle, Klaus']]))
        internal_emails = []
        count=0
        #internal_emails = [x.strip() for x in appointment.RequiredAttendees.split(';') if '@' in x]
        for recipient in appointment.Recipients:
            try:
                exchange_user = recipient.AddressEntry.GetExchangeUser()
                if exchange_user is None:
                    count =count +1
                    #internal_emails.append(recipient.AddressEntry.GetExchangeUser().PrimarySmtpAddress)
            except Exception as e:
                print(f'Error: {e}')
        print("code is running...")
        if count > 0:
            df_container['Speaker'].append('External')
        else:
            df_container['Speaker'].append('Internal')
for key, values in df_container.items():
    if any(v is None for v in values):
        print(f"'None' is present in {key}")


# Compile dataframe
df = pd.DataFrame(df_container)

df['Start'] = df['Start'].dt.tz_convert(None)
print(df['Start'])
html_content = df.to_html()

# Assuming df_container is ready and populated
# store in db
save_dataframe(df_container)

# Display using eel
@eel.expose
def get_content():
    return get_data()

# Update db using eel
@eel.expose
def update_reminder(start_time):
    row =update_dataframe(start_time)
    print(row)
    if row:
        start = row[0][1].split(" ")[0]
        attendee = row[0][3]
        subject = row[0][0]
        type = row[0][5]
        subject = subject.replace('Blocker for Ecosystem:', ' ')
        create_outlook_draft(attendee,start,subject,type)
    return "updated"
# Start eel
eel.start('index.html')