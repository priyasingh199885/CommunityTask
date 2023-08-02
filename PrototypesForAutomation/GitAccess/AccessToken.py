import os

secret_token = os.environ.get('SECRET_TOKEN')

if secret_token is None:
    print('No secret token found.')
else:
    print('Secret token is:', secret_token)


    #Readme.md on how to create token
    # set SECRET_TOKEN="my_token_value"
    # python AccessToken.py