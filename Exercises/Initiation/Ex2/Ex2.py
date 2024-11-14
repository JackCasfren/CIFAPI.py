
#! Before starting, type "pip install requests" in your terminal.

import requests
import base64

def login(url, username, password):
    try:
        # Method 1: Using the auth parameter with out base64 encoding
        #response = requests.get(url, auth=(username, password))
        
        # Method 2: Setting the Authorization header directly
        credentials = username + ":" + password
        # Encoding both username and password
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        print("These are the enconded credentials: " + encoded_credentials)

        headers = {"Authorization": f"Basic {encoded_credentials}"}
        response = requests.get(url, headers=headers)
        
        # Check the status code
        if response.status_code == 200:
            print("Authentication successful!")
            print(f"Unexpected status code: {response.status_code}")
        elif response.status_code == 401:
            print("Authentication failed. Incorrect credentials.")
            print(f"Unexpected status code: {response.status_code}")
        else:
            print(f"Unexpected status code: {response.status_code}")
        
        # Print the status code and response content
        print(f"Status Code: {response.status_code}")
        print("Response Content:")
        print(response.text)
        
        return response
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while triying to login: {e}")
        return None

# API details
url = "http://echo.getpostman.com/basic-auth"
username = "postman"
password = "password"

# Make the request
login(url, username, password)