from llm_commons.langchain.btp_llm import init_llm, init_embedding_model

llm = init_llm('gpt-35-turbo', temperature=0., max_tokens=256)
embedding = init_embedding_model('text-embedding-ada-002-v2')


import json
import requests

KEY_FILE = "key.json" #specify the path to your key.json

# Load the service key
def load_key():
    with open(KEY_FILE, "r") as key_file:
        svc_key = json.load(key_file)

    return svc_key

# Get Token
def get_token(svc_key):
    svc_url = svc_key["url"]
    client_id = svc_key["uaa"]["clientid"]
    client_secret = svc_key["uaa"]["clientsecret"]
    uaa_url = svc_key["uaa"]["url"]

    params = {"grant_type": "client_credentials" }
    resp = requests.post(f"{uaa_url}/oauth/token",
                         auth=(client_id, client_secret),
                         params=params)

    token = resp.json()["access_token"]

    return token

def make_request(data):
    my_svc_key = load_key()
    my_token = get_token(my_svc_key)

    headers = {
        "Authorization":  f"Bearer {my_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(f'{my_svc_key["url"]}/api/v1/completions',
                             headers=headers,
                             json=data)
    return response

if __name__ == "__main__":

    # gpt-35-turbo example, prompt uses Chat Completions API format
    data = {
        "deployment_id": "gpt-35-turbo",
        "messages": [
            {"role": "system", "content": "Assistant is an intelligent chatbot designed to help users answer their tax related questions.\n\nInstructions:\n- Only answer questions related to taxes.\n- If you're unsure of an answer, you can say \"I don't know\" or \"I'm not sure\" and recommend users go to the IRS website for more information."},
            {"role": "user", "content": "When are my taxes due?"}
        ],
        "max_tokens": 100,
        "temperature": 0.0,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "stop": "null"
    }

    response = make_request(data)
    print(response.json())
