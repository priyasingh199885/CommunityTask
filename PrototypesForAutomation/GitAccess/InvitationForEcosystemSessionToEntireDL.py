import base64

import requests
import json
import yaml
import datetime
import win32com.client as win32
import CreateDraft
import os
import AccessToken

outlook = win32.Dispatch("Outlook.Application")

#replace url with ecosystem community url
url = "https://github.tools.sap/api/v3/repos/I585524/CommunityAutomation/contents/PrototypesForAutomation/Abstract"
#url = "https://github.tools.sap/api/v3/reposCloudNativeCulture/CommunityAutomation/tree/main/PrototypesForAutomation/ExampleAbstractsFromEcosystem
#replace put_url
put_url="https://github.tools.sap/api/v3/repos/I585524/CommunityAutomation/contents"
#token = os.environ.get('SECRET_TOKEN')
token = "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"
dl = "DL_5B7147227BCF84E8BE00000F@global.corp.sap"

headers = {"Authorization": f'Bearer {token}',
           "Accept": "application/vnd.github+json"}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    # Process the response
    files = json.loads(response.text)
    print(len(files))
    for file in files:
        if file['name'].endswith('.md'):
            print(f"Accessing file: {file['name']}")
            file_content = requests.get(file['download_url'], headers=headers)
            print(file_content)
            raw_content = file_content.text.split("---")

            # Check if there's potential embedded YAML (split length more than 1)
            if len(raw_content) > 1:
                try:
                    yaml_content = yaml.safe_load(raw_content[1])  # Attempt to load the YAML block
                    if 'Date of Session' in yaml_content:
                        today = datetime.datetime.today().date()
                        print(today - yaml_content['Date of Session'])
                        print(f'invitation sent out already?', yaml_content["Invitation-sent"])
                        if 14 >= (today - yaml_content['Date of Session']).days > 0 and yaml_content['Invitation-sent'] == False:
                            user_input = input(f"do you want to send invitations for {file['name']}? press y for yes / n for no")
                            if user_input == "y":
                                file_url=url + file['name']
                                file_abstract = requests.get(file_url, headers=headers).text
                                yaml_content['Invitation-sent'] = True
                                updated_yaml_block = yaml.dump(yaml_content)
                                updated_content = raw_content[0] + "---" + updated_yaml_block + "---" + raw_content[2]
                                updated_content_encoded = base64.b64encode(updated_content.encode('utf-8')).decode(
                                    'utf-8')
                                put_data = {
                                    'message': 'Update YAML block',
                                    'content': updated_content_encoded,
                                    'sha': file['sha']
                                }
                                put_url = f"{put_url}/{file['path']}"
                                put_response = requests.put(put_url, headers=headers, data=json.dumps(put_data))
                                if put_response.status_code == requests.codes.ok:
                                    print('File updated successfully!')
                                else:
                                    print(f"File update failed. Response: {put_response.content}")
                                try:
                                   CreateDraft.create_draft('Subject',file_content.text,dl, 'cc@example.com', 'bcc@example.com')
                                except Exception as e:
                                    print(e)


                except yaml.YAMLError as e:
                    print(f"Error in YAML in file {file['name']}: {e}")

else:
    # Handle error cases
    print("Error accessing the document:", response.status_code)
