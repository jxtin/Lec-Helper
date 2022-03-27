import requests
import os
import time
import sys

filename = "taunt.mp3"
# api_key = "a796f06a2bce49479d5c534e4b3fb1ae"
api_key = "9235d5e64de54e9c9836f0e653ea51e1"

def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data


headers = {'authorization': api_key}
response = requests.post('https://api.assemblyai.com/v2/upload',
                         headers=headers,
                         data=read_file(filename))

audio_url = response.json()['upload_url']

endpoint = "https://api.assemblyai.com/v2/transcript"
json = { "audio_url": audio_url }
headers = {
    "authorization": api_key,
    "content-type": "application/json"
}
response = requests.post(endpoint, json=json, headers=headers)
response_json = response.json()
print(response_json)

status = ''
while status != 'completed':
    response_result = requests.get(
        os.path.join(endpoint, response_json['id']),
        headers=headers
    )
    status = response_result.json()['status']
    print(f'Status: {status}')

    if status == 'error':
        sys.exit('Audio file failed to process.')
    elif status != 'completed':
        time.sleep(5)

transcript = response_result.json()['text']
print(transcript)

with open('transcript.txt', 'w') as f:
    f.write(transcript)