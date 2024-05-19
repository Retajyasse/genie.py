import requests
import json
import sys

# Replace with your actual API key
API_KEY = "AIzaSyCh8TqW6eBjcfjyoDbkVAEWQ1RMrAk7-VM"
text=" "

if len(sys.argv)>1:
    text='Help with any question i ask about linux bash commands only if my question is off topic please only say : "sorry i only answer bash specific questions ".so my question is '+sys.argv[1]
else:
    exit()


# Build the URL with your API key
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"


# Define the request body
request_body = {
 "contents": [
        {
            "parts": [
                {
                    "text":text
                    }
                ]
                    }
            ]
        }



# Set headers
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, headers=headers, json=request_body)

# Check for successful response
if response.status_code == 200:
  # Parse the JSON response
  data = response.json().get('candidates')[0].get('content').get('parts')[0].get('text')
  # Access the generated text
  print(data)
else:
      print(f"Error: {response.status_code}")
