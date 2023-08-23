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
    try:
        if not valid_email(to):
            raise ValueError("Invalid email address.")

        if not subject:
            raise ValueError("Subject is missing.")

        if not body1+body2:
            raise ValueError("Body is missing.")
        markdown_body = body1
        html_body = markdown2.markdown(markdown_body)
        print(html_body)
        # If no exceptions were raised, we assume that email draft is created successfully.
        mail = Outlook.CreateItem(0)
        mail.Subject = subject
        mail.HTMLBody = html_body + "---\n" + body2 + "---"
        mail.To = to
        mail.CC = cc
        mail.BCC = bcc
        mail.Display(True)
        print("Email draft created successfully.")

    except ValueError as ve:
        print("Failed to create email draft:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)
