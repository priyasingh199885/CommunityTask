import base64
import json
import os
import datetime
import yaml
import GetAccessGit
import requests
import frontmatter
import CreateDraft
from GitAccess import CalendarUpdateAbstract

md_files_to_invite = []
dl = "DL_5B7147227BCF84E8BE00000F@global.corp.sap"
today = datetime.datetime.today().date()
put_url="https://github.tools.sap/api/v3/repos/I585524/CommunityAutomation/contents"
date_of_session=''

def updateAbstract(file_to_invite):
    for file in files:
        put_url = "https://github.tools.sap/api/v3/repos/I585524/CommunityAutomation/contents"
        if file['name'] == file_to_invite:
            print(f"Accessing file: {file['name']}")
            file_content = requests.get(file['download_url'], headers=GetAccessGit.headers)
            print(file_content)
            raw_content = file_content.text.split("---")
            yaml_content = yaml.safe_load(raw_content[1])
            yaml_content['Invitation-sent'] = True
            date_of_session = yaml_content['Date of Session']
            updated_yaml_block = yaml.dump(yaml_content)
            print(raw_content[0])
            print(raw_content[1])
            print(raw_content[2])
            print(raw_content[3])
            #updated_content = raw_content[0] + "---" + updated_yaml_block + "---" + raw_content[2]
            updated_content = "---\n" + updated_yaml_block + "---" + raw_content[2] + "---" + raw_content[3] + "---"
            updated_content_encoded = base64.b64encode(updated_content.encode('utf-8')).decode(
                'utf-8')
            put_data = {
                'message': 'Update YAML block',
                'content': updated_content_encoded,
                'sha': file['sha']
            }
            put_url = f"{put_url}/{file['path']}"
            put_response = requests.put(put_url, headers=GetAccessGit.headers, data=json.dumps(put_data))
            if put_response.status_code == requests.codes.ok:
                print('File updated successfully!')
                CalendarUpdateAbstract.UpdateBlockerBody(date_of_session)
            else:
                print(f"File update failed. Response: {put_response.content}")
            try:
                CreateDraft.create_draft('Subject', file_content.text, dl, 'cc@example.com', 'bcc@example.com')
            except Exception as e:
                print(e)


def selectSession(md_files_to_invite):
    file_to_invite = input("Enter the name of the markdown file you want to create a draft for:")

    if file_to_invite in md_files_to_invite:
        # generate and send email draft here.
        updateAbstract(file_to_invite)
        print(f"Generating email draft for {file_to_invite}")
    else:
        print(
            f"No draft email generated because the file {file_to_invite} either doesn't exist or 'Invitation-sent' is not 'false' or Session has already occured.")


def extract_frontmatter(files):
    for file in files:
        if file['name'].endswith('.md'):
            print(f"Accessing file: {file['name']}")
            file_content_response = requests.get(file['download_url'], headers=GetAccessGit.headers)

            # Make sure the request was successful
            if file_content_response.status_code == 200:
                file_content = file_content_response.text
                raw_content = file_content.split("---")
                if len(raw_content) > 1:
                    try:
                        yaml_content = yaml.safe_load(raw_content[1])  # Attempt to load the YAML block
                        #date_of_session = yaml_content['Date of Session']
                        if yaml_content['Date of Session'] > today and yaml_content[
                            'Invitation-sent'] == False:
                            print('no invitations yet')
                            md_files_to_invite.append(file['name'])

                    except yaml.YAMLError as e:
                        print(f"Error in YAML in file {file['name']}: {e}")

                #md = frontmatter.loads(file_content)

                # Now 'md' is a dictionary with all frontmatter fields.
                # You can access any field, like 'Invitation-sent', with md.get('Invitation-sent')



                    # Your logic here if Invitation-sent is false

            else:
                print(f"Error fetching content for file: {file['name']}")
    return md_files_to_invite


# token = os.environ.get('SECRET_TOKEN')
files = GetAccessGit.files
frontmatter = extract_frontmatter(files)
selectSession(md_files_to_invite)
