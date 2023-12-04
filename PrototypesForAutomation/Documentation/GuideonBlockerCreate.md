# Blocker Create: Guide
The purpose of this file is to help create blockers for future sessions.

## Steps
1. Run BlockerCreate/WeekOfYears.py 
   Please keep Outlook session open in background.This file will update all available slots from your calendar for this year.
2. Generates BlockerCreate/output.html file 
   This file contains all the available slots in a html table format.
3. Now, run BlockerCreate/EelServer.py
   This will open a browser. Go to this browser and select the slots suitable.
4. Automatically, a dialog box will open in Outlook. It will be the Blocker.
5. Update: Speaker's name in Required Attendees. Add some colleagues to CC if necessary.
6. Submit and close.
7. Continue to send more blocker meetings or exit the code.
   
## Things to Remember
1. If you don't use this tool to create blockers, then it is fine. But the next time you want to use this then please follow the steps from start.
2. Output.html is a static page that saves everytime WeekOfMonth.py is executed.
3. Links that appear in RED are parallel meetings which are non-blocker(meetings occurring in that slot that is not from ecosystem)
4. Dialog box is opened in Outlook, go to the application menu in taskbar to see them.
5. Please check the details for generated blocker meeting before pressing send.

## Improvement & Suggestions
1. Currently, when you click on a slot to generate blocker, the clicked slot is not removed from available slot list. Because of this it is necessary to run the WeekOfMonth.py file everytime you want to send blocker using this tool.
2. When to run WeekOfMonth.pf file
   1. If new blockers added in calendar
   2. Manually created blocker without using this toll
   3. Basically, you need to run this file everytime you want to create blocker. 
