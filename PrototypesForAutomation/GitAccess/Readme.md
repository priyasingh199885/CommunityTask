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