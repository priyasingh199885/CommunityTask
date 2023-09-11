import datetime

import markdown2
import win32com.client


def create_appointment(subject, body1,body2, to, cc, bcc):
    Outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = Outlook.GetNamespace("MAPI")
    subject = "Meeting with Alice",
    start_time = datetime.datetime.now() + datetime.timedelta(days=1, hours=9),
    duration = 60,
    location = "Online",
    #body = "Hello Alice,\nWe'll discuss the project status."
    try:
        if not subject:
            raise ValueError("Subject is missing.")

        if not start_time:
            raise ValueError("Start time is missing.")

        if not duration:
            raise ValueError("Duration is missing.")

        if not location:
            raise ValueError("Location is missing.")

        if not body1:
            raise ValueError("Body is missing.")
        markdown_body = body1
        html_body = markdown2.markdown(markdown_body)
        print(html_body)
        # If no exceptions were raised, we assume that the appointment is created successfully.
        appointment = Outlook.CreateItem(1)
        appointment.Subject = subject
        appointment.Start = start_time
        appointment.Duration = duration
        appointment.Location = location
        #appointment.Body = html_body + "---\n" + body2 + "\n---"
        #appointment.Save()
        print("Appointment created successfully.")

    except ValueError as ve:
        print("Failed to create appointment:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)


create_appointment("subject", """<p>There are several books, which cover the topic in detail, explain the reasoning and apply it to specific programming languages.- <a href="https://www.rheinwerk-verlag.de/clean-abap-a-style-guide-for-developers/">Clean ABAP</a>
- <a href="https://www.rheinwerk-verlag.de/clean-abap-lesbarer-und-wartbarer-abap-code/">Clean ABAP - German Version</a>
- <a href="https://www.sap-press.com/clean-sapui5_5479/">Clean SAPUI5</a></p>""","""Date of Session: 2023-07-30
Date of Evaluation: 2022-01-01
Development Phase: Code
Adoption Readiness: Early Adopter
Scopes: CAP Java, CAP node.js, Java
Cluster: Test Automation, DevOps, Developer Experience
External Speaker: No
Invitiation-sent: false""", "", "", "")