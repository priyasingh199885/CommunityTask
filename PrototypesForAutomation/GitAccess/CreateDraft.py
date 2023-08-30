import datetime

import win32com.client
import re
import markdown2

Outlook = win32com.client.Dispatch("Outlook.Application")
namespace = Outlook.GetNamespace("MAPI")


def valid_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False
def create_draft(subject, body1,body2, to, cc, bcc):
    start_time = datetime.datetime.now() + datetime.timedelta(days=1, hours=9),
    duration = 60,
    location = "Online",
    try:
        if not valid_email(to):
            raise ValueError("Invalid email address.")

        if not subject:
            raise ValueError("Subject is missing.")

        if not body1+body2:
            raise ValueError("Body is missing.")
        markdown_body = body1
        markdown_body1 =body2
        html_body = markdown2.markdown(markdown_body)
        html_body1 = markdown2.markdown(markdown_body1)
        print(html_body)
        # If no exceptions were raised, we assume that email draft is created successfully.
        mail = Outlook.CreateItem(0)
        mail.Subject = subject
        mail.HTMLBody = html_body + "---\n" + html_body1 + "\n---"
        mail.To = to
        mail.CC = cc
        mail.BCC = bcc
        mail.Save()
        mail.Display(True)
        #mail.Start = start_time
        #mail.Duration = duration
        #mail.Location = location
        print("Email draft created successfully.")

    except ValueError as ve:
        print("Failed to create email draft:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)
