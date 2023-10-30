import os
import re
from datetime import datetime, timedelta
import win32com.client as win32

internal_template = os.path.join(os.getcwd(), 'Template_Internal.oft')
external_template = os.path.join(os.getcwd(), 'Template_External.oft')
outlook = win32.Dispatch("Outlook.Application")

def create_outlook_draft(to,date,title,type):
    if type == "Internal":
        print("This is an internal speaker")
        mail = outlook.CreateItemFromTemplate(internal_template)
    else:
        mail = outlook.CreateItemFromTemplate(external_template)
    mail.HTMLBody = mail.HTMLBody.replace("Speaker_name", split_string(to))
    mail.HTMLBody = mail.HTMLBody.replace("TOPIC", title)
    mail.HTMLBody = mail.HTMLBody.replace("DATE", date)
    mail.HTMLBody = mail.HTMLBody.replace("Working_Student", "Priya")
    mail.To = to
    mail.CC = "klaus.haeuptle@sap.com"
    mail.Save()
    mail.Display()


def split_string(string):
    # split by ';' and store into list
    list = string.split(';')

    # initialize a new string to store results
    new_str = ""

    # for each item in list
    for item in list:
        # split by ',' or '@' or '.' whichever comes first
        # use regular expression to do so
        import re
        new_item = re.split(',|@|\.', item, 1) # 1 means the split will happen at the first occurrence of any defined separator
        # Append only the first part of split into new_str
        new_str += new_item[0].title() + ", "  # adding a space after each name for readability

    # remove the trailing space at the end of the string
    new_str = new_str.rstrip()
    return new_str

