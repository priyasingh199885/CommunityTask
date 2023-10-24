import eel
import win32com.client
import datetime
import pandas as pd

# Create Outlook object and get Namespace
Outlook = win32com.client.Dispatch("Outlook.Application")
namespace = Outlook.GetNamespace("MAPI")

# Connect to Calendar
calendar = namespace.GetDefaultFolder(9)

appointments = calendar.Items
appointments.Sort("[Start]")


# Restrict to items from tomorrow onwards (gets around issue with recurring appointments)
begin = datetime.date.today() + datetime.timedelta(days=1)
appointments = appointments.Restrict("[Start] >= '" + begin.strftime("%m/%d/%Y") + "'")

data = []

# Iterate through appointments and print details
for appointment in appointments:
    if 'blocker for ecosystem' in appointment.Subject.lower():
        data.append({
            'Subject': appointment.Subject,
            'Start': appointment.Start,
            'Duration': appointment.Duration,
            'Attendees': '; '.join([r.Name for r in appointment.Recipients]),
            'Reminder': 'No' if appointment.ReminderSet else 'No'
        })
# Convert to DataFrame
print(f'{data}')
#df = pd.DataFrame(data, columns=["Subject", "Start", "Duration", "Attendees", "Reminder"])
data.append({
    'Subject': 'Test',
    'Start': '2022-03-26 10:00:00',
    'Duration': 60,
    'Attendees': 'John Doe; Jane Doe',
    'Reminder': 'Yes'
})

df = pd.DataFrame(data, columns=["Subject", "Start", "Duration", "Attendees", "Reminder"])
df['Reminder'] = df['Reminder'].apply(lambda x: f'<a href="#" onclick="change_reminder(\'{x}\'); return false;">{x}</a>' if x == 'No' else 'Yes')
print(df)

# Create or overwrite the html file
with open('my_file.html', 'w') as file:
    file.write(df.to_html(escape=False, index=False))
print("Process completed")

script=""" <script type="text/javascript" src="/eel.js"></script>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script type="text/javascript">
        async function getData() {
            let data = await eel.get_data()();
            document.getElementById("content").innerHTML = data;

            // Adding click event to "No" links
            $('.no-link').click(function(event){
                event.preventDefault();  // Prevent the default action
                let index = $(this).attr('data-index');  // Get the index from data-index attribute
                eel.trigger_python(index);  // call the Python function
            });
        }

        document.onload = getData();
    </script>
    """
#write script
# read the file
with open("my_file.html", "r") as file:
    data = file.read()

# append the script to the end of the file
data += script

# write the file again
with open("output.html", "w") as file:
    file.write(data)





