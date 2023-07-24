import requests
import json
import base64

def upload_schema(schema_type,schema_file_path,schema_name):
    # Set the API endpoint URL
    API_ENDPOINT = "https://5078-samagradevelop-text2sql-wts1kqivc9t.ws-us102.gitpod.io/onboard"

    # Set the path to the schema file
    SCHEMA_FILE = schema_file_path

    # Set the schema type and name
    SCHEMA_TYPE = schema_type
    SCHEMA_NAME = schema_name

    # Set the CSRF token and credentials
    CSRF_TOKEN = "SWTHvaNeh4g3KImyRotjdDcMYuiW0dw4ctce3LXEkRWHJx71t7nKMLCk70wSdSSB"
    USERNAME = "test"
    PASSWORD = "test"

    # Prepare the payload
    payload = {
        "schema_type": SCHEMA_TYPE,
        "schema_name": SCHEMA_NAME
    }

    # Prepare the files for upload (schema file)
    files = {"schema": open(SCHEMA_FILE, "rb")}

    # Set the headers
    headers = {
        "Cookie": f"csrftoken={CSRF_TOKEN}",
        "Authorization": "Basic " + base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()
    }

    try:
        # Make the POST request
        response = requests.post(API_ENDPOINT, data=payload, files=files, headers=headers)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the response JSON
        response_json = response.json()

        # Extract the schema ID from the response
        schema_id = response_json["result"]["data"]["schema_id"]
        return schema_id
        # print("Request was successful!")
        # print(f"Schema ID: {schema_id}")
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)

def run_prompt():
    url = "https://<Paste the same url as of step 8>/prompt/v3"
    prompt = "<Enter your prompt>"
    schema_id = "<Paste your schema id>"
    headers = {
        "Content-Type": "application/json",
        "Cookie": "csrftoken=SWTHvaNeh4g3KImyRotjdDcMYuiW0dw4ctce3LXEkRWHJx71t7nKMLCk70wSdSSB"
    }
    auth = ("test", "test")
    data = {
        "prompt": prompt,
        "schema_id": schema_id
    }

    try:
        response = requests.post(url, json=data, headers=headers, auth=auth)
        response.raise_for_status()
        print("Request was successful!")
        print("Response:")
        print(response.json())  # If the response is in JSON format
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)

