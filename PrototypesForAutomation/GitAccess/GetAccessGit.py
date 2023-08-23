import frontmatter

import AccessToken
import requests
import json
token = AccessToken.secret_token
url = "https://github.tools.sap/api/v3/repos/I585524/CommunityAutomation/contents/PrototypesForAutomation/Abstract"
headers = {"Authorization": f'Bearer {token}',
           "Accept": "application/vnd.github+json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('success')
    files = json.loads(response.text)
    print(f'no of files in repository folder = {len(files)}')

else:
    print('failure to access git')