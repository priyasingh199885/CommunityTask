# Github Personal Access Token
If you want to create a personal access token on GitHub, please follow these steps:

Sign in to GitHub.
Click on your profile photo in the upper-right corner of any page, then click on Settings in the drop-down menu.
In the left sidebar, click on Developer settings.
In the left sidebar, click on Personal access tokens.
Click the "Generate new token" button.
Give your token a descriptive name in the "Note" field.
Choose the scopes, or permissions, you'd like to grant this token. (To use your token to access repositories from the command line, select repo.)
Token Scopes
Click "Generate token", and you're done.


Make sure to copy your new personal access token now. You won't be able to see it again!
CAUTION: Treat your tokens like passwords and keep them secret. When working with the API, use tokens as environment variables instead of hardcoding them into your programs.


More details from the official GitHub documentation [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
Remember to treat your tokens with care, avoid sharing them and always store them securely. If accidentally exposed, they should be immediately revoked to prevent unauthorized access to your GitHub account.


## Dialog Box Feature
The `mail.Display(True)` method in the `create_draft()` function displays the Outlook email window as an interactive modal window. It means that when this window is open, users cannot interact with the other windows in the application until they close the email window. This behavior is a specific feature of the Outlook's mail object and the `Display` method, which is run by the Windows function `ShowDialog()`. This function suspends the code execution in the parent window and gives the control to the modal window (email window, in this case). 

You generally see this behavior with dialog boxes that require a user action before continuing with other tasks, such as accepting a software license agreement, responding to a data-loss warning, or specifying options in a settings dialog box, etc. 

If you don't want to display the message immediately while creating the draft you can use `mail.Display(False)`. But this will create and save the draft email without displaying it to you. But please note that it will still save the email in the "Draft" folder in your Outlook. 

There is no way to make the new mail item window non-modal via the Outlook Object Model (OOM) as the `Display` method invariably shows the mail item as a modal window. If you want to show the new mail item as a non-modal window, you'll have to use Extended MAPI (which is only C++ or Delphi) or a third-party wrapper like Redemption (which works in any language that can make COM Automation calls). 

So when automating Outlook, ensure that there are no other dialog boxes open because they might interfere with your automation script as it's not possible to interact with other dialog boxes when a modal dialog is open. If this creates a hurdle for your task, you might need to reconsider your workflow or use another email client that allows non-modal email draft windows.