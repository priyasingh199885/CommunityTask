import win32com.client
from datetime import datetime, timedelta

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
calendar = outlook.GetDefaultFolder(9) # 9 refers to the calendar folder.
receiver = "ok.ok@sap.com"  # Change this

# Get today's date and time
now = datetime.now()

# Get all the appointments
appointments = calendar.Items

# Order them from oldest to most recent
appointments.Sort("[Start]")

# Filter to only include future appointments
appointments = appointments.Restrict("[Start] >= '" +now.strftime("%m/%d/%Y") + "'")

for appointment in appointments:
    if 'Test Blocker' in appointment.Subject:
        print('Appointment Found: ', appointment.Subject)
        print('Adding You as a Recipient...')
        recipient=appointment.Recipients.Add(receiver)
        recipient.Type = 2
        #appointment.Save()
        appointment.Display()
        print('Done. Press Enter to Proceed to Next Appointment...')
        input()