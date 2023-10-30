# Remember Speaker: Guide
This guide explains how to use the tool to Remember the speaker.

## Steps
1. Run NewRemember/db_operation.py - this creates the db and table
2. Open NewRemember/Collect.py and check if all the libraries imported are installed.
3. Run NewRemember/Collect.py, a browser opens with a table of all blocker meetings.
4. There is a column Reminder, press on 'No' if you want to remember the speaker. 
5. This opens a dialog box in outlook, check the details and send the mail.
PS: Initially, before using this code, the db needs to be updated manually from backend with values 'yes' in column 'Reminder' for which remember was already sent. This, however, only needs to be done the first time you use it.

## Things to Remember
1. A file NewRemember/'automation.db' comes in this folder, all the data on meeting is saved here. It is a sqlLite database. One can use DB BROWSER (SQLite) for backend control. 
2. Currently, only use this tool to send remember, or otherwise there will be no way for the automation.db to know if remember was sent.
3. When the outlook dialog box opens, please check the recipient list, cc, Salutation(sometimes surnames are used). Modify if necessary.
4. If you want to view all the data: execute db_display.py file.

## Improvements & Suggestions
1. Currently, the template says "Hi, I am Priya..." this is the name of the working student. Template can be modified in the future, however code will need no change.
2. If the moderator wants to do this task, then template needs to be updated without the need for any other step.
3. If outlook was used to manually send remember (in case of urgency) then find a way to still add the reminder variable value in automation.db.
