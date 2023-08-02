import win32com.client

Outlook = win32com.client.Dispatch("Outlook.Application")
namespace = Outlook.GetNamespace("MAPI")


def create_draft(subject, body, to, cc, bcc):
    mail = Outlook.CreateItem(0)
    mail.Subject = subject
    mail.Body = body
    mail.To = to
    mail.CC = cc
    mail.BCC = bcc
    mail.Display(True)