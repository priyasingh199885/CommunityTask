from flask import Flask
import eel
import threading

import win32com.client

app = Flask(__name__)

# Initialize Eel
eel.init('')  # 'web' is the folder where your web files (html, js, css, etc.) are located

def start_eel():
    eel.start('index.html', size=(700, 700))  # 'index.html' is one of the files inside 'web' folder
# Custom eel status tracker
eel_status = {"started": False}



@eel.expose
def create_draft_invitations(slot, week):
    print('helo')
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.Subject = 'new mail'
    mail.HTMLBody = 'Hi Colleagues'
    mail.To = 'priya.singh@sap.com'
    mail.Save()
    mail.Display(True)
    return 'done'

@app.route('/start_eel', methods=['GET'])
def start_eel_from_flask():
    if not eel_status["started"]:  # check if Eel was already started
        eel_thread = threading.Thread(target=start_eel, daemon=True)
        #eel_thread.start()
    return eel_thread.start()

if __name__ == "__main__":
    app.run(port=5000)