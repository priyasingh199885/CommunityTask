## Guide on How To Invite Working Student For Blocker Meeting
Adjust the receiver variable to be your email.
This script currently adds you to all appointments with the title "Blocker for Ecosystem" starting from the current date.
You must have appropriate permissions to edit the meeting invite.
Be careful with time zones when manipulating dates and times using the datetime library.
You should close Outlook while running this script.
Test this script with a few test meetings before using it on actual meetings.
PyWin32 API has some bugs/undocumented features especially with recurring appointments.
Be aware this script sends updates to all meeting attendees if any properties are changed.