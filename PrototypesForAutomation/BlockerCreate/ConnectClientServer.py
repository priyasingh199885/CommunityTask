from datetime import datetime, timedelta, time
import pythoncom
from flask import Flask, request
from BlockerCreate.CreateBlocker import create_draft_invitation
pythoncom.CoInitialize()


subject = "Blocker for Ecosystem:"
meeting_date = datetime(2023, 12, 14).date()  # for example, it's set to Dec 11, 2023
start_time = time(15, 55)  # 3:00 PM
duration = timedelta(hours=1, minutes=5)  # 1 hours meeting
attendees = []  # list of attendees emails
#attendees = input("Enter the email addresses for required attendees, separated by commas: ").split(',')
optional_attendees = ['priya.singh05@sap.com']  # list of optional (cc) attendees emails


#from CreateBlocker import  create_draft_invitation
app = Flask(__name__)

@app.route('/')
def home():
    # Serve your DataFrame as home page
    with open('C:\\Users\\I585524\\PycharmProjects\\Automation\\CommunityAutomation\\PrototypesForAutomation\\BlockerCreate\\output.html', 'r') as file:
        return file.read()



    pass


@app.route('/executeFunction')
def executeFunction():
    slot = request.args.get('slot', default = '', type = str)
    starting_time = slot.split("-")[0].split(" ")[1];
    # Your 'Createdraft' function here
    #create_draft_invitation(subject="Blocker for Ecosystem:",meeting_date=meeting_date,start_time=starting_time,duration=timedelta(hours=1, minutes=6),attendees=attendees,optional_attendees=optional_attendees,body='')
    print(f"Executing function for slot: {slot}")
    return f"Function executed for slot: {slot}"

if __name__ == '__main__':
    app.run(debug=True)


