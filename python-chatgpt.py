import requests

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

request_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

request_data = {
    'model': 'text-davinci-003',
    'prompt': "write a python script to take user birthday and claculate present ages bases on present date ",
    'max_tokens': 1000,
    'temperature': 0.5,
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code ==200:
    print(response.json()["choices"][0]["text"]) 
else:
    print("Request failed with status code: " + str(response.status_code))

